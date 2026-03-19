import pandas as pd

# Load full datasets
raw = pd.read_csv("data/raw/transactions_raw.csv")
clean = pd.read_csv("data/processed/transactions_clean.csv")

# Take sample
raw_sample = raw.sample(n=300, random_state=42)
clean_sample = clean.sample(n=300, random_state=42)

# Save samples
raw_sample.to_csv("data/raw/transactions_raw_sample.csv", index=False)
clean_sample.to_csv("data/processed/transactions_clean_sample.csv", index=False)