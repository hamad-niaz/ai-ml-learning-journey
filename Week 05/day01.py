# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score



# df = pd.read_csv(r"C:\Users\shubi\Desktop\AI\students_week5.csv")
# x = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
# y = df['result']

# print(df.columns)
# x_train, x_test, y_train, y_test = train_test_split(
#     x, y, test_size=0.2, random_state=42, shuffle=True
# )

# raw = KNeighborsClassifier(n_neighbors=5).fit(x_train, y_train)
# print('kNN without scaling!', accuracy_score(y_test, raw.predict(x_test)))
# scaler = StandardScaler()
# x_train_5, x_test = scaler.fit_transform(x_train), scaler.transform(x_test)

# for k in [1, 3, 5, 7, 9, 15, 25]:
#     knn = KNeighborsClassifier(n_neighbors=k).fit(x_train_5, y_train)
#     acc = accuracy_score(y_test,knn.predict(x_train))
#     print(f'k=(k:>2): accuracy = {acc:.3f}')
    
    
    
    
    
    
    
    
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

from sklearn.metrics import accuracy_score


df = pd.read_csv(r"C:\Users\shubi\Desktop\AI\students_week5.csv")

x = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])

y = df['result']

print(df.columns)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, shuffle=True
)

raw = KNeighborsClassifier(n_neighbors=5).fit(x_train, y_train)

print('kNN without scaling!', accuracy_score(y_test, raw.predict(x_test)))

scaler = StandardScaler()

x_train_5, x_test = scaler.fit_transform(x_train), scaler.transform(x_test)

for k in [1, 3, 5, 7, 9, 15, 25]:

    knn = KNeighborsClassifier(n_neighbors=k).fit(x_train_5, y_train)

    acc = accuracy_score(y_test, knn.predict(x_test))

    print(f'k={k:>2}: accuracy = {acc:.3f}')