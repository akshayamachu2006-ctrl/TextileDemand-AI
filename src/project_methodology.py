
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

phases = [
    {
        "Phase": "1. Project Planning",
        "Activities": "Define objectives, scope, milestones and resources",
        "Python_Technology": "Python project environment",
        "Expected_Output": "Project plan"
    },
    {
        "Phase": "2. Data Acquisition",
        "Activities": "Identify and collect historical textile sales data",
        "Python_Technology": "Pandas, CSV",
        "Expected_Output": "Raw sales dataset"
    },
    {
        "Phase": "3. Data Preprocessing",
        "Activities": "Handle missing values, duplicates and inconsistent records",
        "Python_Technology": "Pandas, NumPy",
        "Expected_Output": "Clean dataset"
    },
    {
        "Phase": "4. Exploratory Data Analysis",
        "Activities": "Analyse sales patterns and visualize trends",
        "Python_Technology": "Pandas, Matplotlib, Plotly",
        "Expected_Output": "Sales analysis report"
    },
    {
        "Phase": "5. Model Development",
        "Activities": "Select and train suitable forecasting algorithms",
        "Python_Technology": "Scikit-learn",
        "Expected_Output": "Trained forecasting model"
    },
    {
        "Phase": "6. Model Evaluation",
        "Activities": "Evaluate predictions using suitable metrics",
        "Python_Technology": "Scikit-learn, NumPy",
        "Expected_Output": "Model evaluation report"
    },
    {
        "Phase": "7. Testing and Deployment Planning",
        "Activities": "Test model outputs and plan application deployment",
        "Python_Technology": "Python, Streamlit",
        "Expected_Output": "Tested prototype"
    },
    {
        "Phase": "8. Final Review",
        "Activities": "Review outcomes and document recommendations",
        "Python_Technology": "Pandas, Matplotlib",
        "Expected_Output": "Final project report"
    }
]

df = pd.DataFrame(phases)

output_dir = BASE_DIR / "reports"
output_dir.mkdir(exist_ok=True)

df.to_csv(output_dir / "project_methodology.csv", index=False)

print("\n========== PROJECT METHODOLOGY ==========")
print(df.to_string(index=False))

print("\nTotal project phases:", len(df))
print("Methodology file generated successfully!")
