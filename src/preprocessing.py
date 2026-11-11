
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "fashion_retail_sales.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def preprocess_data():

    # Load original dataset
    df = pd.read_csv(INPUT_FILE)

    print("Original dataset shape:", df.shape)

    # Convert purchase date into datetime format
    df["Date Purchase"] = pd.to_datetime(
        df["Date Purchase"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    # Convert purchase amount into numeric values
    df["Purchase Amount (USD)"] = pd.to_numeric(
        df["Purchase Amount (USD)"],
        errors="coerce"
    )

    # Remove rows with invalid dates or missing product names
    df = df.dropna(
        subset=["Date Purchase", "Item Purchased"]
    )

    # Remove duplicate transactions
    df = df.drop_duplicates()

    # Create monthly information
    df["Year_Month"] = (
        df["Date Purchase"].dt.to_period("M").astype(str)
    )

    # Save cleaned transaction data
    cleaned_file = OUTPUT_DIR / "fashion_sales_cleaned.csv"
    df.to_csv(cleaned_file, index=False)

    # Count purchases per item per month as a demand proxy
    monthly_demand = (
        df.groupby(["Year_Month", "Item Purchased"])
        .size()
        .reset_index(name="Purchase Count")
    )

    # Save monthly demand data
    demand_file = OUTPUT_DIR / "monthly_item_demand.csv"
    monthly_demand.to_csv(demand_file, index=False)

    print("\nPreprocessing completed!")
    print("Cleaned dataset shape:", df.shape)
    print("Monthly demand records:", len(monthly_demand))
    print("\nMissing values after preprocessing:")
    print(df.isnull().sum())

    print("\nSaved files:")
    print(cleaned_file)
    print(demand_file)


if __name__ == "__main__":
    preprocess_data()
