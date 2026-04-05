from scripts.memory_reducer import memory_reducer
from scripts.preprocessing import preprocessing
from scripts.create_signal import create_signal
from scripts.backtester import backtest

prices, sp500 = memory_reducer('data/stock_prices.csv'), memory_reducer('data/sp500.csv')
prices, sp500 = preprocessing(prices, sp500)
prices = create_signal(prices)
backtest(prices, sp500)
