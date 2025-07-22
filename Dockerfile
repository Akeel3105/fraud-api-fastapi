# backend/Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Copy backend files and ML model
COPY . /app

# Copy model from one level up
COPY ../ml/model_fraud_rf.pkl /app/model_fraud_rf.pkl

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn scikit-learn pandas

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
