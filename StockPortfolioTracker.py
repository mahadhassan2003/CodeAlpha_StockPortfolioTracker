import requests

class StockPortfolioTracker:
    def __init__(self):
        
        self.api_key = "I3YI6NZ0EEH41DUV"
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        """Add a stock to the portfolio with a specific quantity."""
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        """Remove a specified quantity of stock from the portfolio."""
        if symbol in self.portfolio:
            if self.portfolio[symbol] > quantity:
                self.portfolio[symbol] -= quantity
                print(f"Removed {quantity} shares of {symbol} from the portfolio.")
            elif self.portfolio[symbol] == quantity:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from the portfolio.")
            else:
                print("You don't own that many shares of", symbol)
        else:
            print(f"{symbol} is not in your portfolio.")

    def get_stock_price(self, symbol):
        """Get the current stock price using the Alpha Vantage API."""
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        
     
        try:
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            closing_price = float(data["Time Series (1min)"][last_refreshed]["4. close"])
            return closing_price
        except KeyError:
            print(f"Error retrieving data for {symbol}.")
            return None

    def track_portfolio(self):
        """Track the entire portfolio and display the current value."""
        total_value = 0
        print("\nYour Portfolio:")
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                stock_value = price * quantity
                total_value += stock_value
                print(f"{symbol}: {quantity} shares @ ${price:.2f} each = ${stock_value:.2f}")
            else:
                print(f"{symbol}: Price data not available.")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

tracker = StockPortfolioTracker()


tracker.add_stock("AAPL", 10)
tracker.add_stock("MSFT", 5)
tracker.remove_stock("AAPL", 3)

tracker.track_portfolio()
