from fastapi import FastAPI
from pydantic import BaseModel, Field
from pathlib import Path
import joblib
import __main__
from backend.preprocessing import clean_text, preprocess_text
from prediction import prediction
import review_service

__main__.clean_text = clean_text
__main__.preprocess_text = preprocess_text

# Load ML model
with open('models/model.pkl', 'rb') as f:
    model = joblib.load(f)

#MLFlow
MODEL_VERSION = '1.0.0'



#FastAPI application
app = FastAPI(
    title="Amazon Review Sentiment Analysis API",
    description="API for analyzing Amazon product reviews using machine learning",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Amazon Review Sentiment Analysis API is running"
    }

