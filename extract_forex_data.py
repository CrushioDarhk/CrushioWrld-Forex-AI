import pandas as pd
from datetime import datetime, timedelta
import json

# Load your JSON file (replace 'C:This PC/Downloads/eur_usd_data.json' with your file’s name if different)
with open('C:This PC/Downloads/eur_usd_data.json') as file:
    data = json.load(file)


# Pull the daily time series data
time_series = data['Time Series FX (Daily)']

# Set a 5-year window
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)  # Roughly 1,825 days

# Filter data to the last 5 years
dates = [date for date in time_series if start_date <= datetime.strptime(date, '%Y-%m-%d') <= end_date]

# Build a DataFrame
df = pd.DataFrame({date: time_series[date] for date in dates}).T
df.index = pd.to_datetime(df.index)
df = df.sort_index()  # Sort from oldest to newest

# Rename columns
df.columns = ['Open', 'High', 'Low', 'Close']

# Save as CSV
df.to_csv('C:This PC/Downloads/eur_usd_5years.csv')
print("5 years of data saved as eur_usd_5years.csv!")
