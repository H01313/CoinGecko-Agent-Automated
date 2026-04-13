# XRP RSI Trading Bot

Autonomous trading bot using:
- CoinGecko (data)
- Bybit (execution)
- RSI strategy with success ratio tracking

## Setup

1. Clone repo
2. Install dependencies:

pip install -r requirements.txt

3. Create .env:

BYBIT_API_KEY=your_key
BYBIT_API_SECRET=your_secret

4. Run:

python main.py

## Modes

- PAPER_TRADING = True → veilig testen
- False → live trading

## Strategy

- RSI < 30 → BUY
- RSI > 70 → SELL

Tracks success ratio of trades.
