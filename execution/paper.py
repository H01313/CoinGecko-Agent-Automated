class PaperTrader:
    def __init__(self, balance=1000):
        self.balance = balance
        self.position = None
        self.entry_price = None
        self.trade_history = []

    def buy(self, price, amount):
        if self.position is None:
            self.position = "LONG"
            self.entry_price = price
            print(f"[PAPER] BUY @ {price}")

    def sell(self, price):
        if self.position == "LONG":
            profit = price - self.entry_price
            self.balance += profit

            self.trade_history.append(profit)

            print(f"[PAPER] SELL @ {price} | Profit: {profit}")

            self.position = None
            self.entry_price = None

    def stats(self):
        wins = [p for p in self.trade_history if p > 0]
        total = len(self.trade_history)

        if total == 0:
            return 0

        return len(wins) / total
