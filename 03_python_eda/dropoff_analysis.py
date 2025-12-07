import pandas as pd

progress = pd.read_csv("../01_data/module_progress.csv")

# Dropoff users (<50% complete)
dropoff = progress[progress["completion_percent"] < 50]

print("\n==== DROPOFF USERS (<50%) ====")
print(dropoff)

# Module completion summary
module_avg = progress.groupby("module_id")["completion_percent"].mean()

print("\n==== AVG MODULE COMPLETION ====")
print(module_avg)
