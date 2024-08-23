import pandas as pd
import random
import datetime
import uuid

# Define the number of customers
num_customers = 1000

# Generate Customer IDs
customer_ids = [str(uuid.uuid4()) for _ in range(num_customers)]

# Generate random transaction history data
transaction_data = []

for customer_id in customer_ids:
    num_transactions = random.randint(1, 10)
    for _ in range(num_transactions):
        transaction_date = datetime.date(2022, random.randint(1, 12), random.randint(1, 28))
        transaction_amount = round(random.uniform(500, 5000), 2)
        transaction_type = random.choice(['Deposit', 'Withdrawal'])
        transaction_data.append([customer_id, transaction_date, transaction_amount, transaction_type])

# Create a DataFrame
transaction_history_df = pd.DataFrame(transaction_data, columns=['CustomerID', 'TransactionDate', 'TransactionAmount', 'TransactionType'])

# Save to CSV
transaction_history_df.to_csv('transaction_history.csv', index=False)
print("Transaction history data generated and saved.")
