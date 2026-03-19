-- Merchant risk (Failed GMV)
SELECT merchant_id, SUM(amount) AS failed_gmv
FROM transactions_clean
WHERE status = 'FAILED'
GROUP BY merchant_id
ORDER BY failed_gmv DESC;

-- Bank failure rate
SELECT issuing_bank,
       ROUND(SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 4) AS failure_rate
FROM transactions_clean
GROUP BY issuing_bank
ORDER BY failure_rate DESC;

-- Payment method failure rate
SELECT payment_method,
       ROUND(SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 4) AS failure_rate
FROM transactions_clean
GROUP BY payment_method
ORDER BY failure_rate DESC;

-- High-risk users
SELECT user_id,
       COUNT(*) AS txn_count,
       SUM(amount) AS total_amount
FROM transactions_clean
GROUP BY user_id
HAVING txn_count > 2 AND total_amount > 30000
ORDER BY total_amount DESC;