# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all contents of backend folder to /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn numpy==1.23.5 scikit-learn==1.2.2 pandas joblib


# Expose the port FastAPI runs on
EXPOSE 8000

# Run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
