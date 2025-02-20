import requests
import json
from datetime import date

# Function for fetching JSON data from AF
def fetch_data(page):
    response = requests.get(f"https://arbetsformedlingen.se/rest/rusta-och-matcha-2/sokleverantor/v2/leverantorer?sida={page}&tjanstekoder=A015")
    # Fetch data if request succeeded
    if response.status_code == 200:
        data = response.json()
        # Return None at last page
        if data.get("total_count", 0) == 0:
            return None  
        suppliers = data.get("leverantorer", [])
        if not suppliers:
            return None
        return data
    # Return error if request failed
    print(f"Request failed: status code {response.status_code}")

# Function for applying fetch_data() to all pages and returning the combined result
def fetch_iterator():
    all_data = []
    page = 1
    while True:
        print(f"Fetching from page {page}", end="\r")
        data = fetch_data(page)
        # Break when fetch_data() returns None (last page)
        if data is None:
            return all_data
            break
        all_data.append(data)
        page += 1

# Function for creating JSON file out of combined JSON data
def create_json():
    data = fetch_iterator()
    # Write to file if data is returned
    if data:
        today = date.today()
        with open(f"data/raw/office_data_{today}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("File successfully created.")
    else:
        print(f"Something went wrong! File creation aborted.")