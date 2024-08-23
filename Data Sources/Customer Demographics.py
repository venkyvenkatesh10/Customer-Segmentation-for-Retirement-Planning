import pandas as pd
import random
import uuid

# Generate random customer demographics data
num_customers = 1000
customer_ids = [str(uuid.uuid4()) for _ in range(num_customers)]
ages = [random.randint(25, 65) for _ in range(num_customers)]
genders = [random.choice(['Male', 'Female']) for _ in range(num_customers)]
marital_statuses = [random.choice(['Single', 'Married', 'Divorced', 'Widowed']) for _ in range(num_customers)]
incomes = [round(random.uniform(30000, 150000), 2) for _ in range(num_customers)]

# Create a DataFrame
customer_demographics_df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Age': ages,
    'Gender': genders,
    'MaritalStatus': marital_statuses,
    'AnnualIncome': incomes
})

# Save to CSV
customer_demographics_df.to_csv('customer_demographics.csv', index=False)
print("Customer demographics data generated and saved.")
