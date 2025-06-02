import numpy as np
import pandas as pd
import matplotlib as plt
import datetime as dt

daily_activity = pd.read_csv("data/dailyActivity_merged.csv")

daily_activity.head(10)
missing_values_count = daily_activity.isnull().sum()
missing_values_count[:]
daily_activity.info()
unique_id = len(pd.unique(daily_activity["Id"]))
print("# of unique Id: " + str(unique_id))

daily_activity["ActivityDate"] = pd.to_datetime(daily_activity["ActivityDate"], format="%m/%d/%Y")
daily_activity.info()
daily_activity["ActivityDate"].head()

new_cols = ['Id', 'ActivityDate', 'DayOfTheWeek', 'TotalSteps', 'TotalDistance', 'TrackerDistance',
            'LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance',
            'LightActiveDistance', 'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes',
            'LightlyActiveMinutes', 'SedentaryMinutes', 'TotalExerciseMinutes', 'TotalExerciseHours', 'Calories']

df_activity = daily_activity.reindex(columns=new_cols)
df_activity.head(5)

df_activity["DayOfTheWeek"] = df_activity["ActivityDate"].dt.day_name()
df_activity["DayOfTheWeek"].head(5)

df_activity.rename(columns={"Id": "id", "ActivityDate": "date", "DayOfTheWeek": "day_of_the_week",
                            "TotalSteps": "total_steps", "TotalDistance": "total_dist",
                            "TrackerDistance": "track_dist", "LoggedActivitiesDistance": "logged_dist",
                            "VeryActiveDistance": "very_active_dist", "ModeratelyActiveDistance": "moderate_active_dist",
                            "LightActiveDistance": "light_active_dist", "SedentaryActiveDistance": "sedentary_active_dist",
                            "VeryActiveMinutes": "very_active_mins", "FairlyActiveMinutes": "fairly_active_mins",
                            "LightlyActiveMinutes": "lightly_active_mins", "SedentaryMinutes": "sedentary_mins",
                            "TotalExerciseMinutes": "total_mins", "TotalExerciseHours": "total_hours",
                            "Calories": "calories"}, inplace=True)

print(df_activity.columns.values)
df_activity.head(5)

df_activity["total_mins"] = df_activity["very_active_mins"] + df_activity["fairly_active_mins"] + \
                            df_activity["lightly_active_mins"] + df_activity["sedentary_mins"]
df_activity["total_mins"].head(5)

df_activity["total_hours"] = round(df_activity["total_mins"] / 60)
df_activity["total_hours"].head(5)

df_activity.describe()

import matplotlib.pyplot as plt

plt.style.use("default")
plt.figure(figsize=(6, 4))
plt.hist(df_activity.day_of_the_week, bins=7, width=0.6, color="lightskyblue", edgecolor="black")
plt.xlabel("Day of the week")
plt.ylabel("Frequency")
plt.title("No. of times users logged in app across the week")
plt.grid(True)
plt.show()

plt.style.use("default")
plt.figure(figsize=(8, 6))
plt.scatter(df_activity.total_steps, df_activity.calories, alpha=0.8, c=df_activity.calories, cmap="Spectral")
median_calories = 2303
median_steps = 7637
plt.colorbar(orientation="vertical")
plt.axvline(median_steps, color="Blue", label="Median steps")
plt.axhline(median_calories, color="Red", label="Median calories burned")
plt.xlabel("Steps taken")
plt.ylabel("Calories burned")
plt.title("Calories burned for every step taken")
plt.grid(True)
plt.legend()
plt.show()

plt.style.use("default")
plt.figure(figsize=(8, 6))
plt.scatter(df_activity.total_hours, df_activity.calories, alpha=0.8, c=df_activity.calories, cmap="Spectral")
median_calories = 2303
median_hours = 20
median_sedentary = 991 / 60
plt.colorbar(orientation="vertical")
plt.axvline(median_hours, color="Blue", label="Median steps")
plt.axvline(median_sedentary, color="Purple", label="Median sedentary")
plt.axhline(median_calories, color="Red", label="Median hours")
plt.xlabel("Hours logged")
plt.ylabel("Calories burned")
plt.title("Calories burned for every hour logged")
plt.legend()
plt.grid(True)
plt.show()

very_active_mins = df_activity["very_active_mins"].sum()
fairly_active_mins = df_activity["fairly_active_mins"].sum()
lightly_active_mins = df_activity["lightly_active_mins"].sum()
sedentary_mins = df_activity["sedentary_mins"].sum()

slices = [very_active_mins, fairly_active_mins, lightly_active_mins, sedentary_mins]
labels = ["Very active minutes", "Fairly active minutes", "Lightly active minutes", "Sedentary minutes"]
colours = ["lightcoral", "yellowgreen", "lightskyblue", "darkorange"]
explode = [0, 0, 0, 0.1]
plt.style.use("default")
plt.pie(slices, labels=labels, colors=colours, wedgeprops={"edgecolor": "black"}, explode=explode, autopct="%1.1f%%")
plt.title("Percentage of Activity in Minutes")
plt.tight_layout()
plt.show()
