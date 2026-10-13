import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv("emails.csv")
df = df.dropna()
# print(df.isnull().sum())
# print(df.shape)
# print(df.columns)
X = df.drop(columns=["Email No.","Prediction"])
y = df["Prediction"]
X_train ,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,stratify=y)
models = {
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(),
    "KNN" : KNeighborsClassifier(5),
    "Naive Bayes" : GaussianNB()
}

for name,m in models.items():
  pipe = make_pipeline(StandardScaler(),m)
  pipe.fit(X_train,y_train)
  y_pred = pipe.predict(X_test)
  accuracy = accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred)
  recall = recall_score(y_test, y_pred)
  f1 = f1_score(y_test, y_pred)
  print(f"\n{name}")
  print(f"Accuracy  = {accuracy:.3f}")
  print(f"Precision = {precision:.3f}")
  print(f"Recall    = {recall:.3f}")
  print(f"F1-score  = {f1:.3f}")