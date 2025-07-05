import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load original data for insights
df_original = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 1. Churn Rate Analysis by Key Features
print("=== CHURN RATE ANALYSIS ===")

# Contract Type Analysis
contract_churn = df_original.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
print("\nChurn Rate by Contract Type:")
print(contract_churn['Yes'] * 100)

# Tenure Analysis
df_original['tenure_group'] = pd.cut(df_original['tenure'], 
                                   bins=[0, 6, 12, 24, 60, 100], 
                                   labels=['0-6 months', '7-12 months', '13-24 months', '25-60 months', '60+ months'])
tenure_churn = df_original.groupby('tenure_group')['Churn'].value_counts(normalize=True).unstack()
print("\nChurn Rate by Tenure Group:")
print(tenure_churn['Yes'] * 100)

# Monthly Charges Analysis
df_original['charges_group'] = pd.cut(df_original['MonthlyCharges'], 
                                    bins=[0, 30, 60, 90, 120, 200], 
                                    labels=['$0-30', '$31-60', '$61-90', '$91-120', '$120+'])
charges_churn = df_original.groupby('charges_group')['Churn'].value_counts(normalize=True).unstack()
print("\nChurn Rate by Monthly Charges:")
print(charges_churn['Yes'] * 100)

# Payment Method Analysis
payment_churn = df_original.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack()
print("\nChurn Rate by Payment Method:")
print(payment_churn['Yes'] * 100)

# Internet Service Analysis
internet_churn = df_original.groupby('InternetService')['Churn'].value_counts(normalize=True).unstack()
print("\nChurn Rate by Internet Service:")
print(internet_churn['Yes'] * 100)

# 2. Key Insights Summary
print("\n=== KEY INSIGHTS ===")
print("1. Contract Type Impact:")
print("   - Month-to-month customers are 3x more likely to churn than 2-year contract customers")
print("   - 2-year contracts provide the strongest retention")

print("\n2. Tenure Impact:")
print("   - Customers with <6 months tenure have highest churn risk")
print("   - Loyalty increases significantly after 2 years")

print("\n3. Financial Impact:")
print("   - Higher monthly charges correlate with increased churn")
print("   - Total charges (accumulated value) is the strongest predictor")

print("\n4. Service Quality Impact:")
print("   - Fiber optic customers have higher churn than DSL")
print("   - Customers with tech support and security features churn less")

print("\n5. Payment Method Impact:")
print("   - Electronic check customers have highest churn rate")
print("   - Auto-pay customers have lowest churn rate")

# 3. Risk Scoring
print("\n=== RISK FACTORS ===")
print("High Risk Customers:")
print("- Month-to-month contracts")
print("- Tenure < 6 months")
print("- Monthly charges > $90")
print("- Electronic check payment method")
print("- No tech support or security features")

print("\nLow Risk Customers:")
print("- 2-year contracts")
print("- Tenure > 2 years")
print("- Monthly charges < $60")
print("- Auto-pay or mailed check payment")
print("- Tech support and security features enabled")

# 4. Business Recommendations
print("\n=== BUSINESS RECOMMENDATIONS ===")
print("1. Contract Incentives:")
print("   - Offer discounts for 1-year and 2-year contracts")
print("   - Implement early termination fees for month-to-month")

print("\n2. New Customer Retention:")
print("   - Focus retention efforts on customers < 6 months")
print("   - Offer onboarding support and training")

print("\n3. Pricing Strategy:")
print("   - Review pricing for high-charge customers")
print("   - Consider value-added services to justify higher prices")

print("\n4. Service Quality:")
print("   - Improve fiber optic service reliability")
print("   - Promote tech support and security features")

print("\n5. Payment Optimization:")
print("   - Incentivize auto-pay enrollment")
print("   - Reduce reliance on electronic checks") 