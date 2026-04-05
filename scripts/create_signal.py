import pandas as pd

def create_signal(prices):
    
    prices = prices.reset_index()
   
    # rolling windonw 12 months 
    prices['average_return_1y'] = prices.groupby('ticker')['monthly_past_return'].transform(
        lambda x: x.rolling(12).mean()
    )
    
    # sort and 20 first are true
    prices['signal'] = prices.groupby('Date')['average_return_1y'].transform(
        lambda x: x.rank(ascending=False) <= 20
    )
    
    #muli indexing
    prices = prices.set_index(['Date', 'ticker'])
    
    return prices
