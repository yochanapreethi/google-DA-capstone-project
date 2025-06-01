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

# Add this line BEFORE reindexing (it was missing)
daily_activity["DayOfTheWeek"] = daily_activity["ActivityDate"].dt.day_name()

new_cols = [
    'Id', 'ActivityDate', 'DayOfTheWeek', 'TotalSteps', 'TotalDistance',
    'TrackerDistance', 'LoggedActivitiesDistance', 'VeryActiveDistance',
    'ModeratelyActiveDistance', 'LightActiveDistance', 'SedentaryActiveDistance',
    'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes',
    'SedentaryMinutes', 'TotalExerciseMinutes', 'TotalExerciseHours', 'Calories'
]

df_activity = daily_activity.reindex(columns=new_cols)
df_activity.head(5)

df_activity.rename(columns={
    "Id": "id", "ActivityDate": "date", "DayOfTheWeek": "day_of_the_week",
    "TotalSteps": "total_steps", "TotalDistance": "total_dist", "TrackerDistance": "track_dist",
    "LoggedActivitiesDistance": "logged_dist", "VeryActiveDistance": "very_active_dist",
    "ModeratelyActiveDistance": "moderate_active_dist", "LightActiveDistance": "light_active_dist",
    "SedentaryActiveDistance": "sedentary_active_dist", "VeryActiveMinutes": "very_active_mins",
    "FairlyActiveMinutes": "fairly_active_mins", "LightlyActiveMinutes": "lightly_active_mins",
    "SedentaryMinutes": "sedentary_mins", "TotalExerciseMinutes": "total_mins",
    "TotalExerciseHours": "total_hours", "Calories": "calories"
}, inplace=True)

print(df_activity.columns.values)
df_activity.head(5)

df_activity["total_mins"] = (
    df_activity["very_active_mins"] + df_activity["fairly_active_mins"] +
    df_activity["lightly_active_mins"] + df_activity["sedentary_mins"]
)
df_activity["total_mins"].head(5)

df_activity["total_hours"] = round(df_activity["total_mins"] / 60)
df_activity["total_hours"].head(5)
