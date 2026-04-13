import json
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import requests
import ta

# Jouw bestaande code + dashboard export
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def get_xrp_data():
    url = "https://api.coingecko.com/api/v3/coins/ripple/market_chart"
    params = {"vs_currency": "usd", "days": "1", "interval": "minute"}
    response = requests.get(url, params=params)
    data = response.json()
    prices = data.get("prices", [])
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    return df

class RSIStrategy:
    def __init__(self, period=14):
        self.period = period
    def calculate_rsi(self, df):
        df = df.copy()
        df["rsi"] = ta.momentum.RSIIndicator(close=df["price"], window=self.period).rsi()
        return df
    def generate_signal(self, df):
        latest = df.iloc[-1]
        if latest["rsi"] < 30: return "BUY"
        if latest["rsi"] > 70: return "SELL"
        return "HOLD"

class PaperTrader:
    def __init__(self, balance=1000):
        self.balance = balance
        self.position = None
        self.entry_price = None
        self.trade_history = []
    def buy(self, price):
        if self.position is None:
            self.position = "LONG"
            self.entry_price = price
    def sell(self, price):
        if self.position == "LONG":
            self.balance += (price - self.entry_price)
            self.trade_history.append({"profit": price - self.entry_price})
            self.position = None
            self.entry_price = None
    def stats(self):
        return 0.0 if not self.trade_history else sum(1 for t in self.trade_history if t["profit"] > 0) / len(self.trade_history)

def export_dashboard(df, signal, trader):
    latest = df.iloc[-1]
    snapshot = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "price": float(latest["price"]),
        "rsi": float(latest["rsi"]),
        "signal": signal,
        "balance": float(trader.balance),
        "success_ratio": trader.stats(),
        "position": trader.position or "NONE",
        "entry_price": float(trader.entry_price) if trader.entry_price else None
    }
    (DATA_DIR / "latest_snapshot.json").write_text(json.dumps(snapshot, indent=2))
    (DATA_DIR / "market_data.json").write_text(json.dumps({"series": [{"timestamp": r.isoformat(), "price": float(p)} for r, p in zip(df["timestamp"][-50:], df["price"][-50:])]}))
    (DATA_DIR / "trades.json").write_text(json.dumps(trader.trade_history, indent=2))
    (DATA_DIR / "log_archive.json").write_text(json.dumps({"lines": ["Dashboard data updated"]}, indent=2))

# Run bot
strategy = RSIStrategy()
trader = PaperTrader()
df = get_xrp_data()
df = strategy.calculate_rsi(df)
signal = strategy.generate_signal(df)
if signal == "BUY": trader.buy(df.iloc[-1]["price"])
elif signal == "SELL": trader.sell(df.iloc[-1]["price"])
export_dashboard(df, signal, trader)
print("Dashboard data exported!")
