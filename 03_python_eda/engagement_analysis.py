import pandas as pd

logs = pd.read_csv("../01_data/activity_logs.csv")

logs["activity_date"] = pd.to_datetime(logs["activity_date"])

# Daily Active Users
dau = logs.groupby("activity_date")["user_id"].nunique()
print("\n==== DAILY ACTIVE USERS ====")
print(dau)

# Average session time
avg_time = logs["time_spent_minutes"].mean()
print("\nAverage Session Time:", avg_time)

# Most Active Users
active_users = logs.groupby("user_id")["time_spent_minutes"].sum().sort_values(ascending=False)
print("\n==== Most Active Users ====")
print(active_users)
