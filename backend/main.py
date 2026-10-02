import sys
import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Python path configuration
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ml')))

# Updated Imports with backend. prefix
from backend.database.db import init_db, get_db
from backend.schemas.assessment import AssessmentRequest

app = FastAPI(title="HealthRisk AI API", version="1.0")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()
    global model, preprocessor
    try:
        model = joblib.load('ml/model.pkl')
        preprocessor = joblib.load('ml/preprocessor.pkl')
        print("ML Model & Preprocessor loaded successfully.")
    except Exception as e:
        print(f"Error loading ML artifacts: {e}")

@app.get("/")
def read_root():
    return {"message": "HealthRisk AI Backend is Running"}

@app.post("/predict")
def predict_risk(data: AssessmentRequest):
    try:
        input_dict = data.dict()
        user_id = input_dict.pop('user_id')
        
        df_input = pd.DataFrame([input_dict])
        
        scaled_features = preprocessor.transform(df_input)
        prediction = int(model.predict(scaled_features)[0])
        probabilities = model.predict_proba(scaled_features)[0]
        
        risk_level = "High Risk" if prediction == 1 else "Low Risk"
        risk_score = round(float(probabilities[1]) * 100, 2)
        
        bmi = round(data.weight / ((data.height / 100) ** 2), 1)
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO assessments (
                user_id, age, gender, height, weight, bmi, systolic_bp, diastolic_bp,
                glucose, cholesterol, physical_activity, smoking, alcohol, sleep_hours,
                family_history, prediction, risk_level
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, data.age, data.gender, data.height, data.weight, bmi,
            data.systolic_bp, data.diastolic_bp, data.glucose, data.cholesterol,
            data.physical_activity, data.smoking, data.alcohol, data.sleep_hours,
            data.family_history, prediction, risk_level
        ))
        conn.commit()
        assessment_id = cursor.lastrowid
        conn.close()
        
        return {
            "status": "success",
            "assessment_id": assessment_id,
            "prediction": prediction,
            "risk_level": risk_level,
            "risk_score_percentage": risk_score,
            "bmi": bmi
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history/{user_id}")
def get_history(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assessments WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]