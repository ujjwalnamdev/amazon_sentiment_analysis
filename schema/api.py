import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BRIGHT_DATA_API_KEY")

endpoint = "https://api.brightdata.com/datasets/v3/trigger"


if not API_KEY:
    raise ValueError("API key not found")

def trigger_scraping(product_url, max_reviews= 20):
    Headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


    Parameters= {
        "dataset_id":"gd_le8e811kzy4ggddlq",
        "format":"json",  
        "include_errors":"true"
    }

    Payload = {
        "url": product_url,
        "max_reviews":max_reviews
    }

    response = requests.post(
        endpoint,
        params = Parameters,
        headers = Headers,
        json = Payload,
        timeout = 30
    )

    response.raise_for_status()

    Data = response.json()
    return Data["snapshot_id"]


