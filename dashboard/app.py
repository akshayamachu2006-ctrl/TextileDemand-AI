
from flask import Flask, render_template, jsonify, send_file
import pandas as pd
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

CLEANED_DATA = BASE_DIR / "data" / "processed" / "fashion_sales_cleaned.csv"
DEMAND_DATA = BASE_DIR / "data" / "processed" / "monthly_item_demand.csv"
PREDICTION_DATA = BASE_DIR / "reports" / "future_demand_predictions.csv"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/dashboard-data")
def dashboard_data():
    try:
        sales = pd.read_csv(CLEANED_DATA)
        demand = pd.read_csv(DEMAND_DATA)
        predictions = pd.read_csv(PREDICTION_DATA)

        total_transactions = len(sales)
        total_products = sales["Item Purchased"].nunique()

        forecast_total = int(
            predictions["Predicted Purchase Count"].sum()
        )

        monthly = (
            demand.groupby("Year_Month")["Purchase Count"]
            .sum()
            .sort_index()
        )

        top_products = (
            demand.groupby("Item Purchased")["Purchase Count"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        return jsonify({
            "total_transactions": total_transactions,
            "total_products": int(total_products),
            "forecast_total": forecast_total,
            "monthly_labels": monthly.index.tolist(),
            "monthly_values": monthly.values.tolist(),
            "top_products": [
                {"name": name, "count": int(count)}
                for name, count in top_products.items()
            ],
            "predictions": predictions.to_dict(orient="records")
        })

    except FileNotFoundError as error:
        return jsonify({
            "error": f"Required project file not found: {error.filename}"
        }), 404

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/download/predictions")
def download_predictions():
    return send_file(
        PREDICTION_DATA,
        as_attachment=True,
        download_name="future_demand_predictions.csv"
    )


@app.route("/download/monthly-demand")
def download_monthly_demand():
    return send_file(
        DEMAND_DATA,
        as_attachment=True,
        download_name="monthly_item_demand.csv"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
