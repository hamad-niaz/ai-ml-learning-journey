import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.DataFrame({'study_hrs':[1,2,3,4,5],
    'sleep_hrs':[8,7,6,8,7], 'marks':[50,55,65,70,85]})
print(df.corr()['marks'])
# study_hrs 0.98

# Binning - 
ages = pd.Series([5, 17, 25, 45, 68, 80])
binned = pd.cut(ages, bins=[0,12,19,59,100],
             labels=['Child','Teen','Adult','Senior'])
print(binned)



from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

#  dataset
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([10,20,30,40,50])

# scaling + model
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

pipe.fit(X, y)
print(pipe.predict([[6]])) # Output: [60.]
print("Ye Pipeline ETL ka bhi kaam karta hai - Extract, Transform, Load")