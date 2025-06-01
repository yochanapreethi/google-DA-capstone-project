import pandas as pd

df_activity = pd.read_csv('data/dailyActivity_merged.csv')
print(df_activity.describe())
