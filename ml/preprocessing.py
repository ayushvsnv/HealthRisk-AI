import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class HealthDataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_columns = [
            'age', 'gender', 'height', 'weight', 'bmi', 
            'systolic_bp', 'diastolic_bp', 'pulse_pressure',
            'glucose', 'cholesterol', 'physical_activity', 
            'smoking', 'alcohol', 'sleep_hours', 'family_history'
        ]

    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        # BMI Calculation if missing
        if 'bmi' not in df.columns or df['bmi'].isnull().any():
            df['bmi'] = (df['weight'] / ((df['height'] / 100) ** 2)).round(1)
        
        # Pulse Pressure Calculation (Systolic - Diastolic)
        df['pulse_pressure'] = df['systolic_bp'] - df['diastolic_bp']
        
        return df[self.feature_columns]

    def fit_transform(self, df: pd.DataFrame) -> np.ndarray:
        df_processed = self.create_features(df)
        return self.scaler.fit_transform(df_processed)

    def transform(self, df: pd.DataFrame) -> np.ndarray:
        df_processed = self.create_features(df)
        return self.scaler.transform(df_processed)