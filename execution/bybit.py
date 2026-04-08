import requests
import time
import hmac
import hashlib
from config import BYBIT_API_KEY, BYBIT_API_SECRET, PAPER_TRADING

BASE_URL = "https://api.bybit.com"

def place_order(side, qty):
    if PAPER_TRADING:
        print(f"[PAPER] {side} order geplaatst: {qty}")
        return

    endpoint = "/v5/order/create"

    timestamp = str(int(time.time() * 1000))

    payload = {
        "category": "linear",
        "symbol": "XRPUSDT",
        "side": side,
        "orderType": "Market",
        "qty": str(qty),
        "timeInForce": "GTC"
    }

    payload_str = str(payload)

    signature = hmac.new(
        BYBIT_API_SECRET.encode(),
        payload_str.encode(),
        hashlib.sha256
    ).hexdigest()

    headers = {
        "X-BAPI-API-KEY": BYBIT_API_KEY,
        "X-BAPI-SIGN": signature,
        "X-BAPI-TIMESTAMP": timestamp
    }

    response = requests.post(BASE_URL + endpoint, headers=headers, json=payload)

    return response.json()
