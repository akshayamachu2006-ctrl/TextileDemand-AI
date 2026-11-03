
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

project_scope = """
TEXTILEDEMAND AI - PROJECT SCOPE

PROJECT OVERVIEW:
Develop a Python-based demand forecasting system
for a hypothetical textile manufacturing company
located in Coimbatore, Tamil Nadu.

PROJECT SCOPE:
1. Analyse historical textile sales data.
2. Identify sales trends and seasonal patterns.
3. Clean and preprocess historical datasets.
4. Develop a suitable machine learning forecasting model.
5. Evaluate model performance.
6. Generate future demand predictions.
7. Present analytical results through visualisations.

PROJECT OBJECTIVES:
1. Develop a reliable data preprocessing workflow.
2. Identify important factors influencing product demand.
3. Compare suitable forecasting algorithms.
4. Evaluate predictions using MAE and RMSE.
5. Support production and inventory planning.

OUT OF SCOPE:
1. Actual factory automation.
2. Direct integration with supplier systems.
3. Real-time customer transaction processing.
4. Full-scale commercial deployment.

EXPECTED OUTCOME:
A tested prototype that demonstrates how Python-based
data science techniques can support textile demand
forecasting and business decision-making.
"""

report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

output_file = report_dir / "project_scope.txt"

output_file.write_text(project_scope, encoding="utf-8")

print(project_scope)
print("\nProject scope document generated successfully!")
