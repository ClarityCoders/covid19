from matplotlib import pyplot as plt
import pandas as pd


df = pd.read_csv('us-counties.csv')

# Used this originally to iterate over all states.
# Currently not using and only going over top 10 states.
unique_states = df['state'].unique()

# Get last date to see which states have the most cases currently
last_date = df['date'].max()
df_last_date = df[ df['date'] == last_date]
series_last_date = df_last_date.groupby('state')['cases'].sum()
series_last_date = series_last_date.nlargest(10)

# The chat is flat before 3/15 so lets limit it to after that date.
date_after = pd.Timestamp("03/15/2020")

# Iterate over only the states in top 10
for state in series_last_date.index:
    df_state = df[ df['state'] == state].copy()
    df_state['date'] = pd.to_datetime(df_state['date'])
    # Added this to limit dates plotted to after 3/15
    df_state = df_state[ df_state['date'] > date_after]
    series_state = df_state.groupby('date')['cases'].sum()
    series_state = series_state.diff()
    plt.plot(series_state.index, series_state.values, label=state)


plt.legend()
plt.show()