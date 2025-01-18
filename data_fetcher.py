import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch stock data using yfinance."""
    return yf.download(ticker, start=start_date, end=end_date)
