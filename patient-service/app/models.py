from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Patient():
    __tablename__= "patients"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    age=Column(Integer)
    gender=Column(String)
    phone=Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    address=Column(String)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
