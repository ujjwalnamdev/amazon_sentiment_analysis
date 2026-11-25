# Frontend – Amazon Product Review Intelligence

The frontend provides an interactive user interface for analyzing customer reviews of Amazon products. It allows users to submit an Amazon product URL, initiate review collection, and explore sentiment analysis results through an interactive dashboard.

The application is built using Streamlit and communicates with the FastAPI backend through HTTP REST API requests.

## Directory Structure

```text
frontend/
│
├── Home.py
│
└── pages/
    └── dashboard.py
```


###  Interactive Sentiment Analysis Dashboard

Displays important review analytics through metric cards:

- Total Reviews
- Positive Reviews
- Negative Reviews
- Neutral Reviews
- Average Customer Rating


## Application Workflow

1. User enters an Amazon product URL.
2. Streamlit sends a POST request to the FastAPI backend.
3. Backend initiates review collection and returns a snapshot ID.
4. Frontend stores the snapshot ID in session state.
5. User is redirected to the dashboard.
6. Dashboard sends a GET request using the snapshot ID.
7. Frontend waits for the analysis to complete.
8. The backend returns review data with predicted sentiment labels.
9. Streamlit displays sentiment metrics, rating distribution, and individual customer reviews.

## Running the Frontend

Run the following command from the project root:

```bash
streamlit run frontend/Home.py
```


**Part of the Amazon Product Review Intelligence project.**