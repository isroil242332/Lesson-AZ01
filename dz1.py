import pandas as pd

df = pd.read_csv('travel_destinations.csv')
print(df.head())
print(df.info())
print(df.describe())