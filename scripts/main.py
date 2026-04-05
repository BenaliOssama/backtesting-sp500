import sys
import os
import pandas as pd

# Adding current directory to path to allow script imports
sys.path.append(os.getcwd())

from scripts.memory_reducer import memory_reducer
from scripts.preprocessing import preprocessing
from scripts.create_signal import create_signal
from scripts.backtester import backtest

def main():
    paths = {
        'prices': 'data/stock_prices.csv',
        'sp500': 'data/sp500.csv'
    }
    
    if not os.path.exists(paths['prices']) or not os.path.exists(paths['sp500']):
        print("Data files not found in data/ directory.")
        return

    # import data
    prices = memory_reducer(paths['prices'])
    sp500 = memory_reducer(paths['sp500'])
    
    # preprocessing
    prices, sp500 = preprocessing(prices, sp500)
    
    # create signal
    prices = create_signal(prices)
    
    # backtest
    final_pnl = backtest(prices, sp500)
    
    print(f"Backtest complete. Final Strategy PnL: {final_pnl:.2f}")

if __name__ == "__main__":
    main()
