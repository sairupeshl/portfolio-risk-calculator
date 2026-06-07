# Import the reqd libraries
import pandas as pd
import numpy as np

# Read the returns from the csv file
returns = pd.read_csv("portfolio_returns.csv", index_col="Date", parse_dates=True)

weights = np.array([0.25, 0.15, 0.20, 0.15, 0.25])

# Calculate the Covariance Matrix
cov_mat = returns.cov()

# Calculate portfolio variance
portfolio_var = weights.T @ cov_mat @ weights

# Calculate the Standard Deviation (Volatility)
portfolio_vol = np.sqrt(portfolio_var)

# Calculate daily portfolio return by weighted average
returns['Portfolio_Daily_Return'] = returns.dot(weights)

# Save the data to a new file
summary_data = pd.DataFrame({
    'Portfolio_Daily_Return': returns['Portfolio_Daily_Return']
})
summary_data['Current_Volatility_Baseline'] = portfolio_vol
summary_data.to_csv("portfolio_risk_vectors.csv")
