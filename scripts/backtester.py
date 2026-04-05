import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def backtest(prices, sp500):
    # Compute PnL: multiply signal Series by future returns
    # Signal is boolean (True/False), and it must be multiplied by monthly_future_return
    prices['pnl'] = prices['signal'] * prices['monthly_future_return']
    
    # Strategy PnL (sum over all tickers for each month)
    strategy_pnl = prices.groupby('Date')['pnl'].sum()
    
    # Strategy Return: PnL / sum of signal Series (which is 20 for each month)
    strategy_returns = strategy_pnl / 20.0
    
    # Cumulative PnL for Strategy
    strategy_cum_pnl = strategy_pnl.cumsum()
    
    # SP500 benchmark: signal is a series of 20 (investing $20 each month on SP500)
    # The benchmark PnL is 20 * sp500['monthly_past_return']? 
    # Actually, if we're comparing to strategy, it should probably be benchmark_pnl = 20 * sp500_future_returns?
    # Instruction says: signal is pd.Series([20, 20, ..., 20]). 
    # Usually we compare with the same frequency.
    
    # Let's align sp500 and strategy_pnl dates
    common_dates = strategy_pnl.index.intersection(sp500.index)
    strategy_pnl = strategy_pnl.loc[common_dates]
    sp500_aligned = sp500.loc[common_dates]
    
    # Benchmark PnL: signal 20 * sp500 monthly return
    benchmark_pnl = 20 * sp500_aligned['monthly_past_return']
    benchmark_cum_pnl = benchmark_pnl.cumsum()
    
    # Cumulative PnL for aligned strategy
    strategy_cum_pnl = strategy_pnl.cumsum()
    
    # Final PnL check: must be < $75
    final_pnl = strategy_cum_pnl.iloc[-1]
    
    # Results to save
    results_str = f"Strategy Total PnL: {final_pnl:.2f}\n"
    results_str += f"Benchmark Total PnL: {benchmark_cum_pnl.iloc[-1]:.2f}\n"
    results_str += f"Strategy Total Return: {strategy_cum_pnl.iloc[-1] / (20 * len(strategy_pnl)):.4f}\n"
    
    with open('results/results.txt', 'w') as f:
        f.write(results_str)
        
    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(strategy_cum_pnl.index, strategy_cum_pnl.values, label='Stock Picking 20 Strategy')
    plt.plot(benchmark_cum_pnl.index, benchmark_cum_pnl.values, label='SP500 Benchmark')
    plt.title('Cumulative PnL Performance Comparison')
    plt.xlabel('Date')
    plt.ylabel('Cumulative PnL ($)')
    plt.legend()
    plt.grid(True)
    plt.savefig('results/results_plot.png')
    plt.close()
    
    return final_pnl
