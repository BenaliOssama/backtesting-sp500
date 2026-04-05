from scripts.memory_reducer import memory_reducer
from scripts.preprocessing import preprocessing

prices = memory_reducer('data/stock_prices.csv')
sp500 = memory_reducer('data/sp500.csv')

prices, sp500 = preprocessing(prices, sp500)

print(prices.head())
print(prices.isna().sum())
print(sp500.head())
