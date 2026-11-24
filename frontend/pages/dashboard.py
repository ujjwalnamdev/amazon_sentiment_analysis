import streamlit as st
import requests
import time

st.set_page_config(
    page_title = "Product Analysis Dashboard",
    page_icon = "📊",
    layout = "wide"
)

API_URL = "http://127.0.0.1:8000"

st.title("📊 Product Analysis Dashboard")

#Step 1: Get snapshot id from session state
snapshot_id = st.session_state.get("snapshot_id")

if not snapshot_id:
    st.warning("No product analysis found. Please analyze a product first.")
    st.stop()



#Step 3:check if results are already available
if "analysis_result" not in st.session_state:

    status_message = st.empty()
    status_message.info("Analyzing your product reviews")

    try:
        while True:
            response = requests.get(
                f"{API_URL}/analyze/{snapshot_id}",
                timeout=60
            )
            response.raise_for_status()

            result = response.json()

            if result["status"] == "completed":
                st.session_state["analysis_result"] = result
                break

            time.sleep(5)

        status_message.success("Analysis completed successfully")

    except requests.exceptions.RequestException as e:
        st.error(f"API Error:{e}")
        st.stop()


#Step 4:Get final analysis result

result = st.session_state["analysis_result"]

# Extract results
reviews = result["results"]


# Count sentiments
total_reviews = len(reviews)

positive_count = sum(
    1 for review in reviews
    if str(review["sentiment"]).lower() == "positive"
)

negative_count = sum(
    1 for review in reviews
    if str(review["sentiment"]).lower() == "negative"
)

neutral_count = sum(
    1 for review in reviews
    if str(review["sentiment"]).lower() == "neutral"
)


# Extract valid ratings
ratings = []

for review in reviews:
    rating = review.get("rating")

    try:
        if rating is not None:
            ratings.append(float(rating))
    except (ValueError, TypeError):
        pass

# Calculate average rating
average_rating = (
    sum(ratings) / len(ratings)
    if ratings else 0
)

# Dashboard heading
st.subheader("📊 Review Analytics")

# Display metric cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Reviews",
    total_reviews
)

col2.metric(
    "Positive Reviews",
    positive_count
)

col3.metric(
    "Negative Reviews",
    negative_count
)

col4.metric(
    "Neutral Reviews",
    neutral_count
)

col5.metric(
    "Average Rating",
    f"{average_rating:.1f} ⭐",
    help=f"Calculated from {len(ratings)} valid customer ratings"
)

st.divider()

# Rating distribution
st.subheader("⭐ Customer Rating Distribution")

rating_cols = st.columns(5)

for i, rating_value in enumerate([5, 4, 3, 2, 1]):

    count = sum(
        1 for rating in ratings
        if rating == rating_value
    )

    rating_cols[i].metric(
        f"{rating_value} Star",
        count
    )

st.divider()

st.subheader("Analysis Summary")

st.write("Total Reviews:", result["total_reviews"])

st.divider()

def apply_filter(reviews):
    selected_sentiment = st.selectbox(
        "Filter Reviews by Sentiment",
        ["All", "Positive", "Negative", "Neutral"]
    )

    if selected_sentiment == "All":
        return reviews

    filtered_reviews = [
        review for review in reviews
        if str(review["sentiment"]).lower() == selected_sentiment.lower()
    ]

    return filtered_reviews


# Step 5: Display Individual Reviews
st.subheader("Customer Reviews")

filtered_reviews = apply_filter(reviews)

st.write(f"Showing {len(filtered_reviews)} reviews")

for review in filtered_reviews:
    st.write("Rating:", review["rating"], "⭐")
    st.write("Review:", review["review"])
    st.write("Predicted_Sentiment:", review["sentiment"])
    st.divider()
