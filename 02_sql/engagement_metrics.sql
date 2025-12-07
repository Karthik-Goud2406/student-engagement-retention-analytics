-- Average session time
SELECT AVG(time_spent_minutes) AS avg_session_time
FROM activity_logs;

-- Most active users
SELECT user_id, SUM(time_spent_minutes) AS total_time
FROM activity_logs
GROUP BY user_id
ORDER BY total_time DESC;

-- Most used modules
SELECT module_id, COUNT(*) AS hits
FROM activity_logs
GROUP BY module_id
ORDER BY hits DESC;
