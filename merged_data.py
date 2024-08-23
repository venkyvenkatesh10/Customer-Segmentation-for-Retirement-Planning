import pandas as pd
import numpy as np

# Define the columns
columns = [
    'CustomerID', 'Age', 'Gender', 'MaritalStatus', 'AnnualIncome',
    'RiskTolerance', 'PreferredInvestment', 'PortfolioDiversification',
    'RetirementAge', 'SavingsGoal', 'InvestmentStrategy',
    'MonthlySavings', 'SavingFrequency', 'SavingInstruments',
    'TransactionID', 'TransactionDate', 'TransactionAmount', 'TransactionType'
]

# Generate random data
num_rows = 1000  # Number of rows to generate

data = {
    'CustomerID': np.arange(1, num_rows + 1),
    'Age': np.random.randint(18, 70, num_rows),
    'Gender': np.random.choice(['Male', 'Female'], num_rows),
    'MaritalStatus': np.random.choice(['Single', 'Married', 'Divorced'], num_rows),
    'AnnualIncome': np.random.randint(30000, 150000, num_rows),
    'RiskTolerance': np.random.choice(['Low', 'Medium', 'High'], num_rows),
    'PreferredInvestment': np.random.choice(['Stocks', 'Bonds', 'Real Estate', 'Mutual Funds'], num_rows),
    'PortfolioDiversification': np.random.choice(['Low', 'Medium', 'High'], num_rows),
    'RetirementAge': np.random.randint(55, 70, num_rows),
    'SavingsGoal': np.random.randint(100000, 2000000, num_rows),
    'InvestmentStrategy': np.random.choice(['Conservative', 'Balanced', 'Aggressive'], num_rows),
    'MonthlySavings': np.random.randint(500, 5000, num_rows),
    'SavingFrequency': np.random.choice(['Monthly', 'Quarterly', 'Annually'], num_rows),
    'SavingInstruments': np.random.choice(['Bank Deposit', 'Bonds', 'Stocks', 'Real Estate'], num_rows),
    'TransactionID': np.arange(1, num_rows + 1),
    'TransactionDate': pd.date_range(start='2023-01-01', periods=num_rows, freq='D').strftime('%Y-%m-%d'),
    'TransactionAmount': np.random.uniform(50.0, 10000.0, num_rows).round(2),
    'TransactionType': np.random.choice(['Credit', 'Debit'], num_rows)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_file_path = 'C:\\Users\\venka\\Desktop\\Customer Segmentation for Retirement Planning\\merged_raw_data.csv'
df.to_csv(output_file_path, index=False)

print(f"Random data saved to: {output_file_path}")
