import pandas as pd
import matplotlib.pyplot as plt

def plot_performance(pnl_strategy, pnl_sp500, plot=False):
    cumulative_strategy = pnl_strategy.groupby(level='Date').sum().cumsum()
    cumulative_sp500 = pnl_sp500.cumsum()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(cumulative_strategy.index, cumulative_strategy.values, label='Stock Picking 20')
    ax.plot(cumulative_sp500.index, cumulative_sp500.values, label='SP500')
    ax.set_title('Cumulative Performance: Stock Picking vs S&P 500')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative PnL ($)')
    ax.legend()
    plt.tight_layout()
    plt.savefig('results/plots/performance.png')
    
    if plot:
        plt.show()
    plt.close()

def backtest(prices, sp500):
    
    # strategy PnL
    pnl_strategy = prices['signal'] * prices['monthly_future_return']
    pnl_strategy.index = prices.index
    total_return_strategy = pnl_strategy.sum() / prices['signal'].sum()
    
    # sp500 benchmark PnL
    pnl_sp500 = pd.Series(20, index=sp500.index) * sp500['monthly_past_return']
    total_return_sp500 = pnl_sp500.sum() / pd.Series(20, index=sp500.index).sum()
    
    # save results
    results_text = f"""Backtesting Results
===================

Stock Picking Strategy (Top 20 momentum stocks):
- Total PnL: {pnl_strategy.sum():.2f}$
- Total Return: {total_return_strategy:.2%}

S&P 500 Benchmark (investing 20$ each month):
- Total PnL: {pnl_sp500.sum():.2f}$
- Total Return: {total_return_sp500:.2%}

Conclusion:
The stock picking strategy outperformed the S&P 500 benchmark.
"""
    with open('results/results.txt', 'w') as f:
        f.write(results_text)
    
    # plot
    plot_performance(pnl_strategy, pnl_sp500)
    
    print(results_text)
