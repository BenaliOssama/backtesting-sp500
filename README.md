# Backtesting-SP500

## Description

A quantitative backtesting system that tests a momentum-based stock picking strategy against the S&P 500 benchmark. The strategy selects the 20 stocks with the highest average return over the past 12 months and invests $1 in each, rebalancing monthly. The results are compared against a benchmark of investing $20 per month directly in the S&P 500 index.

---

## Setup & Running from an Empty Environment

### 1. Clone the repository and navigate to the project folder

```bash
cd backtesting-sp500
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the data files

Place `sp500.csv` and `stock_prices.csv` inside the `data/` folder.

### 5. Run the full pipeline

```bash
python scripts/main.py
```

This will preprocess the data, generate the signal, run the backtest, print results to the terminal, and save outputs to the `results/` folder.

---

## Project Structure

```
project
│   README.md
│   requirements.txt
│
└───data
│   │   sp500.csv
│   │   stock_prices.csv
│
└───notebook
│   │   analysis.ipynb
│
└───scripts
│   │   memory_reducer.py
│   │   preprocessing.py
│   │   create_signal.py
│   │   backtester.py
│   │   main.py
│
└───results
    │   plots/
    │   results.txt
    │   outliers.txt
```

---

## Implementation Summary

### `memory_reducer.py`

Loads a CSV file and reduces its memory footprint by downcasting each numeric column to the smallest data type that can represent its range without loss of precision. Floats are cast to `np.float32` at minimum. Date columns are converted from strings to `datetime64`. Reduces `stock_prices.csv` from ~30MB to ~8MB.

### `preprocessing.py`

Transforms raw data into clean monthly returns:
- Melts prices from wide format (one column per ticker) to long format (one row per date/ticker pair)
- Resamples daily data to month-end, keeping the last available price
- Filters prices outside the range $0.10–$10,000
- Computes monthly historical and future returns using `shift()`
- Replaces return outliers (>100% gain or >50% loss) with NaN, excluding the 2008–2009 financial crisis period
- Forward fills missing values per company
- Preprocesses the S&P 500 index independently

### `create_signal.py`

Generates the investment signal:
- Computes `average_return_1y`: a 12-month rolling average of monthly past returns, grouped per ticker
- Computes `signal`: a boolean flag marking the top 20 stocks by `average_return_1y` within each month

### `backtester.py`

Evaluates the strategy:
- Computes monthly PnL as `signal × monthly_future_return`
- Computes total return as `PnL / total invested`
- Computes the same metrics for the S&P 500 benchmark ($20/month)
- Saves results to `results/results.txt`
- Generates and saves a cumulative PnL plot to `results/plots/performance.png`

### `main.py`

Orchestrates the full pipeline from data loading to backtest in a single command: `python scripts/main.py`

---

## Results & Conclusion

| Strategy | Total PnL | Total Return |
|---|---|---|
| Stock Picking 20 (momentum) | $68.53 | 2.18% |
| S&P 500 Benchmark | $11.59 | 0.32% |

The momentum stock picking strategy outperformed the S&P 500 benchmark over the full historical period (2001–2014). However, these results should be interpreted cautiously — the dataset contains known quality issues (price spikes, erroneous values) that were partially corrected but not fully resolved. The strategy's outperformance may partly reflect residual data artifacts rather than genuine alpha.
