from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('us-counties.csv')

unique_states = df['state'].unique()

last_date = df['date'].max()
df_last_date = df[ df['date'] == last_date]
series_last_date = df_last_date.groupby('state')['cases'].sum()
series_last_date = series_last_date.nlargest(5)

date_after = pd.Timestamp("03/15/2020")

for state in series_last_date.index:
    df_state = df[ df['state'] == state].copy()
    df_state['date'] = pd.to_datetime(df_state['date'])
    df_state = df_state[ df_state['date'] > date_after]
    
    series_state = df_state.groupby('date')['cases'].sum()
    series_state = series_state.diff()
    plt.plot(series_state.index, series_state.values, label=state)


plt.legend()
plt.show()