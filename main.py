import time
from data.coingecko import get_xrp_data
from strategy.rsi_strategy import RSIStrategy
from execution.bybit import place_order
from config import TRADE_AMOUNT
from utils.logger import log

strategy = RSIStrategy()

position = None
entry_price = None

while True:
    df = get_xrp_data()
    df = strategy.calculate_rsi(df)

    signal = strategy.generate_signal(df)
    price = df.iloc[-1]["price"]

    log(f"Prijs: {price} | Signaal: {signal}")

    if signal == "BUY" and position is None:
        place_order("Buy", TRADE_AMOUNT)
        position = "LONG"
        entry_price = price

    elif signal == "SELL" and position == "LONG":
        place_order("Sell", TRADE_AMOUNT)
        strategy.log_trade(entry_price, price)
        position = None

        log(f"Succesratio: {strategy.success_ratio()}")

    time.sleep(60)
