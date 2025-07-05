# Customer Churn Prediction Model

## 📊 Project Overview

This project implements a comprehensive customer churn prediction model for subscription-based businesses using machine learning techniques. The model analyzes customer behavior patterns to identify those at risk of churning and provides actionable business recommendations to reduce customer attrition.

## 🎯 Business Objective

Build a predictive model that identifies customers likely to stop using a subscription-based service, providing insights into why customers churn and recommending strategies to reduce churn rates.

## 📈 Key Results

- **Model Accuracy:** 79% (Logistic Regression)
- **ROC-AUC Score:** 83.2% (Excellent predictive power)
- **Current Churn Rate:** 26.5%
- **Potential Revenue Impact:** $1.45M annual loss from churn
- **Expected Churn Reduction:** 15-35% with recommended strategies

## 🏗️ Project Structure

```
Customer-Churn-Analysis/
├── WA_Fn-UseC_-Telco-Customer-Churn.csv    # Original dataset
├── eda_churn.py                            # Exploratory Data Analysis
├── model_building.py                       # Machine Learning Models
├── feature_insights.py                     # Feature Importance Analysis
├── dashboard_visualization.py              # Dashboard Generation
├── business_recommendations.py             # Business Recommendations
├── customer_churn_dashboard.png            # Generated Dashboard
├── churn_distribution.png                  # Churn Distribution Plot
├── tenure_distribution.png                 # Tenure Distribution Plot
├── monthlycharges_distribution.png         # Monthly Charges Distribution
├── boxplot_monthlycharges_churn.png        # Box Plot Analysis
├── boxplot_tenure_churn.png                # Tenure Box Plot
├── correlation_matrix.png                  # Correlation Matrix
└── README.md                               # Project Documentation
```

## 🔍 Dataset Information

**IBM Telco Customer Churn Dataset**
- **Source:** Kaggle
- **Records:** 7,043 customers
- **Features:** 21 variables including:
  - Demographics (gender, age, partner status)
  - Service information (internet type, contract type)
  - Billing information (monthly charges, payment method)
  - Usage patterns (tenure, services used)

## 🛠️ Methodology

### Step 1: Data Preparation
- Handle missing values in TotalCharges
- Convert categorical variables to numerical using One-Hot Encoding
- Remove customer ID (not useful for modeling)
- Normalize numerical features

### Step 2: Exploratory Data Analysis (EDA)
- Analyze churn distribution and rates
- Examine relationships between features and churn
- Create visualizations for key insights
- Identify patterns in customer behavior

### Step 3: Model Building
- **Logistic Regression:** Baseline model for interpretability
- **Random Forest:** Advanced model for better performance
- Train-test split (80-20)
- Cross-validation for robust evaluation

### Step 4: Feature Importance Analysis
- Identify top churn predictors
- Analyze feature importance scores
- Generate business insights

### Step 5: Dashboard Creation
- Comprehensive visualization dashboard
- 12 key charts showing different aspects of churn
- Executive-level insights and metrics

### Step 6: Business Recommendations
- Actionable strategies to reduce churn
- Financial impact projections
- Implementation roadmap

## 📊 Key Findings

### Top Churn Predictors:
1. **Contract Type** (42.7% churn for month-to-month vs 2.8% for 2-year)
2. **Tenure** (New customers <6 months at highest risk)
3. **Monthly Charges** (Higher charges correlate with increased churn)
4. **Internet Service** (Fiber optic customers churn 2.2x more than DSL)
5. **Payment Method** (Electronic check customers have highest churn)

### Critical Insights:
- Month-to-month customers churn **15x more** than 2-year contract customers
- New customers (<6 months) are at **highest risk** of churning
- **Fiber optic service** has significantly higher churn than DSL
- **Auto-pay customers** have the lowest churn rates

## 🚀 Business Recommendations

