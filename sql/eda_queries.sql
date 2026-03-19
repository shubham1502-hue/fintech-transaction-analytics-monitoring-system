-- Basic exploration

SELECT COUNT(*) AS total_transactions FROM transactions_clean;

SELECT status, COUNT(*) 
FROM transactions_clean
GROUP BY status;

SELECT failure_reason, COUNT(*) 
FROM transactions_clean
WHERE status = 'FAILED'
GROUP BY failure_reason
ORDER BY COUNT(*) DESC;