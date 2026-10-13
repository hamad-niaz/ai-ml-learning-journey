import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

vals = np.array([[10],[20],[30],[40],[50]])
X_train, X_test = train_test_split(vals, test_size=0.2, random_state=42)

# StandardScaler - mean 0, std 1
scaler = StandardScaler()
scaler.fit(X_train) # Sirf train pe fit
print("Train Scaled:", scaler.transform(X_train).flatten())
print("Test Scaled:", scaler.transform(X_test).flatten())

# MinMaxScaler 
print(MinMaxScaler().fit_transform(vals).flatten())
# [0. 0.25 0.5 0.75 1. ]