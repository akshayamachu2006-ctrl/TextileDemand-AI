
import pandas as pd
import plotly.express as px
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Proposed project schedule
tasks = [
    {
        "Task": "Project Planning",
        "Start": "2026-11-09",
        "Finish": "2026-11-15",
        "Phase": "Planning"
    },
    {
        "Task": "Data Acquisition",
        "Start": "2026-11-16",
        "Finish": "2026-11-22",
        "Phase": "Data Management"
    },
    {
        "Task": "Data Cleaning",
        "Start": "2026-11-23",
        "Finish": "2026-11-29",
        "Phase": "Data Management"
    },
    {
        "Task": "Exploratory Data Analysis",
        "Start": "2026-11-30",
        "Finish": "2026-12-06",
        "Phase": "Analysis"
    },
    {
        "Task": "Model Development",
        "Start": "2026-12-07",
        "Finish": "2026-12-13",
        "Phase": "Machine Learning"
    },
    {
        "Task": "Model Evaluation",
        "Start": "2026-12-14",
        "Finish": "2026-12-20",
        "Phase": "Machine Learning"
    },
    {
        "Task": "Testing and Deployment Planning",
        "Start": "2026-12-21",
        "Finish": "2026-12-27",
        "Phase": "Testing"
    },
    {
        "Task": "Final Review",
        "Start": "2026-12-28",
        "Finish": "2027-01-03",
        "Phase": "Review"
    }
]

df = pd.DataFrame(tasks)

df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# Create Gantt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Phase",
    title="TextileDemand AI - Project Gantt Chart"
)

fig.update_yaxes(autorange="reversed")

fig.update_layout(
    xaxis_title="Project Timeline",
    yaxis_title="Project Activities",
    template="plotly_white",
    height=550
)

# Save chart
report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

fig.write_html(report_dir / "project_gantt_chart.html")
fig.write_image(report_dir / "project_gantt_chart.png")

fig.show()

print("Gantt chart generated successfully!")
