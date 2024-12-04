import tkinter as tk

import requests
import time


CATEGORIES = {
    "Video Games": 15,
    "Computers": 18,
    "General Knowledge": 9,
    "Anime & Manga": 31,
    "Cartoons & Animations": 32,
}

OPENTDB_ENDPOINT = "https://opentdb.com/api.php"

params = {"amount": 5, "category": ""}

data_dict = {"data":[]}

for category, value in CATEGORIES.items():
    params["category"] = value
    try:
        print("Attempting HTTP Request to OpenTDB")
        response = requests.get(url=OPENTDB_ENDPOINT, params=params)
        response.raise_for_status()
    except requests.HTTPError as errh:
        print(f"HTPP Error: {errh}")
    except len(response.json()) == 0:
        print("Unsuccessful Request, Returned Empty")
    else:
        print("Successful Request")
        data = response.json()
        data_dict["data"].append(data)
    time.sleep(5)

print(data_dict)