import os
import pandas as pd
import numpy as np

# Define paths
RAW_DATA_PATH = r'C:\Users\venka\Desktop\Customer Segmentation for Retirement Planning\Data Sources'
S3_DATA_PATH = r'C:\Users\venka\Desktop\Customer Segmentation for Retirement Planning\S3'


# Create S3 folder if it doesn't exist
os.makedirs(S3_DATA_PATH, exist_ok=True)

# Cleaning Functions as defined earlier
def clean_customer_demographics(file_path):
    df = pd.read_csv(file_path)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
    df['MaritalStatus'] = df['MaritalStatus'].fillna('Unknown')
    df['AnnualIncome'] = df['AnnualIncome'].fillna(df['AnnualIncome'].median())
    df.drop_duplicates(subset='CustomerID', inplace=True)
    df['Age'] = df['Age'].astype(int)
    df['AnnualIncome'] = df['AnnualIncome'].astype(float)
    Q1 = df['AnnualIncome'].quantile(0.25)
    Q3 = df['AnnualIncome'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df['AnnualIncome'] = np.where(df['AnnualIncome'] > upper_bound, upper_bound, df['AnnualIncome'])
    df['AnnualIncome'] = np.where(df['AnnualIncome'] < lower_bound, lower_bound, df['AnnualIncome'])
    return df

def clean_savings_behavior(file_path):
    df = pd.read_csv(file_path)
    df['TotalSavings'] = df['TotalSavings'].fillna(df['TotalSavings'].median())
    df['DepositFrequency'] = df['DepositFrequency'].fillna('Unknown')
    df['YearsSaving'] = df['YearsSaving'].fillna(df['YearsSaving'].median())
    df.drop_duplicates(subset='CustomerID', inplace=True)
    df['TotalSavings'] = df['TotalSavings'].astype(float)
    df['YearsSaving'] = df['YearsSaving'].astype(int)
    Q1 = df['TotalSavings'].quantile(0.25)
    Q3 = df['TotalSavings'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df['TotalSavings'] = np.where(df['TotalSavings'] > upper_bound, upper_bound, df['TotalSavings'])
    df['TotalSavings'] = np.where(df['TotalSavings'] < lower_bound, lower_bound, df['TotalSavings'])
    return df

def clean_investment_preferences(file_path):
    df = pd.read_csv(file_path)
    df['RiskTolerance'] = df['RiskTolerance'].fillna(df['RiskTolerance'].mode()[0])
    df['PreferredInvestment'] = df['PreferredInvestment'].fillna(df['PreferredInvestment'].mode()[0])
    df['PortfolioDiversification'] = df['PortfolioDiversification'].fillna(df['PortfolioDiversification'].mean())
    df.drop_duplicates(subset='CustomerID', inplace=True)
    df['PortfolioDiversification'] = df['PortfolioDiversification'].astype(float)
    df['PortfolioDiversification'] = df['PortfolioDiversification'].clip(0, 1)
    return df

def clean_retirement_goals(file_path):
    df = pd.read_csv(file_path)
    df['TargetRetirementAge'] = df['TargetRetirementAge'].fillna(df['TargetRetirementAge'].median())
    df['ExpectedRetirementExpenses'] = df['ExpectedRetirementExpenses'].fillna(df['ExpectedRetirementExpenses'].median())
    df['CurrentSavings'] = df['CurrentSavings'].fillna(df['CurrentSavings'].median())
    df['RequiredSavings'] = df['RequiredSavings'].fillna(df['RequiredSavings'].median())
    df.drop_duplicates(subset='CustomerID', inplace=True)
    df['TargetRetirementAge'] = df['TargetRetirementAge'].astype(int)
    df[['ExpectedRetirementExpenses', 'CurrentSavings', 'RequiredSavings']] = df[['ExpectedRetirementExpenses', 'CurrentSavings', 'RequiredSavings']].astype(float)
    df['CurrentSavings'] = np.where(df['CurrentSavings'] > df['RequiredSavings'], df['RequiredSavings'], df['CurrentSavings'])
    return df

def clean_transaction_history(file_path):
    df = pd.read_csv(file_path)
    df['TransactionAmount'] = df['TransactionAmount'].fillna(df['TransactionAmount'].median())
    df['TransactionType'] = df['TransactionType'].fillna('Unknown')
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')
    df['TransactionDate'] = df['TransactionDate'].fillna(pd.Timestamp.now())
    df.drop_duplicates(subset=['CustomerID', 'TransactionDate', 'TransactionAmount', 'TransactionType'], inplace=True)
    df['TransactionAmount'] = df['TransactionAmount'].astype(float)
    Q1 = df['TransactionAmount'].quantile(0.25)
    Q3 = df['TransactionAmount'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df['TransactionAmount'] = np.where(df['TransactionAmount'] > upper_bound, upper_bound, df['TransactionAmount'])
    df['TransactionAmount'] = np.where(df['TransactionAmount'] < lower_bound, lower_bound, df['TransactionAmount'])
    return df

# Mapping of raw file names to their cleaning functions
file_cleaning_mapping = {
    'customer_demographics.csv': clean_customer_demographics,
    'savings_behavior.csv': clean_savings_behavior,
    'investment_preferences.csv': clean_investment_preferences,
    'retirement_goals.csv': clean_retirement_goals,
    'transaction_history.csv': clean_transaction_history
}

def process_and_clean_data():
    for file_name, cleaning_function in file_cleaning_mapping.items():
        raw_file_path = os.path.join(RAW_DATA_PATH, file_name)
        s3_file_path = os.path.join(S3_DATA_PATH, file_name)
        
        try:
            print(f"Processing {file_name}...")
            cleaned_df = cleaning_function(raw_file_path)
            cleaned_df.to_csv(s3_file_path, index=False)
            print(f"{file_name} cleaned and saved to {s3_file_path}\n")
        except Exception as e:
            print(f"Error processing {file_name}: {e}\n")

if __name__ == "__main__":
    process_and_clean_data()
    print("All files have been processed and cleaned successfully.")
