import os

print("Running Data Cleaning...")
os.system("python data_cleaning.py")

print("\nRunning Engagement Analysis...")
os.system("python engagement_analysis.py")

print("\nRunning Retention Analysis...")
os.system("python retention_analysis.py")

print("\nRunning Dropoff Analysis...")
os.system("python dropoff_analysis.py")

print("\nGenerating Charts...")
os.system("python charts.py")

print("\n==== PROJECT COMPLETE ====")
print("All outputs are generated in:")
print("-> 03_python_eda (terminal results)")
print("-> 04_dashboard (charts PNG files)")
