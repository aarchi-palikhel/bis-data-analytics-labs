import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Step 1: Load CSV file
df = pd.read_csv('Lab_2_Data.csv')

# Step 2: Preprocessing
# Drop rows with missing Profit and Transactions separately
profit_train = df.dropna(subset=['Profit'])
trans_train = df.dropna(subset=['Transactions'])
# Step 3: Train Linear Regression Models
profit_model = LinearRegression()
trans_model = LinearRegression()

# Train Profit model
X_profit = profit_train[['Sales']]
y_profit = profit_train['Profit']
profit_model.fit(X_profit, y_profit)

# Train Transactions model
X_trans = trans_train[['Sales']]
y_trans = trans_train['Transactions']
trans_model.fit(X_trans, y_trans)

# (Optional) Print R² scores
print("Profit model R² score:", r2_score(y_profit, profit_model.predict(X_profit)))
print("Transactions model R² score:", r2_score(y_trans, trans_model.predict(X_trans)))

# Step 4: Predict missing values using vectorized logic
missing_profit = df['Profit'].isna()
missing_trans = df['Transactions'].isna()

df.loc[missing_profit, 'Predicted_Profit'] = profit_model.predict(df.loc[missing_profit, ['Sales']])
df.loc[~missing_profit, 'Predicted_Profit'] = df.loc[~missing_profit, 'Profit']

df.loc[missing_trans, 'Predicted_Transactions'] = trans_model.predict(df.loc[missing_trans, ['Sales']])
df.loc[~missing_trans, 'Predicted_Transactions'] = df.loc[~missing_trans, 'Transactions']

# Step 5: Visualization
plt.figure(figsize=(12, 5))

# Sort for smooth regression lines
df_sorted = df.sort_values('Sales')
x_sorted = pd.DataFrame({'Sales': df_sorted['Sales']})

# Sales vs Profit
plt.subplot(1, 2, 1)
plt.scatter(df['Sales'], df['Profit'], label='Actual Profit', color='blue', alpha=0.6)
plt.scatter(df['Sales'], df['Predicted_Profit'], label='Predicted Profit', color='red', alpha=0.6)
plt.plot(x_sorted['Sales'], profit_model.predict(x_sorted), color='black', linestyle='-', label='Regression Line')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Sales vs Profit')
plt.legend()

# Sales vs Transactions
plt.subplot(1, 2, 2)
plt.scatter(df['Sales'], df['Transactions'], label='Actual Transactions', color='green', alpha=0.6)
plt.scatter(df['Sales'], df['Predicted_Transactions'], label='Predicted Transactions', color='orange', alpha=0.6)
plt.plot(x_sorted['Sales'], trans_model.predict(x_sorted), color='black', linestyle='-', label='Regression Line')
plt.xlabel('Sales')
plt.ylabel('Transactions')
plt.title('Sales vs Transactions')
plt.legend()

plt.tight_layout()
plt.savefig('lab2_predictions.png')
plt.show()

# Step 6: Save results
df.to_excel('Lab_2_Predicted_Output.xlsx', index=False)
