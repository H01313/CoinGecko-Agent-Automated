import time
from data.coingecko import get_xrp_data
from strategy.rsi_strategy import RSIStrategy
from execution.paper import PaperTrader
from utils.logger import log

# INIT
strategy = RSIStrategy()
trader = PaperTrader()

def run_bot():
    df = get_xrp_data()
    df = strategy.calculate_rsi(df)

    latest = df.iloc[-1]
    price = latest["price"]
    rsi = latest["rsi"]

    signal = strategy.generate_signal(df)

    log(f"Prijs: {price:.4f} | RSI: {rsi:.2f} | Signaal: {signal}")

    # BUY
    if signal == "BUY":
        trader.buy(price, amount=1)

    # SELL
    elif signal == "SELL":
        trader.sell(price)

    # Stats
    success = trader.stats()
    log(f"Succesratio: {success:.2%}")
    log(f"Balance: {trader.balance:.2f} USDT")
    log("-" * 40)


# 🔥 FIX: GEEN infinite loop meer → 1 run en STOP
if __name__ == "__main__":
    try:
        run_bot()
    except Exception as e:
        log(f"FOUT: {e}")
