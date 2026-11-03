
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load dataset
file_path = BASE_DIR / "data" / "raw" / "textile_sales_sample.csv"

df = pd.read_csv(file_path)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Calculate revenue
df["revenue"] = df["units_sold"] * df["unit_price"]

print("\n========== TEXTILE SALES ANALYSIS ==========")

# Dataset overview
print("\nDataset Information:")
print(df.info())

print("\nFirst Five Records:")
print(df.head())

# Overall sales analysis
print("\nTotal Units Sold:", df["units_sold"].sum())

print("Total Revenue:", df["revenue"].sum())

print("Average Units Sold:", np.mean(df["units_sold"]))

# Product category analysis
category_sales = df.groupby(
    "product_category"
)["units_sold"].sum()

print("\nSales by Product Category:")
print(category_sales)

# Monthly sales analysis
df["month"] = df["date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby(
    "month"
)["units_sold"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Create project reports folder
report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

# Visualize monthly sales
plt.figure(figsize=(10, 5))

monthly_sales.plot(
    kind="bar",
    title="Monthly Textile Sales Analysis"
)

plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph
plt.savefig(report_dir / "monthly_sales.png")

plt.show()

print("\nAnalysis completed successfully!")
print("Graph saved inside the reports folder.")
