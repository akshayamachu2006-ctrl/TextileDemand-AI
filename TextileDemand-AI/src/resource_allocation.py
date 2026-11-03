
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

resources = [
    ["Project Coordinator", 1, "Project planning and coordination"],
    ["Data Scientist", 1, "Data analysis and ML development"],
    ["Data Analyst", 1, "Data cleaning and visualization"],
    ["Python Developer", 1, "Application development"],
    ["Project Reviewer", 1, "Testing and quality assurance"],
    ["Python", "-", "Programming language"],
    ["Pandas and NumPy", "-", "Data processing"],
    ["Scikit-learn", "-", "Machine learning"],
    ["Streamlit", "-", "Dashboard development"],
    ["VS Code", "-", "Development environment"],
    ["Computer / Laptop", 1, "Development and testing"],
]

df = pd.DataFrame(
    resources,
    columns=["Resource", "Quantity", "Responsibility / Purpose"]
)

output_dir = BASE_DIR / "reports"
output_dir.mkdir(exist_ok=True)

df.to_csv(output_dir / "resource_allocation.csv", index=False)

print("RESOURCE ALLOCATION PLAN")
print(df.to_string(index=False))

print("\nResource allocation file generated successfully!")
