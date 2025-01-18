from data_fetcher import fetch_stock_data
from plotter import plot_stock_trend, plot_moving_averages, plot_volatility
from indicators import calculate_moving_averages, calculate_volatility

def main():
    ticker = 'AAPL'
    start_date = '2023-01-01'
    end_date = '2024-12-31'
    
    # Fetch stock data
    data = fetch_stock_data(ticker, start_date, end_date)
    
    # Calculate indicators
    data = calculate_moving_averages(data)
    data = calculate_volatility(data)
    
    # Plot results
    plot_stock_trend(data, ticker)
    plot_moving_averages(data, ticker)
    plot_volatility(data, ticker)

if __name__ == '__main__':
    main()
