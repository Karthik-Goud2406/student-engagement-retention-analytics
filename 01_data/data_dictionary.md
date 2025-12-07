# DATA DICTIONARY

## users.csv

user_id - Unique ID for each learner  
name - Learner name  
age - Age  
gender - M/F  
signup_date - Date of joining  
subscription_type - Free/Premium  
country - Country of user

## activity_logs.csv

log_id - Unique event ID  
user_id - Learner ID  
activity_date - Activity timestamp  
activity_type - login/video_play/quiz_attempt  
module_id - Course module  
time_spent_minutes - Time spent on activity

## module_progress.csv

progress_id - Unique row  
user_id - Learner ID  
module_id - Learning module  
completion_percent - Progress %  
last_accessed - Last activity date
