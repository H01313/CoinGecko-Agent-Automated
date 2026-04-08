import os
from dotenv import load_dotenv

load_dotenv()

# Trading settings
SYMBOL = "XRPUSDT"
TIMEFRAME = "5m"
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

TRADE_AMOUNT = 50  # USDT per trade

# Bybit API
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

# Mode
PAPER_TRADING = True
