def calculate_moving_averages(data):
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    return data

def calculate_volatility(data):
    data['Volatility'] = data['Close'].rolling(window=20).std()
    return data
