from fastapi import FastAPI
from .database import get_db

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Patient Service Running"}

@app.get("/test-db")
def test_db():
    result = get_db()
    return{"db_status":result}