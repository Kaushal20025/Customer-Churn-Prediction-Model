import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load original and cleaned data
# Original for readable plots, cleaned for correlation
raw = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.drop('customerID', axis=1, inplace=True)
df = pd.get_dummies(df, drop_first=True)

# 1. Churn Rate Percentage (Target Distribution)
sns.countplot(x='Churn', data=raw)
plt.title('Churn Distribution')
plt.savefig('churn_distribution.png')
plt.close()

churn_pct = raw['Churn'].value_counts(normalize=True) * 100
print('Churn Percentage:')
print(churn_pct)

# 2. Distribution of Numerical Features
sns.histplot(raw['tenure'], kde=True)
plt.title('Distribution of Tenure')
plt.savefig('tenure_distribution.png')
plt.close()

sns.histplot(raw['MonthlyCharges'], kde=True)
plt.title('Distribution of Monthly Charges')
plt.savefig('monthlycharges_distribution.png')
plt.close()

# 3. Box Plots: Churn vs. MonthlyCharges, Tenure
sns.boxplot(x='Churn', y='MonthlyCharges', data=raw)
plt.title('Monthly Charges by Churn')
plt.savefig('boxplot_monthlycharges_churn.png')
plt.close()

sns.boxplot(x='Churn', y='tenure', data=raw)
plt.title('Tenure by Churn')
plt.savefig('boxplot_tenure_churn.png')
plt.close()

# 4. Correlation Matrix (on Cleaned Data)
plt.figure(figsize=(12,8))
corr = df.corr()
sns.heatmap(corr, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.close()

print('EDA plots saved as PNG files in the current directory.') 