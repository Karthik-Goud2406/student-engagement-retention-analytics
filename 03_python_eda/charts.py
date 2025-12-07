
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
logs = pd.read_csv("../01_data/activity_logs.csv")
progress = pd.read_csv("../01_data/module_progress.csv")

logs["activity_date"] = pd.to_datetime(logs["activity_date"])

# -------------------------------
# 1️⃣ Daily Active Users Chart
# -------------------------------
dau = logs.groupby("activity_date")["user_id"].nunique()

plt.figure(figsize=(8,4))
dau.plot(kind="line")
plt.title("Daily Active Users (DAU)")
plt.xlabel("Date")
plt.ylabel("Active Users")
plt.savefig("../04_dashboard/dau_trend.png")
plt.close()

# -------------------------------
# 2️⃣ Retention Curve
# -------------------------------
last_seen = logs.groupby("user_id")["activity_date"].max()
first_seen = logs.groupby("user_id")["activity_date"].min()

retention_days = (last_seen - first_seen).dt.days

plt.figure(figsize=(8,4))
plt.hist(retention_days, bins=10)
plt.title("Retention Curve")
plt.xlabel("Days Active")
plt.ylabel("Users")
plt.savefig("../04_dashboard/retention_curve.png")
plt.close()

# -------------------------------
# 3️⃣ Dropoff Funnel Chart
# -------------------------------
module_completion = progress.groupby("module_id")["completion_percent"].mean()

plt.figure(figsize=(6,4))
module_completion.plot(kind="bar")
plt.title("Module Completion (Dropoff Funnel)")
plt.xlabel("Module")
plt.ylabel("Avg Completion %")
plt.savefig("../04_dashboard/dropoff_funnel.png")
plt.close()

print("Charts generated successfully!")
