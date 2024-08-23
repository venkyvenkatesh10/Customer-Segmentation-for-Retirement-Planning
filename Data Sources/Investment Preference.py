import pandas as pd
import random
import uuid

# Define the number of customers
num_customers = 1000

# Generate Customer IDs
customer_ids = [str(uuid.uuid4()) for _ in range(num_customers)]

# Generate random investment preferences data
risk_tolerance = [random.choice(['Low', 'Medium', 'High']) for _ in range(num_customers)]
preferred_investments = [random.choice(['Stocks', 'Bonds', 'Mutual Funds', 'ETFs', 'Real Estate']) for _ in range(num_customers)]
portfolio_diversification = [round(random.uniform(0.1, 1.0), 2) for _ in range(num_customers)]  # 0.1 to 1.0 scale

# Create a DataFrame
investment_preferences_df = pd.DataFrame({
    'CustomerID': customer_ids,
    'RiskTolerance': risk_tolerance,
    'PreferredInvestment': preferred_investments,
    'PortfolioDiversification': portfolio_diversification
})

# Save to CSV
investment_preferences_df.to_csv('investment_preferences.csv', index=False)
print("Investment preferences data generated and saved.")
