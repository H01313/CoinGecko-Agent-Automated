import requests
import pandas as pd
import time

BASE_URL = "https://api.coingecko.com/api/v3"

def get_xrp_data():
    url = f"{BASE_URL}/coins/ripple/market_chart"
    
    params = {
        "vs_currency": "usd",
        "days": "1",
        "interval": "minute"
    }

    response = requests.get(url, params=params)
    data = response.json()

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    return df
