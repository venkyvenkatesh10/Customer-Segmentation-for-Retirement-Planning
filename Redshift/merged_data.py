import pandas as pd
import numpy as np

# Define the output file path
output_file_path = 'C:/Users/venka/Desktop/Customer Segmentation for Retirement Planning/generated_data.csv'

# Define the columns based on the previous CSV file structure
columns = [
    'CustomerID', 'Age', 'Gender', 'MaritalStatus', 'AnnualIncome',
    'RiskTolerance', 'PreferredInvestment', 'PortfolioDiversification',
    'SavingsGoal', 'SavingFrequency', 'CustomerLifetimeValue', 'TransactionAmount'
]

# Generate random data
np.random.seed(42)  # For reproducibility

# Example data generation for each column
data = {
    'CustomerID': np.random.randint(1000, 9999, 100),
    'Age': np.random.randint(18, 70, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'MaritalStatus': np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], 100),
    'AnnualIncome': np.random.randint(30000, 150000, 100),
    'RiskTolerance': np.random.choice(['Low', 'Medium', 'High'], 100),
    'PreferredInvestment': np.random.choice(['Bonds', 'Mutual Funds', 'Stocks', 'Real Estate'], 100),
    'PortfolioDiversification': np.random.choice(['Low', 'Medium', 'High'], 100),
    'SavingsGoal': np.random.choice(['Retirement', 'Education', 'Travel', 'Home Purchase'], 100),
    'SavingFrequency': np.random.choice(['Monthly', 'Quarterly', 'Annually'], 100),
    'CustomerLifetimeValue': np.random.randint(5000, 50000, 100),
    'TransactionAmount': np.random.randint(100, 5000, 100)
}

# Create the DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the generated data outside the Redshift directory
df.to_csv(output_file_path, index=False)

print(f"Random data generated and saved to {output_file_path}")
