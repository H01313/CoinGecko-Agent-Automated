from flask import Flask, request, jsonify
from execution.paper import PaperTrader
from utils.logger import log

app = Flask(__name__)

trader = PaperTrader()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    signal = data.get("signal")
    price = float(data.get("price"))

    log(f"Webhook ontvangen: {signal} @ {price}")

    if signal == "BUY":
        trader.buy(price, 1)

    elif signal == "SELL":
        trader.sell(price)

    log(f"Balance: {trader.balance}")
    log(f"Succesratio: {trader.stats()}")

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
