"""Starter module for TextileDemand AI. Implementation will be added step by step."""

import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "processed" / "monthly_item_demand.csv"
MODEL_FILE = BASE_DIR / "models" / "demand_model.pkl"
MAPPING_FILE = BASE_DIR / "models" / "item_mapping.csv"

REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)


# Load data and trained model
data = pd.read_csv(DATA_FILE)
model = joblib.load(MODEL_FILE)
mapping = pd.read_csv(MAPPING_FILE)

# Create year and month features
data["Year_Month"] = pd.to_datetime(data["Year_Month"])
data["year"] = data["Year_Month"].dt.year
data["month"] = data["Year_Month"].dt.month

# Use the existing item mapping
mapping_columns = mapping.columns.tolist()

if "Item Purchased" not in mapping_columns:
    raise ValueError("Item Purchased column missing from item_mapping.csv")

if "item_encoded" not in mapping_columns:
    raise ValueError("item_encoded column missing from item_mapping.csv")

data = data.merge(
    mapping[["Item Purchased", "item_encoded"]],
    on="Item Purchased",
    how="inner"
)

# Features and target
X = data[["year", "month", "item_encoded"]]
y = data["Purchase Count"]

# Chronological train-test split
unique_months = sorted(data["Year_Month"].unique())

if len(unique_months) < 2:
    raise ValueError("At least two different months are needed for evaluation.")

split_index = int(len(unique_months) * 0.8)
split_index = max(1, min(split_index, len(unique_months) - 1))

test_months = unique_months[split_index:]
test_mask = data["Year_Month"].isin(test_months)

X_test = X[test_mask]
y_test = y[test_mask]

# Generate predictions
predictions = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("\n========== MODEL EVALUATION ==========")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Testing records: {len(y_test)}")
print("======================================")

# Save actual vs predicted results
results = data.loc[test_mask, [
    "Year_Month",
    "Item Purchased",
    "Purchase Count"
]].copy()

results["Predicted Purchase Count"] = np.maximum(predictions, 0)
results["Predicted Purchase Count"] = (
    results["Predicted Purchase Count"].round(0)
)

results.to_csv(
    REPORT_DIR / "actual_vs_predicted.csv",
    index=False
)

# Save evaluation metrics
metrics = pd.DataFrame({
    "Metric": ["MAE", "RMSE"],
    "Value": [mae, rmse]
})

metrics.to_csv(
    REPORT_DIR / "model_evaluation_metrics.csv",
    index=False
)

# Actual vs predicted chart
plt.figure(figsize=(10, 6))

plt.plot(
    range(len(y_test)),
    y_test.values,
    label="Actual Demand",
    marker="o"
)

plt.plot(
    range(len(predictions)),
    predictions,
    label="Predicted Demand",
    marker="x"
)

plt.title("Actual vs Predicted Purchase Count")
plt.xlabel("Testing Records")
plt.ylabel("Purchase Count")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(REPORT_DIR / "actual_vs_predicted.png", dpi=300)
plt.close()

print("\nEvaluation files saved successfully!")
print("Check your reports folder.")
