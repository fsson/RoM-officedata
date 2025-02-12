import subprocess
import sys

def install(package):
  try:
    __import__(package)
  except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

packages = ['requests', 'pandas', 'json', 'datetime']

for p in packages:
    install(p)

import requests
import pandas as pd
import json
from datetime import date

def fetch_data(page):
    response = requests.get(f"https://arbetsformedlingen.se/rest/rusta-och-matcha-2/sokleverantor/v2/leverantorer?sida={page}&tjanstekoder=A015")
    if response.status_code == 200:
        data = response.json()
        if data.get("total_count", 0) == 0:
            return None  
        suppliers = data.get("leverantorer", [])
        if not suppliers:
            return None
        return data
    print(f"Request failed: status code {response.status_code}")

def fetch_iterator():
    all_data = []
    page = 1
    while True:
        print(f"Fetching from page {page}")
        data = fetch_data(page)
        if data is None:
            return all_data
            break
        all_data.append(data)
        page += 1

def create_file():
    data = fetch_iterator()
    if data:
        today = date.today()
        with open(f"data/raw/office_data_{today}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("File successfully created.")
    else:
        print(f"Something went wrong! File creation aborted.")

create_file()