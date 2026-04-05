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
   pip install -r venv/requirements.txt
   ```
3. Execute the main script:
   ```bash
   python scripts/main.py
   ```

## Implementation Summary
- **memory_reducer.py**: Optimizes the memory usage of the datasets by downcasting numeric types (minimum `float32` for precision).
- **preprocessing.py**: Handles data cleaning, including monthly resampling, outlier filtering (prices between $0.1 and $10,000), and calculating historical and future returns.
- **create_signal.py**: Generates trading signals by identifying the top 20 companies each month based on their 1-year average return.
- **backtester.py**: Computes the Profit and Loss (PnL) and strategy returns, and generates cumulative PnL plots for visualization.
- **main.py**: Orchestrates the entire workflow from data ingestion to results generation.

## Performance Conclusion
*(To be updated after execution)*
The strategy evaluates whether selecting the top 20 momentum-based stocks outperforms the broader S&P 500 index.
