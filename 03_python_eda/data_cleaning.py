import pandas as pd

users = pd.read_csv("../01_data/users.csv")
logs = pd.read_csv("../01_data/activity_logs.csv")
progress = pd.read_csv("../01_data/module_progress.csv")

# Handle missing values
users.fillna(method="ffill", inplace=True)
logs.fillna(0, inplace=True)
progress.fillna(0, inplace=True)

# Correct data types
logs["activity_date"] = pd.to_datetime(logs["activity_date"])
progress["last_accessed"] = pd.to_datetime(progress["last_accessed"])

print("Data cleaned successfully.")
