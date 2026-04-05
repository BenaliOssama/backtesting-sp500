# Backtesting-SP500

## Project Purpose
The goal of this project is to develop a backtesting strategy for S&P 500 stocks. It involves data preprocessing, memory optimization, signal generation based on historical returns, and evaluating the performance of a top-20 stock selection strategy against the S&P 500 benchmark.

## Project Structure
```
project
│   README.md
│   requirements.txt
│
└───data
│   │   sp500.csv
│   |   stock_prices.csv
│
└───notebook
│   │   analysis.ipynb
|
|───scripts
|   │   memory_reducer.py
|   │   preprocessing.py
|   │   create_signal.py
|   |   backtester.py
│   |   main.py
│
└───results
    │   plots
    │   results.txt
    │   outliers.txt
```

## How to Run
1. Ensure you have the datasets `sp500.csv` and `stock_prices.csv` in the `data/` directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute the main script:
   ```bash
   python3 scripts/main.py
   ```

## Implementation Summary
- **memory_reducer.py**: Optimizes the memory usage of the datasets by downcasting numeric types (minimum `float32` for precision). It ensures the optimized `prices` dataset weighs less than 8MB and the `sp500` dataset weighs less than 0.15MB.
- **preprocessing.py**: Handles data cleaning, including monthly resampling, outlier filtering (prices between $0.1 and $10,000), and calculating historical and future returns. It also handles missing values using forward fill per company.
- **create_signal.py**: Generates trading signals by identifying the top 20 companies each month based on their 1-year average return (rolling 12-month mean).
- **backtester.py**: Computes the Profit and Loss (PnL) by multiplying the signal series by future returns. It also calculates the strategy return and compares it against an S&P 500 benchmark.
- **main.py**: Orchestrates the entire workflow from data ingestion to results generation.

## Performance Conclusion
The strategy's performance was evaluated against the S&P 500 benchmark. In the backtest:
- **Strategy Total PnL**: 19.71
- **Benchmark Total PnL**: 15.18
- **Strategy Total Return**: 0.0616

The Stock Picking 20 strategy outperformed the broader S&P 500 index in terms of cumulative PnL on the provided dataset. The final PnL on full historical data is expected to be below $75 if outliers are correctly handled.
