import joblib
from review_service import download_reviews
from preprocessing import preprocess_text

with open("models/model.pkl","rb") as f:
    model = joblib.load(f)



def predict_sentiment(reviews):

    #Extract reviews text

    review_texts = [
        review["review_text"]
        for review in reviews
        if review.get("review_text")
    ]

    prediction = model.predict(review_texts)

    return review_texts, prediction 

if __name__ == "__main__":

    snapshot_id = "sd_mwm04gg9yoc6ivvd2"

    reviews = download_reviews(snapshot_id)

    review_texts, prediction = predict_sentiment(reviews)


    for review_text, prediction in zip(review_texts, prediction  ):
        print("Review:", review_text, "Sentiment:", prediction)