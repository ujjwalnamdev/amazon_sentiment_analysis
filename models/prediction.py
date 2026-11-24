import joblib
import __main__
from pathlib import Path
from schema.review_service import download_reviews



with open("models/model.pkl","rb") as f:
    model = joblib.load(f)



def predict_sentiment(reviews):

    #Extract reviews text

    review_texts = [
        review["review_text"]
        for review in reviews
        if review.get("review_text")
    ]
    rating = [
        review.get("rating")
        for review in reviews
    ]

    prediction = model.predict(review_texts)

    return rating, review_texts, prediction 

if __name__ == "__main__":

    snapshot_id = "sd_mwm04gg9yoc6ivvd2"

    reviews = download_reviews(snapshot_id)

    rating, review_texts, prediction = predict_sentiment(reviews)


    for rating, review_text, prediction in zip(rating, review_texts, prediction  ):
        print("Rating:", rating,"Review:", review_text, "Sentiment:", prediction)