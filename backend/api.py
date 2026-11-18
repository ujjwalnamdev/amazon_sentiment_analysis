import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BRIGHT_DATA_API_KEY")

endpoint = "https://api.brightdata.com/datasets/v3/trigger"


product_url = "https://www.amazon.in/TIMEX-Leather-Tw00Zr262E-Color-Brown-Color-Blue/dp/B07H3T56MJ/ref=zg_bs_c_watches_d_sccl_6/521-6966738-1460955?pd_rd_w=jCul0&content-id=amzn1.sym.b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_p=b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_r=6T52M36KS9NP65NMCAW8&pd_rd_wg=2Fi5g&pd_rd_r=87ac7a26-e137-4071-9efa-5b5f26608483&pd_rd_i=B07H3K85H5&th=1"

if not API_KEY:
    raise ValueError("API key not found")

def trigger_scraping(product_url, max_reviews= 30):
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

    print("Status_code:",response.status_code)
    print("Response:", response.json())
    Data = response.json()
    return Data["snapshot_id"]



if __name__ == "__main__":
    product_url = "https://www.amazon.in/TIMEX-Leather-Tw00Zr262E-Color-Brown-Color-Blue/dp/B07H3T56MJ/ref=zg_bs_c_watches_d_sccl_6/521-6966738-1460955?pd_rd_w=jCul0&content-id=amzn1.sym.b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_p=b908f532-cbe7-4274-8b24-b671acc58bd2&pf_rd_r=6T52M36KS9NP65NMCAW8&pd_rd_wg=2Fi5g&pd_rd_r=87ac7a26-e137-4071-9efa-5b5f26608483&pd_rd_i=B07H3K85H5&th=1"

    snapshot_id = trigger_scraping(product_url)

    print("Snapshot_id:", snapshot_id)