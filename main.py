#!/usr/bin/env python3
print("🚀 COINGECKO BTC TRADER LIVE!")
import json
from datetime import datetime
import requests

# Live BTC price
data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids
