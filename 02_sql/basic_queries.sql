-- Total users
SELECT COUNT(*) AS total_users FROM users;

-- Daily Active Users
SELECT activity_date, COUNT(DISTINCT user_id) AS dau
FROM activity_logs
GROUP BY activity_date
ORDER BY activity_date;

-- Module usage
SELECT module_id, COUNT(*) AS activity_count
FROM activity_logs
GROUP BY module_id;
