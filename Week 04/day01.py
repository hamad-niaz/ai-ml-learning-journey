import numpy as np
import pandas as pd

# data
prices = pd.Series([100, 500, 1000, 50000])
print("Original:", prices.values)

# Transformation - shape change
log_prices = np.log(prices)
print("Log Transform ke baad:")
print(log_prices)

