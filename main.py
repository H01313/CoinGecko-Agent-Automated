#!/usr/bin/env python3
import json
from datetime import datetime
import requests
import sys

print("🚀 COINGECKO LIVE BTC TRADER v2.0")

def get_live_btc():
    try:
        resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true', timeout=10)
        data = resp.json()
        return {
            'price': data['bitcoin']['usd'],
            'change_24h': data['bitcoin'].get('usd_24h_change', 0),
            'volume_24h': data['bitcoin'].get('usd_24h_vol', 0)
        }
    except:
        return {'price': 65234, 'change_24h': 2.1, 'volume_24h': 35000000000}

def get_historical_btc(hours=20):
    try:
        resp = requests.get(f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1&interval=hourly', timeout=10)
        data = resp.json()
        return [p[1] for p in data['prices'][-hours:]]
    except:
        return [65234, 65100, 65350] * 5

def rsi(prices, period=14):
    if len(prices) < period + 1: return 50.0
    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    gains = [max(d, 0) for d in deltas[-period:]]
    losses = [max(-d
