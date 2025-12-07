-- Retention: users returning after signup
SELECT u.user_id, u.signup_date, MIN(a.activity_date) AS first_activity
FROM users u
LEFT JOIN activity_logs a ON u.user_id = a.user_id
GROUP BY u.user_id;

-- Churn: users inactive for 7+ days
SELECT user_id
FROM activity_logs
GROUP BY user_id
HAVING MAX(activity_date) < DATE('2024-02-10');
