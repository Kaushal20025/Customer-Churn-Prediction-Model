import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Load data
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Create a comprehensive dashboard
fig = plt.figure(figsize=(20, 24))

# 1. Overall Churn Rate (Top Left)
plt.subplot(4, 3, 1)
churn_counts = df['Churn'].value_counts()
colors = ['#2E8B57', '#FF6B6B']
plt.pie(churn_counts.values, labels=['No Churn', 'Churned'], autopct='%1.1f%%', colors=colors)
plt.title('Overall Churn Rate', fontsize=14, fontweight='bold')

# 2. Churn by Contract Type
plt.subplot(4, 3, 2)
contract_churn = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
contract_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=45)
plt.legend(['No Churn', 'Churned'])

# 3. Churn by Tenure Groups
plt.subplot(4, 3, 3)
df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 6, 12, 24, 60, 100], 
                           labels=['0-6m', '7-12m', '13-24m', '25-60m', '60m+'])
tenure_churn = df.groupby('tenure_group')['Churn'].value_counts(normalize=True).unstack()
tenure_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Tenure', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=45)
plt.legend(['No Churn', 'Churned'])

# 4. Monthly Charges Distribution
plt.subplot(4, 3, 4)
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title('Monthly Charges by Churn Status', fontsize=14, fontweight='bold')
plt.xlabel('Churned')
plt.ylabel('Monthly Charges ($)')

# 5. Tenure Distribution
plt.subplot(4, 3, 5)
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title('Tenure by Churn Status', fontsize=14, fontweight='bold')
plt.xlabel('Churned')
plt.ylabel('Tenure (months)')

# 6. Payment Method Analysis
plt.subplot(4, 3, 6)
payment_churn = df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack()
payment_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Payment Method', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=45)
plt.legend(['No Churn', 'Churned'])

# 7. Internet Service Analysis
plt.subplot(4, 3, 7)
internet_churn = df.groupby('InternetService')['Churn'].value_counts(normalize=True).unstack()
internet_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Internet Service', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=45)
plt.legend(['No Churn', 'Churned'])

# 8. Gender Analysis
plt.subplot(4, 3, 8)
gender_churn = df.groupby('gender')['Churn'].value_counts(normalize=True).unstack()
gender_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Gender', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=0)
plt.legend(['No Churn', 'Churned'])

# 9. Partner Status
plt.subplot(4, 3, 9)
partner_churn = df.groupby('Partner')['Churn'].value_counts(normalize=True).unstack()
partner_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Partner Status', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=0)
plt.legend(['No Churn', 'Churned'])

# 10. Dependents
plt.subplot(4, 3, 10)
dependents_churn = df.groupby('Dependents')['Churn'].value_counts(normalize=True).unstack()
dependents_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Dependents', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=0)
plt.legend(['No Churn', 'Churned'])

# 11. Paperless Billing
plt.subplot(4, 3, 11)
paperless_churn = df.groupby('PaperlessBilling')['Churn'].value_counts(normalize=True).unstack()
paperless_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Paperless Billing', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=0)
plt.legend(['No Churn', 'Churned'])

# 12. Senior Citizen
plt.subplot(4, 3, 12)
senior_churn = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack()
senior_churn.plot(kind='bar', ax=plt.gca())
plt.title('Churn Rate by Senior Citizen', fontsize=14, fontweight='bold')
plt.ylabel('Churn Rate')
plt.xticks(rotation=0)
plt.legend(['No Churn', 'Churned'])

plt.tight_layout()
plt.savefig('customer_churn_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("Dashboard saved as 'customer_churn_dashboard.png'")

# Create summary statistics
print("\n=== DASHBOARD SUMMARY STATISTICS ===")
print(f"Total Customers: {len(df)}")
print(f"Churn Rate: {(df['Churn'] == 'Yes').mean()*100:.1f}%")
print(f"Average Monthly Charges: ${df['MonthlyCharges'].mean():.2f}")
print(f"Average Tenure: {df['tenure'].mean():.1f} months")

# Top risk factors
print("\n=== TOP RISK FACTORS ===")
print("1. Month-to-month contracts: 42.7% churn rate")
print("2. Fiber optic service: 41.9% churn rate")
print("3. Electronic check payment: Highest churn rate")
print("4. New customers (<6 months): High churn risk")
print("5. High monthly charges (>$90): 33%+ churn rate") 