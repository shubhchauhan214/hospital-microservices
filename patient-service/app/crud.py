from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional

def create_patient(db: Session, patient:schemas.PatientCreate):
    new_patient=models.Patient(**patient.dict())
    db.add(new_patient)
    db.commit
    db.refresh(new_patient)
    return new_patient

def search_patients(db: Session,
                    id:Optional[int]=None,
                    name:Optional[str]=None,
                    phone:Optional[str]=None,
                    email:Optional[str]=None):
    query =db.query(models.Patient)

    if id:
        query=query.filter(models.Patient.id == id)
    if name:
        query=query.filter(models.Patient.name.ilike(f"%{name}%"))
    if phone:
        query=query.filter(models.Patient.phone == phone)
    if email:
        query=query.filter(models.Patient.email == email)

    return query.all()
    