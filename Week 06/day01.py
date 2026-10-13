import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

df = pd.read_csv (r"C:\Users\shubi\Desktop\AI\students_week5.csv")
x = df.drop(columns= ['student_id', 'final_score', 'result', 'performance'])
y = df ['result']
x_train, x_test, y_train, y_test = train_test_split(
     x, y, test_size=0.2, random_state=42, shuffle=True
)

for depth in [3 , None]:
    tree=  DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(x_train, y_train)
    print(f"max_depth={depth}: train = {tree.score(x_train, y_train):.3f}")
    print(f"test = {tree.score(x_test, y_test):.3f}")
    
small = DecisionTreeClassifier(max_depth=2, random_state=42,).fit(x_train, y_train)
print (export_text(small, feature_names=list(x.columns)))


######### RandomForest

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import cl

df = pd.read_csv (r"C:\Users\shubi\Desktop\AI\students_week5.csv")
x = df.drop(columns= ['student_id', 'final_score', 'result', 'performance'])
y = df ['result']
x_train, x_test, y_train, y_test = train_test_split(
     x, y, test_size=0.2, random_state=42, stratify=y
)

forest = RandomforestClassifier(n_estimarors= 200, random_state= 42)
forest.fit(x_train, y_train)
print("Random Forest Test Accuracy:", round(forest.sxore(x_test, y_test), 3))

importance = pd.Series(forest.feature_Importances_, index=columns)