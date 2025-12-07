import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
users = pd.read_csv("../01_data/users.csv")
logs = pd.read_csv("../01_data/activity_logs.csv")
progress = pd.read_csv("../01_data/module_progress.csv")

logs["activity_date"] = pd.to_datetime(logs["activity_date"])

# ----------------------
# Streamlit Dashboard UI
# ----------------------

st.title("📊 Student Engagement & Retention Dashboard")

st.markdown("### Platform Analytics Overview")


# 1️⃣ KPI Metrics
st.subheader("Key Metrics")

dau = logs.groupby("activity_date")["user_id"].nunique().iloc[-1]
avg_time = logs["time_spent_minutes"].mean()
total_users = users.shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Daily Active Users", dau)
col2.metric("Avg Session Time (min)", round(avg_time, 2))
col3.metric("Total Users", total_users)


# 2️⃣ DAU Trend Chart
st.subheader("📈 Daily Active Users Trend")

dau_series = logs.groupby("activity_date")["user_id"].nunique()

fig1, ax1 = plt.subplots()
dau_series.plot(kind="line", ax=ax1)
ax1.set_title("Daily Active Users")
ax1.set_xlabel("Date")
ax1.set_ylabel("Active Users")

st.pyplot(fig1)


# 3️⃣ Module Completion / Dropoff
st.subheader("📉 Dropoff Funnel (Module Completion %)")

module_completion = progress.groupby("module_id")["completion_percent"].mean()

fig2, ax2 = plt.subplots()
module_completion.plot(kind="bar", ax=ax2, color="orange")
ax2.set_title("Average Module Completion %")
ax2.set_xlabel("Module ID")
ax2.set_ylabel("Completion %")

st.pyplot(fig2)


# 4️⃣ Retention Curve
st.subheader("📊 Retention Curve")

last_seen = logs.groupby("user_id")["activity_date"].max()
first_seen = logs.groupby("user_id")["activity_date"].min()
retention_days = (last_seen - first_seen).dt.days

fig3, ax3 = plt.subplots()
ax3.hist(retention_days, bins=10, color="green")
ax3.set_title("Retention Curve")
ax3.set_xlabel("Days Active")
ax3.set_ylabel("Number of Users")

st.pyplot(fig3)


# 5️⃣ Raw Data View
st.subheader("📄 Raw Data (Optional)")

if st.checkbox("Show Users Data"):
    st.write(users)

if st.checkbox("Show Activity Logs"):
    st.write(logs)

if st.checkbox("Show Module Progress"):
    st.write(progress)


st.success("Dashboard loaded successfully!")
