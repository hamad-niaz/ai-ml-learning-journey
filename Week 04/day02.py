import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Ordered categories
sizes = ['Small','Medium','Large','Medium']
le = LabelEncoder()
encoded = le.fit_transform(sizes)
print(encoded) # Output: [2 1 0 1]

# Unordered categories 
df = pd.DataFrame({'City': ['Lahore', 'Karachi', 'Lahore']})
one_hot = pd.get_dummies(df['City'])
print(one_hot)
# Karachi Lahore
# 0 0 1
# 1 1 0