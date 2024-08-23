import os

# Define paths
RAW_DATA_PATH = 'Data Sources'
S3_DATA_PATH = 'S3'

# Create S3 folder if it doesn't exist
os.makedirs(S3_DATA_PATH, exist_ok=True)

print(f"Folder structure set up successfully. Raw data path: '{RAW_DATA_PATH}', S3 data path: '{S3_DATA_PATH}'")
