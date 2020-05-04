from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    )

unique_states = df['state'].unique()
plt.style.use("seaborn-talk")

# Get last date to see which states have the most cases currently
last_date = df['date'].max()
df_last_date = df[ df['date'] == last_date]
series_last_date = df_last_date.groupby('state')['cases'].sum().sort_values(ascending=False)
print(series_last_date)

labels = []
values = []
state_count = 5
other_total = 0
for state in series_last_date.index:
    if state_count > 0:
        labels.append(state)
        values.append(series_last_date[state])
        state_count -= 1
    else:
        other_total += series_last_date[state]
labels.append("Other")
values.append(other_total)

wedge_dict = {
    'edgecolor': 'black',
    'linewidth': 2        
}

explode = (0, 0.1, 0, 0, 0, 0)

plt.title(f"Total Cases on {last_date}")
plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%', wedgeprops=wedge_dict)
plt.show()