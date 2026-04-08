import pandas as pd
import ta

class RSIStrategy:
    def __init__(self, period=14):
        self.period = period
        self.trades = []

    def calculate_rsi(self, df):
        df["rsi"] = ta.momentum.RSIIndicator(
            close=df["price"], window=self.period
        ).rsi()
        return df

    def generate_signal(self, df):
        latest = df.iloc[-1]

        if latest["rsi"] < 30:
            return "BUY"
        elif latest["rsi"] > 70:
            return "SELL"
        else:
            return "HOLD"

    def log_trade(self, entry_price, exit_price):
        profit = exit_price - entry_price
        success = 1 if profit > 0 else 0

        self.trades.append(success)

    def success_ratio(self):
        if len(self.trades) == 0:
            return 0
        return sum(self.trades) / len(self.trades)
