# Linear Regression on Titanic Dataset (IDLE Version)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load dataset
df = pd.read_csv("C:/Users/vasu jain/OneDrive/Downloads/Desktop/titanic dataset.csv")   # make sure file is in same folder

# Step 2: Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Convert categorical column (Sex) to numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Step 3: Select features and target
X = df[['Pclass', 'Age', 'Fare', 'Sex']]
y = df['Survived']

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("----- MODEL PERFORMANCE -----")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 8: Coefficients
print("\n----- MODEL DETAILS -----")
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.show()
