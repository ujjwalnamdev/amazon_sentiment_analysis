# Backend – Amazon Product Review Intelligence

The backend is responsible for handling API requests, collecting Amazon product reviews, processing review data, and generating sentiment analysis results using the trained machine learning model.

It acts as the communication layer between the Streamlit frontend, the review collection service, and the sentiment analysis model.


## Directory Structure

```text
backend/
│
└── app.py
```

## Application Workflow

1. The frontend submits an Amazon product URL to the backend.
2. The backend initiates the review collection process.
3. A snapshot ID is returned to the frontend.
4. The frontend uses the snapshot ID to request analysis.
5. The backend retrieves the collected reviews.
6. Review text is processed and passed to the trained sentiment classification model.
7. Predicted sentiment results are returned to the frontend.
8. The frontend displays the results through an interactive dashboard.

### . Start the FastAPI Server through

Run:

```bash
uvicorn backend.app:app --reload
```


**Part of the Amazon Product Review Intelligence project.**