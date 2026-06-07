# Import the reqd libraries
import numpy as np
import pandas as pd
import yfinance as yf

# Stocks in the portfolio from Nifty
tickers = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ITC.NS"]

# Import last 5 years' data from yf
raw_data = yf.download(tickers, start="2021-01-01", end="2026-01-01", threads=False)

# Extract the closing prices
closing_prices = raw_data['Close']

# Calculate the percentage change in the closing prices and drop the NAN (first day)
portfolio_returns = closing_prices.pct_change().dropna()

# Store as a csv file
portfolio_returns.to_csv("portfolio_returns.csv")
