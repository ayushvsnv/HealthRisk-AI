from pydantic import BaseModel, Field

class AssessmentRequest(BaseModel):
    user_id: int = 1
    age: int = Field(..., ge=1, le=120)
    gender: int = Field(..., ge=0, le=1)  # 0: Female, 1: Male
    height: float = Field(..., ge=50, le=250)
    weight: float = Field(..., ge=20, le=300)
    systolic_bp: int = Field(..., ge=70, le=250)
    diastolic_bp: int = Field(..., ge=40, le=150)
    glucose: int = Field(..., ge=1, le=3)
    cholesterol: int = Field(..., ge=1, le=3)
    physical_activity: int = Field(..., ge=0, le=1)
    smoking: int = Field(..., ge=0, le=1)
    alcohol: int = Field(..., ge=0, le=1)
    sleep_hours: int = Field(..., ge=1, le=24)
    family_history: int = Field(..., ge=0, le=1)