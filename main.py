import yfinance as yf
import numpy as np
from matplotlib import pyplot as plt

import matplotlib

data = yf.Ticker('MSFT')
hist = data.history(period='1mo').iloc[1:20]

# plt.plot(range(1, 20), data.history(period='1mo')['Close'].iloc[1:20])
# plt.show()

print(hist.index.date)
def return_data():
    



