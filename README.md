Qualifier – A Shopping Assistant 🛍️

Overview 

Qualifier is an Amazon Product Review Sentiment Analysis application built using Natural Language Processing (NLP) and Machine Learning.

It analyzes Amazon product reviews and classifies customer opinions into three sentiment categories: Positive, Negative, and Neutral.

The application helps users understand customer feedback and gain insights into product reviews through an interactive dashboard.

Sentiment Categories

1.Positive: Reviews expressing satisfaction or a favourable opinion.

2.Negative: Reviews expressing dissatisfaction or an unfavourable opinion.

3.Neutral: Reviews expressing neither a clearly positive nor a negative opinion.

## Dataset Source

- **Original Dataset:** Amazon Reviews 2023
- **Research Group:** McAuley Research Group
- **Source:** [Hugging Face – Amazon Reviews 2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)
- **Format:** Parquet
- **Data Type:** Customer reviews and related product information

## Categories Included

The dataset contains reviews from the following five categories:

| No. | Category | Reviews |
|:---:|---|---:|
| 1 | Electronics | 20,000 |
| 2 | Health and Personal Care | 20,000 |
| 3 | Handmade Products | 20,000 |
| 4 | Arts, Crafts and Sewing | 20,000 |
| 5 | Digital Music | 20,000 |
| | **Total** | **100,000** |


## Features

- Extract Amazon product reviews using an API.
- Clean and preprocess review text.
- Perform sentiment classification.
- Classify reviews into Positive, Negative, and Neutral.
- Display sentiment distribution.
- Analyze customer feedback through an interactive dashboard.


## Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Machine Learning:** Scikit-learn
- **NLP:** NLTK
- **Text Feature Extraction:** TF-IDF
- **ML Algorithm:** Complement Naive Bayes
- **Data Processing:** Pandas, NumPy
- **API Integration:** Requests


## Project Architecture

            Streamlit Frontend 
                  ↓ 
            FastAPI Backend 
                  ↓
            Review Extraction and Preprocessing 
                  ↓
            ML Prediction Pipeline 
                  ↓
            Sentiment Analysis Dashboard


## Project folder architecture

amazon_sentiment_analysis/
│
├── backend/
├── frontend/
│   └── pages/
├── models/
├── schema/
├── .gitignore
├── README.md
└── requirements.txt


## Installation and Setup

### a. Clone the repository

git clone <your-repository-url>

### b. Navigate to the project directory

cd amazon_sentiment_analysis

### c. Create a virtual environment

python -m venv venv

### d. Activate the environment

Windows:

venv\Scripts\activate

### e. Install dependencies

pip install -r requirements.txt


## 7.Environment Variables

Create a `.env` file in the project root:

Replace your_api_key_here with your actual API key.
API_KEY=your_api_key_here

## 8. Run this project through

# Start FastAPI backend
uvicorn backend.app:app --reload

# Start Streamlit frontend
streamlit run frontend/Home.py


## Demo video

A demonstration of the application.
link- []

## Future Improvements

Support more Amazon product categories.

Improve sentiment classification performance.

Introduce aspect-based sentiment analysis.

Provide more detailed customer feedback insights.



## Author 
Ujjwal Namdev