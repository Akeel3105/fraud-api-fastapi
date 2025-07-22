# backend/model_utils.py

import joblib
import pandas as pd
import os



# Load the trained model
# model = joblib.load(r'D:\fraud-detection-ecommerce\backend\model_fraud_rf.pkl')
# model = joblib.load(os.path.join(os.path.dirname(__file__), 'model_fraud_rf.pkl'))

model_path = os.path.join(os.path.dirname(__file__), 'model_fraud_rf.pkl')
model = joblib.load(model_path)

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
