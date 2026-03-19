import pandas as pd

df = pd.read_csv("transactions.csv")

print("Total rows:", len(df))

# 1. Failure Rate
failure_rate = (df['status'] == 'FAILED').mean() * 100
print("Failure Rate (%):", round(failure_rate, 2))

# 2. NULL Failure Reasons
failed_df = df[df['status'] == 'FAILED']
null_failure_pct = failed_df['failure_reason'].isna().mean() * 100
print("Unexplained Failures (%):", round(null_failure_pct, 2))

# 3. Merchant Concentration (Top 5)
failed_gmv = failed_df.groupby('merchant_id')['amount'].sum().sort_values(ascending=False)
top5_share = failed_gmv.head(5).sum() / failed_gmv.sum() * 100
print("Top 5 Merchants Contribution to Failed GMV (%):", round(top5_share, 2))

# 4. Peak Hour Analysis
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
peak = df[df['hour'].between(19, 22)]

peak_failure_rate = (peak['status'] == 'FAILED').mean() * 100
overall_failure_rate = (df['status'] == 'FAILED').mean() * 100

print("Peak Hour Failure Rate (%):", round(peak_failure_rate, 2))
print("Overall Failure Rate (%):", round(overall_failure_rate, 2))

# 5. Bank Spike (SBI during peak)
sbi_peak = df[(df['issuing_bank'] == 'SBI') & (df['hour'].between(19, 22))]
sbi_peak_failure = (sbi_peak['status'] == 'FAILED').mean() * 100

print("SBI Peak Failure Rate (%):", round(sbi_peak_failure, 2))

# 6. Fraud Rate
fraud_rate = df['is_fraud'].mean() * 100
print("Fraud Rate (%):", round(fraud_rate, 2))