from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    email: EmailStr
    address: str

class PatientResponse(BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes=True
