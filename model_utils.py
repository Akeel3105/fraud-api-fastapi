# backend/model_utils.py

import joblib
import pandas as pd

# Load the trained model
model = joblib.load(r'D:\fraud-detection-ecommerce\ml\model_fraud_rf.pkl')

# Define required features (order must match training!)
FEATURE_COLUMNS = [
    'merchant', 'category', 'amt', 'gender', 'city', 'state',
    'zip', 'lat', 'long', 'city_pop', 'job', 'unix_time',
    'merch_lat', 'merch_long', 'hour', 'day', 'month', 'weekday', 'age'
]

def predict_fraud(input_dict):
    df = pd.DataFrame([input_dict], columns=FEATURE_COLUMNS)
    prediction = model.predict(df)[0]
    return bool(prediction)
