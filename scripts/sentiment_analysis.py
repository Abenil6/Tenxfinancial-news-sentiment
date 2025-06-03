import yfinance as yf
import talib
import matplotlib.pyplot as plt

# Download stock data
aapl = yf.download('AAPL', start='2024-01-01', end='2025-05-01')

# Calculate 20-day Simple Moving Average (SMA)
aapl['SMA_20'] = talib.SMA(aapl['Close'], timeperiod=20)

# Plot Close price and SMA
aapl[['Close', 'SMA_20']].plot(title="AAPL Close Price and 20-day SMA")
plt.show()
