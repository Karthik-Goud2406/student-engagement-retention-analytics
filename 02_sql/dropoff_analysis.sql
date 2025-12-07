-- Dropoff per module
SELECT module_id,
       AVG(completion_percent) AS avg_completion
FROM module_progress
GROUP BY module_id;

-- Users who stopped before 50%
SELECT user_id, completion_percent
FROM module_progress
WHERE completion_percent < 50;
