# Data Dictionary

This dataset represents simulated payment transactions used for monitoring system performance and fraud detection.

---

## Columns

| Column Name | Description |
|------------|------------|
| transaction_id | Unique identifier for each transaction |
| user_id | Unique identifier for customer |
| merchant_id | Identifier for merchant |
| amount | Transaction value (₹) |
| timestamp | Date and time of transaction |
| status | Transaction outcome (SUCCESS / FAILED) |
| failure_reason | Reason for failure (if applicable) |
| issuing_bank | Bank processing the transaction |
| payment_method | Mode of payment (Card, UPI, Wallet) |
| risk_level | Derived risk classification (High / Medium / Low) |

---

## Derived Fields

- **Failure Rate** → % of failed transactions  
- **Failed GMV** → Total value of failed transactions  
- **Success Rate** → % of successful transactions  
- **Risk Level** → Based on transaction patterns and rules  

---

## Notes

- UNKNOWN failures represent system-level or unidentified errors  
- Data is synthetically generated to simulate real-world scenarios  