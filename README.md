# Stock Portfolio Tracker

This Python-based Stock Portfolio Tracker is designed to help users manage and monitor their stock holdings. The tracker allows users to add or remove stocks from their portfolio, fetch current stock prices, and calculate the portfolio's total value using real-time data from the Alpha Vantage API.

## Project Overview

The Stock Portfolio Tracker provides essential portfolio management functionalities, including:
- **Real-Time Price Retrieval**: The tracker integrates with the Alpha Vantage API to get up-to-date stock prices for each symbol in the portfolio.
- **Portfolio Management**: Users can add stocks to their portfolio with specified quantities and remove stocks as needed, with the portfolio automatically adjusting accordingly.
- **Total Portfolio Value Calculation**: The tracker computes the overall portfolio value based on the latest stock prices, providing an up-to-date view of investment value.

### Key Features

- **API Integration**: Retrieves live stock prices from Alpha Vantage, updating the portfolio value each time it is checked.
- **Error Handling**: Handles errors such as unavailable stock data or invalid removal attempts with informative messages.
- **Summary Report**: Calculates and displays individual stock values and the total portfolio value based on current prices.

## Project Structure

The main components of the Stock Portfolio Tracker include:

- **`add_stock(symbol, quantity)`**: Adds a specified quantity of a stock to the portfolio.
- **`remove_stock(symbol, quantity)`**: Removes a specified quantity of a stock from the portfolio or all shares if the quantity matches exactly.
- **`get_stock_price(symbol)`**: Fetches the latest stock price for a symbol using the Alpha Vantage API.
- **`track_portfolio()`**: Displays a summary of each stock’s value and the total portfolio value.

## Requirements

- Alpha Vantage API Key


---

The Stock Portfolio Tracker provides a straightforward solution for monitoring investment portfolios in real time, with API-based price tracking and portfolio management functionalities.
