import matplotlib.pyplot as plt

def plot_stock_trend(data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label=f'{ticker} Closing Prices')
    plt.title(f'{ticker} Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

def plot_moving_averages(data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Closing Price')
    plt.plot(data['SMA_50'], label='50-Day SMA')
    plt.plot(data['SMA_200'], label='200-Day SMA')
    plt.title(f'{ticker} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

def plot_volatility(data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Volatility'], label='20-Day Volatility', color='orange')
    plt.title(f'{ticker} Stock Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility (Standard Deviation)')
    plt.legend()
    plt.grid()
    plt.show()
