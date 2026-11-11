
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load processed monthly demand data
file_path = (
    BASE_DIR / "data" / "processed" / "monthly_item_demand.csv"
)

df = pd.read_csv(file_path)

print("\n========== FASHION DEMAND ANALYSIS ==========")

# Dataset overview
print("\nDataset Information:")
print(df.info())

print("\nFirst Five Records:")
print(df.head())

# Total purchase count
print("\nTotal Purchase Count:", df["Purchase Count"].sum())

# Item-wise demand analysis
item_demand = (
    df.groupby("Item Purchased")["Purchase Count"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Most Purchased Items:")
print(item_demand.head(10))

# Monthly demand analysis
monthly_demand = (
    df.groupby("Year_Month")["Purchase Count"]
    .sum()
    .sort_index()
)

print("\nMonthly Demand:")
print(monthly_demand)

# Create reports folder
report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

# Plot monthly demand
plt.figure(figsize=(10, 5))
monthly_demand.plot(kind="bar", title="Monthly Fashion Purchase Demand")

plt.xlabel("Month")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(report_dir / "monthly_demand.png")
plt.show()

# Plot top 10 items
plt.figure(figsize=(10, 5))
item_demand.head(10).plot(
    kind="bar",
    title="Top 10 Most Purchased Fashion Items"
)

plt.xlabel("Fashion Item")
plt.ylabel("Purchase Count")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(report_dir / "top_10_items.png")
plt.show()

print("\nDemand analysis completed successfully!")
print("Graphs saved inside the reports folder.")
