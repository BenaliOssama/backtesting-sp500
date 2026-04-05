import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.memory_reducer import memory_reducer
from scripts.preprocessing import preprocessing
from scripts.create_signal import create_signal
from scripts.backtester import backtest

paths = {
    'prices': 'data/stock_prices.csv',
    'sp500': 'data/sp500.csv'
}

# import data
prices = memory_reducer(paths['prices'])
sp500 = memory_reducer(paths['sp500'])

# preprocessing
prices, sp500 = preprocessing(prices, sp500)

# create signal
prices = create_signal(prices)

# backtest
backtest(prices, sp500)
