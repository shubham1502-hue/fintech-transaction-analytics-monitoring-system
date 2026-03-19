-- Hourly failure trend (Peak load logic)
SELECT 
    HOUR(timestamp) AS hour,
    COUNT(*) AS total_txns,
    SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) AS failed_txns,
    ROUND(SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 4) AS failure_rate
FROM transactions_clean
GROUP BY hour
ORDER BY hour;

-- Top failure contributing merchants (Pareto logic)
SELECT merchant_id,
       COUNT(*) AS failed_txns,
       SUM(amount) AS failed_gmv
FROM transactions_clean
WHERE status = 'FAILED'
GROUP BY merchant_id
ORDER BY failed_gmv DESC
LIMIT 10;

-- Failure reason contribution %
SELECT failure_reason,
       COUNT(*) AS count,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM transactions_clean
WHERE status = 'FAILED'
GROUP BY failure_reason
ORDER BY count DESC;