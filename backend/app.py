from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from backend.api import trigger_scraping
import joblib
import __main__
from backend.preprocessing import clean_text, preprocess_text
from backend.review_service import(check_snapshot_status, download_reviews)
from backend.prediction import predict_sentiment


__main__.clean_text = clean_text
__main__.preprocess_text = preprocess_text

# Load ML model
with open('backend/models/model.pkl', 'rb') as f:
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

class ProductRequest(BaseModel):
    product_url : HttpUrl

@app.post("/scrape")
def scrape_product(request:ProductRequest):

    try: 
        snapshot_id = trigger_scraping(str(request.product_url))

        
        return{
            "message":"Scraping started successfully",
            "snapshot_id":snapshot_id
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail = str(e)
        )
    
@app.get("/analyze/{snapshot_id}")
def analyze_product(snapshot_id: str):

    try:
        status_data = check_snapshot_status(snapshot_id)

        if status_data["status"] != "ready":
            return {
                "status": status_data["status"],
                "message": "Scraping is not completed yet"
            }

        reviews = download_reviews(snapshot_id)

        rating, review_texts, predictions = predict_sentiment(reviews)

        results = []

        for rating, review_text, prediction in zip(rating, review_texts, predictions):
            results.append({
                "rating":rating,
                "review": review_text,
                "sentiment": str(prediction)
            })

        return {
            "status": "completed",
            "total_reviews": len(results),
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 