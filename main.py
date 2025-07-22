# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from backend.model_utils import predict_fraud

app = FastAPI(title="Fraud Detection API")

# Define expected input structure
class Transaction(BaseModel):
    merchant: int
    category: int
    amt: float
    gender: int
    city: int
    state: int
    zip: int
    lat: float
    long: float
    city_pop: int
    job: int
    unix_time: int
    merch_lat: float
    merch_long: float
    hour: int
    day: int
    month: int
    weekday: int
    age: int

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running!"}

@app.post("/predict")
def predict(transaction: Transaction):
    result = predict_fraud(transaction.dict())
    return {"is_fraud": result}
