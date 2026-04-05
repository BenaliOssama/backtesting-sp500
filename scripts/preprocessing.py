import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_avg_price(df, plot=False):
    avg_price = df.groupby('Date')['Price'].mean()
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(avg_price.index, avg_price.values)
    ax.set_title('Average Stock Price Across S&P 500 Companies Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Average Price ($)')
    plt.tight_layout()
    plt.savefig('results/plots/avg_price.png')
    if plot:
        plt.show()
    plt.close()

def preprocessing(prices, sp500):
    
    # --- PRICES ---
    
    # wide to long
    prices = prices.melt(id_vars='Date', var_name='ticker', value_name='Price')
    
    # resample to month end
    prices = prices.set_index('Date')
    prices = prices.groupby('ticker')['Price'].resample('ME').last()
    prices = prices.reset_index()
    
    # filter price outliers
    prices = prices[(prices['Price'] >= 0.1) & (prices['Price'] <= 10000)]
    
    # sort before shift operations
    prices = prices.sort_values(['ticker', 'Date'])
    
    # compute returns
    prices['monthly_past_return'] = prices.groupby('ticker')['Price'].transform(
        lambda x: (x - x.shift(1)) / x.shift(1)
    )
    prices['monthly_future_return'] = prices.groupby('ticker')['Price'].transform(
        lambda x: (x.shift(-1) - x) / x
    )
    
    # replace return outliers with NaN (excluding 2008-2009)
    mask_not_crisis = ~prices['Date'].dt.year.isin([2008, 2009])
    mask_outlier = (prices['monthly_past_return'] > 1) | (prices['monthly_past_return'] < -0.5)
    prices.loc[mask_not_crisis & mask_outlier, 'monthly_past_return'] = np.nan
    prices.loc[mask_not_crisis & mask_outlier, 'monthly_future_return'] = np.nan
    
    # forward fill per company
    prices['monthly_past_return'] = prices.groupby('ticker')['monthly_past_return'].transform(
        lambda x: x.ffill()
    )
    prices['monthly_future_return'] = prices.groupby('ticker')['monthly_future_return'].transform(
        lambda x: x.ffill()
    )
    
    # drop unfillable rows
    prices = prices.dropna()
    
    # set MultiIndex
    prices = prices.set_index(['Date', 'ticker'])
    
    # --- SP500 ---
    
    sp500 = sp500.set_index('Date')
    sp500 = sp500['Adjusted Close'].resample('ME').last()
    sp500 = sp500.to_frame()
    sp500['monthly_past_return'] = (
        sp500['Adjusted Close'] - sp500['Adjusted Close'].shift(1)
    ) / sp500['Adjusted Close'].shift(1)
    sp500 = sp500.dropna()
    
    return prices, sp500
