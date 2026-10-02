import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 10000

# Generating Realistic Features
age = np.random.randint(18, 80, size=n_samples)
gender = np.random.choice([0, 1], size=n_samples)  # 0: Female, 1: Male
height = np.random.normal(165, 10, size=n_samples).round(1)  # in cm
weight = np.random.normal(70, 15, size=n_samples).round(1)   # in kg

systolic_bp = np.random.randint(90, 180, size=n_samples)
diastolic_bp = np.random.randint(60, 110, size=n_samples)

glucose = np.random.choice([1, 2, 3], size=n_samples, p=[0.7, 0.2, 0.1])       # 1: Normal, 2: Above Normal, 3: High
cholesterol = np.random.choice([1, 2, 3], size=n_samples, p=[0.65, 0.25, 0.1])  # 1: Normal, 2: Above Normal, 3: High

physical_activity = np.random.choice([0, 1], size=n_samples, p=[0.4, 0.6]) # 0: Low, 1: Moderate/High
smoking = np.random.choice([0, 1], size=n_samples, p=[0.75, 0.25])
alcohol = np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])
sleep_hours = np.random.randint(4, 10, size=n_samples)
family_history = np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])

# Calculate Derived Feature: BMI
bmi = (weight / ((height / 100) ** 2)).round(1)

# Synthetic Risk Score Formula (Medical-Based Rules)
risk_score = (
    (age > 50) * 1.5 +
    (bmi > 25) * 1.2 +
    (bmi > 30) * 1.8 +
    (systolic_bp > 130) * 1.5 +
    (diastolic_bp > 85) * 1.2 +
    (glucose - 1) * 1.2 +
    (cholesterol - 1) * 1.3 +
    (smoking == 1) * 1.5 +
    (alcohol == 1) * 0.8 +
    (physical_activity == 0) * 1.0 +
    (sleep_hours < 6) * 1.0 +
    (family_history == 1) * 1.5
)

# Convert Risk Score to Binary Target (0: Low Risk, 1: High Risk)
threshold = np.percentile(risk_score, 50)
target = (risk_score >= threshold).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'age': age,
    'gender': gender,
    'height': height,
    'weight': weight,
    'bmi': bmi,
    'systolic_bp': systolic_bp,
    'diastolic_bp': diastolic_bp,
    'glucose': glucose,
    'cholesterol': cholesterol,
    'physical_activity': physical_activity,
    'smoking': smoking,
    'alcohol': alcohol,
    'sleep_hours': sleep_hours,
    'family_history': family_history,
    'target': target
})

# Save to CSV
df.to_csv('ml/dataset/health_data.csv', index=False)
print("10,000 records successfully generated at 'ml/dataset/health_data.csv'!")