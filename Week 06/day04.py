# ============================================
# LOAN APPROVAL PREDICTION USING DECISION TREE
# ============================================

# Step 1: Libraries import karna
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# ============================================
# Step 2: Dataset load karna
# ============================================

df = pd.read_csv("loan_data_set.csv")

print("Dataset successfully loaded!")
print("Dataset Shape:", df.shape)


# ============================================
# Step 3: Missing Values Handle karna
# ============================================

# Categorical columns ke missing values ko Mode se fill karna
categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])


# Numerical columns ke missing values ko Median se fill karna
numerical_columns = [
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())


# ============================================
# Step 4: Dependents ko numeric banana
# ============================================

# Dataset mein "3+" hai, isko 3 kar dete hain
df["Dependents"] = df["Dependents"].replace("3+", "3")

df["Dependents"] = df["Dependents"].astype(int)


# ============================================
# Step 5: Loan Status ko numeric banana
# ============================================

# Y = 1  (Approved)
# N = 0  (Not Approved)

df["Loan_Status"] = df["Loan_Status"].map({
    "Y": 1,
    "N": 0
})


# ============================================
# Step 6: Loan_ID remove karna
# ============================================

# Loan_ID sirf identification ke liye hai,
# prediction mein iska koi useful role nahi

df = df.drop("Loan_ID", axis=1)


# ============================================
# Step 7: Categorical data ko numeric banana
# ============================================

df = pd.get_dummies(
    df,
    columns=[
        "Gender",
        "Married",
        "Education",
        "Self_Employed",
        "Property_Area"
    ],
    drop_first=True,
    dtype=int
)


# ============================================
# Step 8: Input X aur Target y banana
# ============================================

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]


# ============================================
# Step 9: Training aur Testing Data
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ============================================
# Step 10: Decision Tree Model
# ============================================

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)


# ============================================
# Step 11: Model Train karna
# ============================================

model.fit(X_train, y_train)

print("\nModel training complete!")


# Model Test karna


y_pred = model.predict(X_test)

# Accuracy


accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

#  Classification Report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# USER SE LOAN DATA LENA


print("\n===================================")
print("     LOAN APPROVAL PREDICTION")
print("===================================")

print("\nPlease enter your information:\n")


# Gender
gender = input("Gender (Male/Female): ").strip().title()

# Married
married = input("Married (Yes/No): ").strip().title()

# Dependents
dependents = input("Number of Dependents (0/1/2/3): ").strip()

# Education
education = input("Education (Graduate/Not Graduate): ").strip().title()

# Self Employed
self_employed = input("Self Employed (Yes/No): ").strip().title()

# Applicant Income
applicant_income = float(
    input("Applicant Income: ")
)

# Coapplicant Income
coapplicant_income = float(
    input("Coapplicant Income: ")
)

# Loan Amount
loan_amount = float(
    input("Loan Amount: ")
)

# Loan Term
loan_term = float(
    input("Loan Amount Term (e.g. 360): ")
)

# Credit History
credit_history = float(
    input("Credit History (1 = Good, 0 = Bad): ")
)

# Property Area
property_area = input(
    "Property Area (Urban/Semiurban/Rural): "
).strip().title()

# User ka data DataFrame mein banana

user_data = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [int(dependents)],
    "Education": [education],
    "Self_Employed": [self_employed],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_history],
    "Property_Area": [property_area]
})

#  User data ko same format mein convert karna

user_data = pd.get_dummies(
    user_data,
    columns=[
        "Gender",
        "Married",
        "Education",
        "Self_Employed",
        "Property_Area"
    ],
    drop_first=True,
    dtype=int
)

#  Training columns ke according
# User data ko arrange karna


user_data = user_data.reindex(
    columns=X.columns,
    fill_value=0
)

#Loan Prediction

prediction = model.predict(user_data)

####Result

print("\n===================================")

if prediction[0] == 1:
    print("       LOAN APPROVED")
    print("       Congratulations!")
else:
    print("       LOAN NOT APPROVED")

print("===================================")