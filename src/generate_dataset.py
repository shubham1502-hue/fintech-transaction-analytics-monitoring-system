import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

NUM_ROWS = 50000

users = [f"user_{i}" for i in range(1, 5001)]
merchants = [f"merchant_{i}" for i in range(1, 101)]
high_failure_merchants = set(merchants[:5])

payment_methods = ["UPI", "CARD", "WALLET"]
banks = ["HDFC", "SBI", "ICICI", "AXIS"]

start_time = datetime(2025, 1, 1)

data = []

def generate_amount(merchant):
    if merchant in high_failure_merchants:
        return np.random.randint(2000, 20000)
    elif np.random.rand() < 0.85:
        return np.random.randint(50, 500)
    else:
        return np.random.randint(5000, 50000)

def get_failure_reason():
    reasons = ["INSUFFICIENT_FUNDS", "BANK_DOWN", "TIMEOUT", "FRAUD_SUSPECTED"]
    return random.choice(reasons)

def is_peak_hour(hour):
    return 19 <= hour <= 22

def generate_timestamp():
    random_minutes = np.random.randint(0, 60*24*30)
    return start_time + timedelta(minutes=int(random_minutes))

for i in range(NUM_ROWS):
    user = random.choice(users)
    merchant = random.choice(merchants)
    amount = generate_amount(merchant)
    method = random.choice(payment_methods)
    bank = random.choice(banks)
    timestamp = generate_timestamp()
    hour = timestamp.hour

    base_failure_prob = 0.12

    if method == "CARD":
        base_failure_prob += 0.05
    elif method == "WALLET":
        base_failure_prob -= 0.03

    if merchant in high_failure_merchants:
        base_failure_prob += 0.20  # increase failure rate
        amount = int(amount * np.random.uniform(1.5, 3))  # increase GMV weight

    if is_peak_hour(hour):
        base_failure_prob += 0.05

    # Simulate bank downtime spike
    if bank == "SBI" and is_peak_hour(hour):
        base_failure_prob += 0.15

    status = "FAILED" if np.random.rand() < base_failure_prob else "SUCCESS"

    failure_reason = None
    if status == "FAILED":
        if np.random.rand() < 0.7:
            failure_reason = get_failure_reason()

    processing_time = np.random.normal(1200, 300)
    if is_peak_hour(hour):
        processing_time += 500

    is_fraud = 0
    if np.random.rand() < 0.02:
        is_fraud = 1

    data.append([
        f"txn_{i}",
        user,
        merchant,
        amount,
        status,
        failure_reason,
        method,
        bank,
        timestamp,
        processing_time,
        is_fraud
    ])

columns = [
    "transaction_id",
    "user_id",
    "merchant_id",
    "amount",
    "status",
    "failure_reason",
    "payment_method",
    "issuing_bank",
    "timestamp",
    "processing_time_ms",
    "is_fraud"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("transactions.csv", index=False)

print("Dataset generated: transactions.csv")