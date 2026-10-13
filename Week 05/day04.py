import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Data Load
df = pd.read_csv('students_week5.csv')

X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']  # 1 = Pass, 0 = Fail

# 2. Split 80/20 with stratify=y 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Model Train
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, pred)) # 0.865 aayega
print(confusion_matrix(y_test, pred))
# Output:
# [[66  9]  -> 66 Fail sahi, 9 Fail galat Pass bole
#  [18 107]] -> 18 Pass galat Fail bole, 107 Pass sahi
print(classification_report(y_test, pred))


y = df['performance']  # 0 = Low, 1 = Medium, 2 = High

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000) # Same code 3 classes handle kar lega
model.fit(X_train, y_train)

print('Accuracy:', accuracy_score(y_test, model.predict(X_test))) # 0.77 aayega
print(confusion_matrix(y_test, model.predict(X_test)))

# Probabilities 
print(model.predict_proba(X_test[:3]).round(2))


proba = model.predict_proba(X_test) 

df_binary = pd.read_csv('students_week5.csv')
X_b = df_binary.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y_b = df_binary['result']
# ... same split & scaler ...

probas = model.predict_proba(X_test)[:,1] 

# Threshold 0.5
pred_05 = (probas >= 0.5).astype(int)

# Threshold 0.7 
pred_07 = (probas >= 0.7).astype(int)

print("Threshold 0.5 pe Precision:", ...)
print("Threshold 0.7 pe Precision badh jayega lekin Recall kam ho jayega")
