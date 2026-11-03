
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

risks = [
    {
        "Risk_ID": "R01",
        "Risk": "Missing or incomplete sales data",
        "Probability": "High",
        "Impact": "High",
        "Mitigation": "Validate datasets and handle missing values",
        "Contingency": "Use an alternative verified dataset"
    },
    {
        "Risk_ID": "R02",
        "Risk": "Insufficient historical data",
        "Probability": "Medium",
        "Impact": "High",
        "Mitigation": "Check data coverage before model development",
        "Contingency": "Use a suitable baseline forecasting method"
    },
    {
        "Risk_ID": "R03",
        "Risk": "Low model prediction accuracy",
        "Probability": "Medium",
        "Impact": "High",
        "Mitigation": "Compare multiple models and tune parameters",
        "Contingency": "Revisit features and forecasting approach"
    },
    {
        "Risk_ID": "R04",
        "Risk": "Project schedule delays",
        "Probability": "Medium",
        "Impact": "Medium",
        "Mitigation": "Track milestones and review progress weekly",
        "Contingency": "Reallocate resources and revise deadlines"
    },
    {
        "Risk_ID": "R05",
        "Risk": "Technical or software failures",
        "Probability": "Medium",
        "Impact": "Medium",
        "Mitigation": "Test code regularly and maintain backups",
        "Contingency": "Restore backup and use an alternative environment"
    },
    {
        "Risk_ID": "R06",
        "Risk": "Data privacy or security issues",
        "Probability": "Low",
        "Impact": "High",
        "Mitigation": "Use authorised datasets and restrict access",
        "Contingency": "Stop affected processing and follow incident procedures"
    },
    {
        "Risk_ID": "R07",
        "Risk": "Resource or team availability issues",
        "Probability": "Medium",
        "Impact": "Medium",
        "Mitigation": "Assign backup responsibilities and plan workloads",
        "Contingency": "Redistribute tasks among available team members"
    }
]

df = pd.DataFrame(risks)

output_dir = BASE_DIR / "reports"
output_dir.mkdir(exist_ok=True)

file_path = output_dir / "risk_management_plan.csv"

df.to_csv(file_path, index=False)

print("\n========== RISK MANAGEMENT PLAN ==========")
print(df.to_string(index=False))

print("\nTotal risks identified:", len(df))
print("Risk management plan saved successfully!")
print("Location:", file_path)
