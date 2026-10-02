import sqlite3
import os

DB_PATH = "healthrisk.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)
    
    # Assessments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        age INTEGER,
        gender INTEGER,
        height REAL,
        weight REAL,
        bmi REAL,
        systolic_bp INTEGER,
        diastolic_bp INTEGER,
        glucose INTEGER,
        cholesterol INTEGER,
        physical_activity INTEGER,
        smoking INTEGER,
        alcohol INTEGER,
        sleep_hours INTEGER,
        family_history INTEGER,
        prediction INTEGER,
        risk_level TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    conn.commit()
    conn.close()