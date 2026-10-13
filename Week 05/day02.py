import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix


# df = pd.read_csv(r"C:\Users\shubi\Desktop\AI\students_week5.csv")

# x = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])

# y = df['result']

# print(df.columns)

# x_train, x_test, y_train, y_test = train_test_split(
#     x, y, test_size=0.2, random_state=42, shuffle=True
# )

# model = GaussianNB()
# model.fit(x_train, y_train)
# pred = model.predict(x_test)
# print('Accuracy:', acuracy_score(y_test, pred))
# print(confusion_matrix(y_test, pred))

# new_student = x_test.iloc[[0]]
# print('Pass probability:', model.predict_log_proba(new_student)[0][1].round(2))























import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv("students_week5.csv")

X = df.drop(columns=["student_id", "final_score", "result", "performance"])

y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": SVC(),
    "KNN (K=5)": KNeighborsClassifier(5),
    "Naive Bayes": GaussianNB()
}
for name, m in models.items():

    pipe = make_pipeline(
        StandardScaler(),
        m
    )
    pipe.fit(X_train, y_train)

    print(f"{name:20s} accuracy = {pipe.score(X_test, y_test):.3f}")