### Immediate Actions (0-3 months):
1. **Contract Incentives:** Offer 15-25% discounts for longer contracts
2. **New Customer Program:** 30-day onboarding support and free tech support
3. **Service Improvement:** Enhanced support for fiber optic customers
4. **Payment Optimization:** $5/month discount for auto-pay enrollment

### Medium-term Strategies (3-12 months):
1. **Pricing Review:** Optimize pricing for high-charge customers
2. **Service Quality:** Invest in infrastructure and support capabilities
3. **Customer Segmentation:** Develop targeted retention campaigns

## 💰 Financial Impact

- **Current Annual Revenue Loss:** $1,450,450.79
- **Potential Savings:**
  - 15% churn reduction: $217,567.62 saved annually
  - 25% churn reduction: $362,612.70 saved annually
  - 35% churn reduction: $507,657.78 saved annually

## 🛠️ Installation & Usage

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Running the Analysis

1. **Data Preparation:**
   ```bash
   python -c "import pandas as pd; df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv'); df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce'); df.dropna(inplace=True); print('Data cleaned successfully!')"
   ```

2. **Exploratory Data Analysis:**
   ```bash
   python eda_churn.py
   ```

3. **Model Building:**
   ```bash
   python model_building.py
   ```

4. **Feature Insights:**
   ```bash
   python feature_insights.py
   ```

5. **Dashboard Generation:**
   ```bash
   python dashboard_visualization.py
   ```

6. **Business Recommendations:**
   ```bash
   python business_recommendations.py
   ```

## 📈 Model Performance

| Model | Accuracy | ROC-AUC | Precision | Recall | F1-Score |
|-------|----------|---------|-----------|--------|----------|
| Logistic Regression | 79% | 83.2% | 0.62 | 0.52 | 0.57 |
| Random Forest | 79% | 81.6% | 0.63 | 0.48 | 0.54 |

## 🎯 Success Metrics

- Reduce overall churn rate from 26.5% to <20%
- Increase 2-year contract adoption by 40%
- Reduce new customer churn by 25%
- Improve customer satisfaction scores by 15%
- Achieve 85% auto-pay enrollment rate

## 📊 Visualizations Generated

The project creates several key visualizations:
- Overall churn distribution (pie chart)
- Churn rates by contract type, tenure, payment method
- Box plots for monthly charges and tenure analysis
- Correlation matrix for feature relationships
- Comprehensive dashboard with 12 charts

## 🔧 Technical Details

### Technologies Used:
- **Python 3.10+**
- **Pandas:** Data manipulation and analysis
- **NumPy:** Numerical computations
- **Matplotlib/Seaborn:** Data visualization
- **Scikit-learn:** Machine learning models
- **Jupyter Notebook:** Interactive analysis (optional)

### Model Features:
- **Feature Engineering:** One-hot encoding, data cleaning
- **Model Selection:** Logistic Regression vs Random Forest
- **Evaluation Metrics:** Accuracy, ROC-AUC, Precision, Recall, F1-Score
- **Feature Importance:** Random Forest feature ranking

## 📝 Project Deliverables

1. **Predictive Model:** 79% accurate churn prediction
2. **Business Dashboard:** 12 comprehensive visualizations
3. **Actionable Insights:** 5 key risk factors identified
4. **Strategic Recommendations:** Implementation roadmap
5. **Financial Analysis:** $1.45M impact assessment

## 🤝 Contributing

This project is designed for educational and business analysis purposes. Feel free to:
- Fork the repository
- Submit issues and enhancement requests
- Contribute additional analysis or visualizations

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Kaushal** - Data Analyst & Machine Learning Enthusiast

## 📞 Contact

- **GitHub:** [@Kaushal20025](https://github.com/Kaushal20025)
- **Project Link:** [Customer Churn Prediction Model](https://github.com/Kaushal20025/Customer-Churn-Prediction-Model)

---

**Note:** This project demonstrates end-to-end data science workflow from data cleaning to business recommendations, making it ideal for portfolio projects and real-world applications in customer analytics.
