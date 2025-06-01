# visualize.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset (adjust path if needed)
df_activity = pd.read_csv("data/dailyActivity_merged.csv")

# HISTOGRAM: Number of times users logged in app across the week
plt.style.use("default")
plt.figure(figsize=(6, 4))
plt.hist(df_activity["day_of_the_week"], bins=7,
         width=0.6, color="lightskyblue", edgecolor="black")
plt.xlabel("Day of the week")
plt.ylabel("Frequency")
plt.title("No. of times users logged in app across the week")
plt.grid(True)
plt.show()

# SCATTER PLOT: Calories burned vs. steps taken
plt.figure(figsize=(8, 6))
plt.scatter(df_activity["total_steps"], df_activity["calories"],
            alpha=0.8, c=df_activity["calories"], cmap="Spectral")
median_calories = 2303
median_steps = 7637
plt.colorbar(orientation="vertical")
plt.axvline(median_steps, color="blue", label="Median steps")
plt.axhline(median_calories, color="red", label="Median calories burned")
plt.xlabel("Steps taken")
plt.ylabel("Calories burned")
plt.title("Calories burned for every step taken")
plt.grid(True)
plt.legend()
plt.show()

# SCATTER PLOT: Calories burned vs. hours logged
plt.figure(figsize=(8, 6))
plt.scatter(df_activity["total_hours"], df_activity["calories"],
            alpha=0.8, c=df_activity["calories"], cmap="Spectral")
median_hours = 20
median_sedentary = 991 / 60  # convert mins to hours for median sedentary
plt.colorbar(orientation="vertical")
plt.axvline(median_hours, color="blue", label="Median hours")
plt.axvline(median_sedentary, color="purple", label="Median sedentary hours")
plt.axhline(median_calories, color="red", label="Median calories burned")
plt.xlabel("Hours logged")
plt.ylabel("Calories burned")
plt.title("Calories burned for every hour logged")
plt.legend()
plt.grid(True)
plt.show()

# PIE CHART: Percentage of activity in minutes
very_active_mins = df_activity["very_active_mins"].sum()
fairly_active_mins = df_activity["fairly_active_mins"].sum()
lightly_active_mins = df_activity["lightly_active_mins"].sum()
sedentary_mins = df_activity["sedentary_mins"].sum()

slices = [very_active_mins, fairly_active_mins, lightly_active_mins, sedentary_mins]
labels = ["Very active minutes", "Fairly active minutes", "Lightly active minutes", "Sedentary minutes"]
colors = ["lightcoral", "yellowgreen", "lightskyblue", "darkorange"]
explode = [0, 0, 0, 0.1]  # highlight sedentary

plt.style.use("default")
plt.figure(figsize=(7, 7))
plt.pie(slices, labels=labels, colors=colors, explode=explode,
        wedgeprops={"edgecolor": "black"}, autopct="%1.1f%%")
plt.title("Percentage of Activity in Minutes")
plt.tight_layout()
plt.show()
