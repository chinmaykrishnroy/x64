class StockMarketTradingSystem:
    def __init__(self):
        # Initialize portfolio as an empty dictionary to store stock symbols and quantities
        self.portfolio = {}

    def buy_stock(self, symbol, quantity):
        # Method to buy stock
        # Simulated logic for buying a stock
        if symbol in self.portfolio:
            # If the stock is already in the portfolio, increase the quantity
            self.portfolio[symbol] += quantity
        else:
            # If the stock is not in the portfolio, add it with the specified quantity
            self.portfolio[symbol] = quantity
        # Print confirmation message
        print(f"Bought {quantity} shares of {symbol}")

    def sell_stock(self, symbol, quantity):
        # Method to sell stock
        # Simulated logic for selling a stock
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            # If the stock exists in the portfolio and there are enough shares to sell
            self.portfolio[symbol] -= quantity
            # Deduct sold quantity from the portfolio
            print(f"Sold {quantity} shares of {symbol}")
            if self.portfolio[symbol] == 0:
                # If all shares of the stock are sold, remove it from the portfolio
                del self.portfolio[symbol]
        else:
            # If there are not enough shares to sell
            print("Not enough shares to sell.")

    def show_portfolio(self):
        # Method to display portfolio
        print("Portfolio:")
        for symbol, quantity in self.portfolio.items():
            # Print each stock symbol and its corresponding quantity in the portfolio
            print(f"{symbol}: {quantity} shares")


# Example usage
if __name__ == "__main__":
    # Create an instance of the StockMarketTradingSystem class
    trading_system = StockMarketTradingSystem()
    # Buy stocks
    trading_system.buy_stock("AAPL", 10)
    trading_system.buy_stock("MSFT", 5)
    # Sell stocks
    trading_system.sell_stock("AAPL", 3)
    trading_system.sell_stock("GOOG", 2)  # Not enough shares to sell
    # Show portfolio
    trading_system.show_portfolio()