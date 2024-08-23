import pandas as pd
import random
import uuid

# Define the number of customers
num_customers = 1000

# Generate Customer IDs
customer_ids = [str(uuid.uuid4()) for _ in range(num_customers)]

# Generate random savings behavior data
savings_amounts = [round(random.uniform(5000, 200000), 2) for _ in range(num_customers)]
deposit_frequencies = [random.choice(['Monthly', 'Quarterly', 'Annually']) for _ in range(num_customers)]
years_saving = [random.randint(1, 40) for _ in range(num_customers)]

# Create a DataFrame
savings_behavior_df = pd.DataFrame({
    'CustomerID': customer_ids,
    'TotalSavings': savings_amounts,
    'DepositFrequency': deposit_frequencies,
    'YearsSaving': years_saving
})

# Save to CSV
savings_behavior_df.to_csv('savings_behavior.csv', index=False)
print("Savings behavior data generated and saved.")
