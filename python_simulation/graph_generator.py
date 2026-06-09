import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/waste_data.csv")

plt.figure(figsize=(12,6))

plt.plot(
    df["FillPercent"],
    marker="o"
)

plt.title(
    "Smart City Waste Monitoring Trend"
)

plt.xlabel(
    "Readings"
)

plt.ylabel(
    "Fill Percentage (%)"
)

plt.grid(True)

plt.savefig(
    "outputs/fill_level_trend.png"
)

plt.show()