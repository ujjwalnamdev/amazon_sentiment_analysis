
import streamlit as st
import requests

st.set_page_config(
    page_title="Amazon Review Intelligence",
    page_icon="🛒",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

st.title("🛒 Amazon Review Analysis")

st.write(
    "Discover what customers really think about a product."
)

st.divider()

product_url = st.text_input(
    "Enter Amazon Product URL",
    placeholder="https://www.amazon.in/dp/PRODUCT_ID"
)

if st.button("Submit", type="primary"):

    if not product_url:
        st.warning("Please enter an Amazon product URL.")

    else:
        try:
            with st.spinner("Starting product analysis..."):

                response = requests.post(
                    f"{API_URL}/scrape",
                    json={"product_url": product_url},
                    timeout=30
                )

                response.raise_for_status()

                data = response.json()

                snapshot_id = data["snapshot_id"]

                # Store data for the dashboard page
                st.session_state["snapshot_id"] = snapshot_id
                st.session_state["product_url"] = product_url

                # Reset previous product analysis
                st.session_state.pop("analysis_result", None)
                st.session_state.pop("analysis_snapshot_id", None)
                
                # Navigate to dashboard
                st.switch_page("pages/dashboard.py")

        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {e}")
