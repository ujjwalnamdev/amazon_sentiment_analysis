import requests
from api import API_KEY

PROGRESS_URL = "https://api.brightdata.com/datasets/v3/progress"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def check_snapshot_status(snapshot_id: str):

    url = f"{PROGRESS_URL}/{snapshot_id}"

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()
    
    return response.json()


DOWNLOAD_URL = "https://api.brightdata.com/datasets/v3/snapshot"

def download_reviews(snapshot_id:str):

    url = f"{DOWNLOAD_URL}/{snapshot_id}"

    response = requests.get(
        url,
        headers = headers,
        params = {"format":"json"},
        timeout = 60
    )

    response.raise_for_status()
    return response.json()



# # if __name__=="__main__":
# #     snapshot_id = "sd_mwm04gg9yoc6ivvd2"
# #     status = check_snapshot_status(snapshot_id)
# #     print("Snapshot Status:",status)  


# # if __name__ =="__main__":
# #     snapshot_id = "sd_mwm04gg9yoc6ivvd2"
# #     reviews = download_reviews(snapshot_id)
# #     print("Reviews:",reviews)

# snapshot_id = "sd_mwm04gg9yoc6ivvd2"
# reviews = download_reviews(snapshot_id)
# print(type(reviews))
# print(len(reviews))
# print(reviews[0])