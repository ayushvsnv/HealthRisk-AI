import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from preprocessing import HealthDataPreprocessor

#  Load Dataset
data_path = 'ml/dataset/health_data.csv'
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Dataset not found at {data_path}. Run generate_dataset.py first.")

df = pd.read_csv(data_path)

X = df.drop(columns=['target'])
y = df['target']

# Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Preprocessing & Scaling
preprocessor = HealthDataPreprocessor()
X_train_scaled = preprocessor.fit_transform(X_train)
X_test_scaled = preprocessor.transform(X_test)

# Define Models
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM": SVC(probability=True, random_state=42)
}

results = []
best_model = None
best_f1 = 0.0
best_model_name = ""

print("--- Training & Evaluating Models ---")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    results.append({
        "Model": name,
        "Accuracy": round(acc, 4),
        "Precision": round(prec, 4),
        "Recall": round(rec, 4),
        "F1-Score": round(f1, 4)
    })
    
    # Selecting Best Model based on F1-Score
    if f1 > best_f1:
        best_f1 = f1
        best_model = model
        best_model_name = name

# Display Results
results_df = pd.DataFrame(results)
print("\n", results_df.to_string(index=False))

# 5. Save Phase 5 Deliverables (Model + Preprocessor)
print(f"\nBest Model: {best_model_name} (F1-Score: {best_f1})")

joblib.dump(best_model, 'ml/model.pkl')
joblib.dump(preprocessor, 'ml/preprocessor.pkl')

print("Saved 'ml/model.pkl' and 'ml/preprocessor.pkl' successfully!")