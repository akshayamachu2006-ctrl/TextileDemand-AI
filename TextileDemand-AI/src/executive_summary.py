
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

summary = """
EXECUTIVE SUMMARY
TEXTILEDEMAND AI

PROJECT OVERVIEW

TextileDemand AI is a proposed Python-based demand
forecasting system designed for a hypothetical textile
manufacturing company in Coimbatore, Tamil Nadu.

PROJECT GOALS

The primary goal is to analyse historical textile sales
data and predict future product demand using data science
and machine learning techniques.

The system aims to support production planning,
inventory management and informed business decisions.

TECHNOLOGIES

Python
Pandas
NumPy
Matplotlib
Scikit-learn
Plotly
Streamlit

PROJECT TIMELINE

Week 1: Project Planning
Week 2: Data Acquisition
Week 3: Data Cleaning and Preprocessing
Week 4: Exploratory Data Analysis
Week 5: Model Development
Week 6: Model Evaluation
Week 7: Testing and Deployment Planning
Week 8: Final Review

EXPECTED DELIVERABLES

1. Historical sales data analysis.
2. Cleaned and processed dataset.
3. Exploratory data analysis report.
4. Trained demand forecasting model.
5. Model evaluation report.
6. Demand prediction prototype.
7. Visualisation dashboard.
8. Final project documentation.

PROJECT BENEFITS

The proposed system aims to improve demand estimation,
support inventory decisions, identify sales patterns
and reduce uncertainty in production planning.

CONCLUSION

TextileDemand AI demonstrates how Python-based data
science and machine learning techniques can support
better decision-making in textile manufacturing.
"""

report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

output_file = report_dir / "executive_summary.txt"

output_file.write_text(summary, encoding="utf-8")

print(summary)
print("\nExecutive summary generated successfully!")
