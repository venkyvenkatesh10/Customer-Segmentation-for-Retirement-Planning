import pandas as pd
import random
import uuid

# Define the number of customers
num_customers = 1000

# Generate Customer IDs
customer_ids = [str(uuid.uuid4()) for _ in range(num_customers)]

# Generate random retirement goals data
target_retirement_age = [random.randint(60, 70) for _ in range(num_customers)]
expected_retirement_expenses = [round(random.uniform(20000, 100000), 2) for _ in range(num_customers)]
current_savings = [round(random.uniform(10000, 200000), 2) for _ in range(num_customers)]
required_savings = [current_savings[i] + random.uniform(50000, 300000) for i in range(num_customers)]

# Create a DataFrame
retirement_goals_df = pd.DataFrame({
    'CustomerID': customer_ids,
    'TargetRetirementAge': target_retirement_age,
    'ExpectedRetirementExpenses': expected_retirement_expenses,
    'CurrentSavings': current_savings,
    'RequiredSavings': required_savings
})

# Save to CSV
retirement_goals_df.to_csv('retirement_goals.csv', index=False)
print("Retirement goals data generated and saved.")
