from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

figure(num=None, figsize=(16,12))
df = pd.read_csv('us-counties.csv')

unique_states = df['state'].unique()


plt.style.use('seaborn-colorblind')
print(plt.style.available)


last_date = df['date'].max()
df_last_date = df[ df['date'] == last_date]
series_last_date = df_last_date.groupby('state')['cases'].sum()
series_last_date = series_last_date.nlargest(10)

ax = plt.subplot()       
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)    

date_after = pd.Timestamp("03/15/2020")

for state in series_last_date.index:
    df_state = df[ df['state'] == state].copy()
    df_state['date'] = pd.to_datetime(df_state['date'])
    df_state = df_state[ df_state['date'] > date_after]
    
    series_state = df_state.groupby('date')['cases'].sum()
    series_state = series_state.diff()
    series_state.index = series_state.index.strftime('%b %d')
    plt.plot(series_state.index, series_state.values, label=state)

plt.ylabel("New Cases")
plt.title('Top 10 Covid-19 States')
plt.grid(True)
plt.yticks(range(0, 12001, 1000))
plt.xticks(rotation=45)
plt.legend()
plt.show()