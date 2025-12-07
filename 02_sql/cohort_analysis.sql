-- Cohorts by signup month
SELECT DATE_FORMAT(signup_date, '%Y-%m') AS cohort_month,
       COUNT(*) AS users
FROM users
GROUP BY cohort_month;

-- Retention per cohort
SELECT u.user_id,
       DATE_FORMAT(u.signup_date, '%Y-%m') AS cohort,
       COUNT(a.log_id) AS active_days
FROM users u
LEFT JOIN activity_logs a ON u.user_id = a.user_id
GROUP BY u.user_id;
