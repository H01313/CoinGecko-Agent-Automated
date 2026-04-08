#!/usr/bin/env python3
print("🚀 COINGECKO BTC TRADER")
import json
from datetime import datetime
import requests

# Live BTC
data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()
price = data['bitcoin']['usd']

# RSI sim
rsi = 28.5
trade = {
  "time": str(datetime.now()),
  "symbol": "BTC/USDT",
  "action": "buy",
  "price": price,
  "rsi": rsi,
  "winrate": 0
