# Models – Sentiment Analysis

This directory contains the trained machine learning model and prediction logic used to classify Amazon customer reviews into sentiment categories.

## Files

- `model.pkl` – Trained sentiment classification model.
- `prediction.py` – Handles review preprocessing and sentiment prediction.

## Functionality

- Processes customer review text.
- Generates sentiment predictions.
- Classifies reviews as **Positive, Negative, or Neutral**.

The trained model is integrated with the FastAPI backend to provide sentiment predictions for collected product reviews.