"""Starter module for TextileDemand AI. Implementation will be added step by step."""

import pandas as pd
import joblib
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_FILE = BASE_DIR / "models" / "demand_model.pkl"
MAPPING_FILE = BASE_DIR / "models" / "item_mapping.csv"
DATA_FILE = BASE_DIR / "data" / "processed" / "monthly_item_demand.csv"
OUTPUT_DIR = BASE_DIR / "reports"

OUTPUT_DIR.mkdir(exist_ok=True)

# Load trained model and item mapping
model = joblib.load(MODEL_FILE)
mapping = pd.read_csv(MAPPING_FILE)

# Find the next month after the latest historical month
df = pd.read_csv(DATA_FILE)
df["Year_Month"] = pd.to_datetime(df["Year_Month"])

latest_month = df["Year_Month"].max()
next_month = latest_month + pd.offsets.MonthBegin(1)

# Prepare prediction records
future_data = mapping.copy()

future_data["year"] = next_month.year
future_data["month"] = next_month.month

features = ["year", "month", "item_encoded"]

# Predict future demand
future_data["Predicted Purchase Count"] = model.predict(
    future_data[features]
).round(0).astype(int)

# Prevent negative purchase counts
future_data["Predicted Purchase Count"] = (
    future_data["Predicted Purchase Count"].clip(lower=0)
)

# Save predictions
predictions = future_data[
    ["Item Purchased", "Predicted Purchase Count"]
]

output_file = OUTPUT_DIR / "future_demand_predictions.csv"
predictions.to_csv(output_file, index=False)

print("\n========== FUTURE DEMAND PREDICTION ==========")
print("Forecast month:", next_month.strftime("%B %Y"))
print(predictions.to_string(index=False))

print("\nPrediction completed successfully!")
print("Saved to:", output_file)
