import pandas as pd
import numpy as np

def create_signal(prices):
    # Ensure data is sorted by ticker and Date
    prices = prices.sort_index(level=['ticker', 'Date'])
    
    # Create average_return_1y: average of monthly past returns over the previous year (12 consecutive rows)
    # grouped by company
    prices['average_return_1y'] = prices.groupby('ticker')['monthly_past_return'].transform(
        lambda x: x.rolling(window=12).mean()
    )
    
    # Create signal: True if average_return_1y is among the 20 highest within the same month
    # grouped by Date
    prices['signal'] = prices.groupby('Date')['average_return_1y'].transform(
        lambda x: x.rank(ascending=False, method='first') <= 20
    )
    
    return prices
