import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'C:\\Users\\venka\\Desktop\\Customer Segmentation for Retirement Planning\\merged_raw_data.csv'
df = pd.read_csv(file_path)

# List all columns to check their names
print(df.columns)

# Set up the matplotlib figure
plt.figure(figsize=(20, 25))

# 4. Savings Behavior
# 1. Savings Goal Distribution: Histogram to see what customers are saving for.
plt.subplot(4, 2, 1)
sns.histplot(df['SavingsGoal'], kde=True, bins=20, color='green')
plt.title('Savings Goal Distribution')
plt.xlabel('Savings Goal')
plt.ylabel('Frequency')

# 2. Saving Frequency: Bar chart to determine how often customers save.
plt.subplot(4, 2, 2)
sns.countplot(x='SavingFrequency', hue='SavingFrequency', data=df, palette='Blues', legend=False)
plt.title('Saving Frequency')
plt.xlabel('Saving Frequency')
plt.ylabel('Count')

# 3. Saving Instruments Usage: Stacked bar chart to explore the types of saving instruments customers use.
plt.subplot(4, 2, 3)
saving_instruments = df['SavingInstruments'].str.get_dummies(', ')
saving_instruments.sum().plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.title('Saving Instruments Usage')
plt.xlabel('Saving Instrument')
plt.ylabel('Count')

# 5. Transaction Behavior
# 1. Transaction Type Distribution: Pie chart to see the split between credit and debit transactions.
plt.subplot(4, 2, 4)
transaction_types = df['TransactionType'].value_counts()
plt.pie(transaction_types, labels=transaction_types.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Transaction Type Distribution')

# 2. Transaction Amount by Date: Line chart to identify trends or anomalies in spending over time.
plt.subplot(4, 2, 5)
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
df.groupby('TransactionDate')['TransactionAmount'].sum().plot(kind='line', color='purple')
plt.title('Transaction Amount by Date')
plt.xlabel('Date')
plt.ylabel('Total Transaction Amount')

# 3. High-Value Transactions: Scatter plot to highlight significant customer transactions.
plt.subplot(4, 2, 6)
sns.scatterplot(x='TransactionAmount', y='CustomerID', data=df, hue='TransactionType', palette='coolwarm')
plt.title('High-Value Transactions')
plt.xlabel('Transaction Amount')
plt.ylabel('Customer ID')

# 6. Customer Lifetime Value (CLTV)
# Check if 'CustomerLifetimeValue' exists and handle it accordingly
if 'CustomerLifetimeValue' in df.columns:
    # 1. CLTV Distribution: Histogram to see the distribution of customer lifetime values.
    plt.subplot(4, 2, 7)
    sns.histplot(df['CustomerLifetimeValue'], kde=True, bins=20, color='orange')
    plt.title('CLTV Distribution')
    plt.xlabel('Customer Lifetime Value')
    plt.ylabel('Frequency')

    # 2. CLTV Segmentation: Box plot to show the range of values within different customer segments.
    plt.subplot(4, 2, 8)
    sns.boxplot(x='CustomerSegment', y='CustomerLifetimeValue', data=df, palette='Set2')
    plt.title('CLTV Segmentation')
    plt.xlabel('Customer Segment')
    plt.ylabel('Customer Lifetime Value')
else:
    print("Column 'CustomerLifetimeValue' not found in the dataset.")

# Adjust layout for better readability
plt.tight_layout(pad=3.0)

# Save the visualization to a file
output_image_path = 'C:\\Users\\venka\\Desktop\\Customer Segmentation for Retirement Planning\\savings_transaction_cltv_analysis.png'
plt.savefig(output_image_path)

plt.show()

print(f"Visualization saved to: {output_image_path}")

# 7. Cross-Analysis Insights
plt.figure(figsize=(20, 12))

# Insight: Identify correlations between different customer behaviors and outcomes.
# Visualization:
# 1. Risk Tolerance vs. Investment Strategy: Heatmap to explore the relationship between risk tolerance and chosen investment strategies.
plt.subplot(1, 2, 1)
heatmap_data = pd.crosstab(df['RiskTolerance'], df['InvestmentStrategy'])
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm')
plt.title('Risk Tolerance vs. Investment Strategy')
plt.xlabel('Investment Strategy')
plt.ylabel('Risk Tolerance')

# 2. Income vs. Preferred Investment Type: Mosaic plot or stacked bar chart to see how income levels influence investment choices.
plt.subplot(1, 2, 2)
income_bins = pd.cut(df['AnnualIncome'], bins=4)
investment_income_data = pd.crosstab(income_bins, df['PreferredInvestment'])
investment_income_data.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='Paired')
plt.title('Income vs. Preferred Investment Type')
plt.xlabel('Annual Income')
plt.ylabel('Count')

# Adjust layout for better readability
plt.tight_layout(pad=3.0)

# Save the visualization to a file
cross_analysis_output_image_path = 'C:\\Users\\venka\\Desktop\\Customer Segmentation for Retirement Planning\\cross_analysis_insights.png'
plt.savefig(cross_analysis_output_image_path)

plt.show()

print(f"Cross-analysis visualization saved to: {cross_analysis_output_image_path}")
