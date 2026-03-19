-- Which bank contributes most to failures in terms of GMV?
SELECT issuing_bank,
       SUM(amount) AS failed_gmv
FROM transactions_clean
WHERE status = 'FAILED'
GROUP BY issuing_bank
ORDER BY failed_gmv DESC;

-- Which payment method is most unreliable?
SELECT payment_method,
       COUNT(*) AS total_txns,
       SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) AS failed_txns,
       ROUND(SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 4) AS failure_rate
FROM transactions_clean
GROUP BY payment_method
ORDER BY failure_rate DESC;

-- Users with abnormal behavior
SELECT user_id,
       COUNT(*) AS txn_count,
       SUM(amount) AS total_amount,
       AVG(amount) AS avg_amount
FROM transactions_clean
GROUP BY user_id
HAVING txn_count > 2 AND avg_amount > 10000
ORDER BY total_amount DESC;