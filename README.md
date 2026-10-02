# 🚀 HealthRisk AI — Smart Cardiovascular Risk Screening System

An end-to-end Machine Learning driven web application designed for early-stage health risk screening and analytical assessment using patient biometrics, clinical vitals, and lifestyle risk factors.

---

## 📌 Project Overview & Purpose
**HealthRisk AI** evaluates clinical parameters to estimate a patient's cardiovascular health risk level. It aims to bridge the gap between preliminary screening and formal diagnostic procedures by serving as an automated risk stratification tool.

> **Note:** This system is built for screening/prediction purposes only and does not serve as a medical diagnosis replacement.

---

## 🏗️ System Architecture
```text
                 USER
                   ↓
     HTML5 + CSS3 + JS Dashboard
                   ↓
             FastAPI (REST API)
                   ↓
        Input Validation (Pydantic)
                   ↓
        Data Preprocessing & Scaling
                   ↓
    ML Ensemble (Random Forest Classifier)
                   ↓
   ┌───────────────────────┴───────────────────────┐
   ↓                                               ↓
MySQL / SQLite Database                       Diagnostic Result
   ↓                                               ↓
Prediction History Record                      Dynamic Clinical Report

🛠️ Tech Stack & ToolsFrontend: HTML5, Modern CSS3 (Glassmorphism & Flex/Grid Layouts), Vanilla JavaScript (Fetch API)Backend: FastAPI, Uvicorn, PydanticMachine Learning: Python, Scikit-Learn, Pandas, NumPy, JoblibDatabase: SQLite / MySQL (Assessment History Records)Version Control: Git & GitHub📊 Machine Learning Model BenchmarksMultiple classification models were trained and evaluated on 10,000 processed patient records:ModelAccuracyPrecisionRecallF1-ScoreLogistic Regression88.8%89.5%87.9%88.7%K-Nearest Neighbors (KNN)84.6%88.3%79.9%83.9%Random Forest Classifier93.1%93.6%92.5%93.1%Support Vector Machine (SVM)90.5%90.9%90.0%90.5%Selected Model: Random Forest Classifier (saved as ml/model.pkl with preprocessor pipeline ml/preprocessor.pkl).⚙️ Project Setup & Installation Instructions1. Clone & NavigateBashgit clone [https://github.com/your-username/HealthRisk-AI.git](https://github.com/your-username/HealthRisk-AI.git)
cd HealthRisk-AI
2. Virtual Environment SetupPowerShellpython -m venv venv
.\venv\Scripts\activate
3. Install DependenciesBashpip install -r requirements.txt
4. Generate Dataset & Train ML ModelBashpython ml/generate_dataset.py
python ml/train.py
5. Launch FastAPI Backend ServerBashuvicorn backend.main:app --reload
API Documentation / Swagger UI: http://127.0.0.1:8000/docs6. Run Frontend DashboardOpen frontend/assessment.html in any web browser.🔌 Core API EndpointsPOST /predict: Accepts JSON payload of patient parameters and returns risk prediction status, probability score, and BMI.GET /history/{user_id}: Retrieves previous health assessment logs for a specific user.
---

### Git Commit & Push Commands

Apne project ko GitHub par upload karne ke liye terminal par ye sequence run karo:

```powershell
git init
git add .
git commit -m "Complete HealthRisk AI Major Project Setup with 93.1% F1 ML Model and Modern UI"
git branch -M main
git remote add origin https://github.com/your-username/HealthRisk-AI.git
git push -u origin main
