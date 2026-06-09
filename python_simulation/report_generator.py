import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/waste_data.csv")

plt.figure(figsize=(10,5))

plt.plot(df["FillPercent"])

plt.title("Waste Bin Fill Level")

plt.xlabel("Reading")

plt.ylabel("Fill %")

plt.grid()

plt.savefig("outputs/charts.png")

plt.show()