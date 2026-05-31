import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_cleaned.csv")

# Movies vs TV Shows
df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()

report = f"""
NETFLIX DATA REPORT

Total Records: {len(df)}

Movies:
{df['type'].value_counts()}

Top Countries:
{df['country'].value_counts().head(10)}
"""

with open("Netflix_Report.txt", "w") as f:
    f.write(report)