# Example showing how to plot a single state using a downloaded csv
from matplotlib import pyplot as plt
import pandas as pd

# Pull in our csv file make sure its in same directory.
df = pd.read_csv("us-counties.csv")

# Create a new data frame of a single state.
df_illinois = df[ df['state'] == 'Illinois'].copy()
# Make sure pandas realizes our date column is a date.
df_illinois['date'] = pd.to_datetime(df_illinois['date'])

# Sum up all the cases for Illinois by date.
# Use diff method to compair to previous day to get new cases.
series_illinois_sum = df_illinois.groupby('date')['cases'].sum()
series_illinois_diff = series_illinois_sum.diff()

plt.plot(series_illinois_diff.index, series_illinois_diff.values, label="Illinois")
#plt.xlabel("Date")
plt.ylabel("New Cases")
plt.title('Illinois new Cases per day.')
plt.legend()
plt.show()