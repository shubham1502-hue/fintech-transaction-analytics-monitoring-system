-- Total GMV
SELECT SUM(amount) AS total_gmv
FROM transactions_clean;

-- Failed GMV
SELECT SUM(amount) AS failed_gmv
FROM transactions_clean
WHERE status = 'FAILED';

-- Success Rate
SELECT 
    ROUND(SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS success_rate
FROM transactions_clean;

-- Total Transactions
SELECT COUNT(*) AS total_transactions
FROM transactions_clean;