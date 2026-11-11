
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "processed" / "monthly_item_demand.csv"
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)
df["Year_Month"] = pd.to_datetime(df["Year_Month"])

# Sort chronologically
df = df.sort_values("Year_Month").copy()

# Create item encoding
df["item_encoded"] = df["Item Purchased"].astype("category").cat.codes

# Create time features
df["year"] = df["Year_Month"].dt.year
df["month"] = df["Year_Month"].dt.month

# Split using the last 20% of months for testing
months = sorted(df["Year_Month"].unique())
split_index = max(1, int(len(months) * 0.8))

train_months = months[:split_index]
test_months = months[split_index:]

if not test_months:
    raise ValueError("Not enough months for chronological testing.")

train_df = df[df["Year_Month"].isin(train_months)]
test_df = df[df["Year_Month"].isin(test_months)]

features = ["year", "month", "item_encoded"]
target = "Purchase Count"

X_train = train_df[features]
X_test = test_df[features]
y_train = train_df[target]
y_test = test_df[target]

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("\n========== CHRONOLOGICAL MODEL EVALUATION ==========")
print("Training months:", len(train_months))
print("Testing months:", len(test_months))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

# Save model and item mapping
joblib.dump(model, MODEL_DIR / "demand_model.pkl")

mapping = df[["Item Purchased", "item_encoded"]].drop_duplicates()
mapping.to_csv(MODEL_DIR / "item_mapping.csv", index=False)

print("\nImproved model saved successfully!")
