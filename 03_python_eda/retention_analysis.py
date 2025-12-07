import pandas as pd

logs = pd.read_csv("../01_data/activity_logs.csv")
logs["activity_date"] = pd.to_datetime(logs["activity_date"])

# First & Last activity per user
first_seen = logs.groupby("user_id")["activity_date"].min()
last_seen = logs.groupby("user_id")["activity_date"].max()

retention_days = (last_seen - first_seen).dt.days

print("\n==== RETENTION DAYS PER USER ====")
print(retention_days)

# Churn: users inactive for 7+ days
latest_date = logs["activity_date"].max()
churn_threshold = latest_date - pd.Timedelta(days=7)

churn_users = last_seen[last_seen < churn_threshold]

print("\n==== CHURN USERS (inactive 7+ days) ====")
print(churn_users)
