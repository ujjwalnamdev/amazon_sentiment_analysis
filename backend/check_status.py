import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BRIGHT_DATA_API_KEY")

snapshot_id = "sd_mwj3g54n2m2mttso1y"

url = f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Job status:", response.json())

download_url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}"

download_response = requests.get(
    download_url,
    headers=headers,
    params={"format": "json"},
    timeout=60
)

print("Download status:", download_response.status_code)
print("Downloaded data:")
print(download_response.text[:5000])