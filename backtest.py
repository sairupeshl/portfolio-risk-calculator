# Import the required libraries
import pandas as pd
import numpy as np

# Import the data
data = pd.read_csv("portfolio_risk_vectors.csv", index_col="Date", parse_dates=True)
daily_returns = data['Portfolio_Daily_Return']
portfolio_vol = data['Current_Volatility_Baseline'].iloc[0]

# Define portfolio value and confidence level
portfolio_val = 1000000
confidence = 0.95

# Z-score for 95% confidence, from normal distribution
z_score = 1.645

# Calculate the variance percentage and value at the bottom 5%
var_pc = portfolio_vol * z_score
var_rs = portfolio_val * var_pc

# Calculate breaches and compare
breaches = daily_returns[daily_returns < -var_pc]
total_days = len(daily_returns)
total_breaches = len(breaches)
breach_pc = (total_breaches / total_days) * 100
expected_breaches = total_days * (1 - confidence)
