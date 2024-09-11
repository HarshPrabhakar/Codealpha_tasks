import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker} to your portfolio.")

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if shares >= self.portfolio[ticker]:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker} from your portfolio.")
            else:
                self.portfolio[ticker] -= shares
                print(f"Removed {shares} shares of {ticker} from your portfolio.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def get_portfolio_value(self):
        total_value = 0
        for ticker, shares in self.portfolio.items():
            stock = yf.Ticker(ticker)
            price = stock.history(period="1d")['Close'][0]
            value = price * shares
            total_value += value
            print(f"{ticker}: {shares} shares @ ${price:.2f} = ${value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

    def track_performance(self):
        print("Tracking portfolio performance:")
        for ticker in self.portfolio:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            current_price = hist['Close'][0]
            previous_close = hist['Close'][1] if len(hist) > 1 else current_price
            change = ((current_price - previous_close) / previous_close) * 100
            print(f"{ticker}: Current Price = ${current_price:.2f}, Change = {change:.2f}%")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nOptions: 1. Add Stock 2. Remove Stock 3. View Portfolio Value 4. Track Performance 5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter the stock ticker (e.g., AAPL, TSLA): ").upper()
            shares = int(input(f"Enter the number of shares of {ticker} to add: "))
            portfolio.add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the stock ticker to remove: ").upper()
            shares = int(input(f"Enter the number of shares of {ticker} to remove: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == '3':
            portfolio.get_portfolio_value()
        elif choice == '4':
            portfolio.track_performance()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
