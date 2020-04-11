from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("us-counties.csv")
print(df)

# Style Options do this last
# plt.style.use('seaborn-deep')

# do wihtout copy explain error
#df_illinois = df[ df['state'] == 'Illinois']
df_illinois = df[ df['state'] == 'Illinois'].copy()
df_illinois['date'] = pd.to_datetime(df_illinois['date'])

series_illinois_sum = df_illinois.groupby('date')['cases'].sum()
series_illinois_diff = series_illinois_sum.diff()

#series_illinois = series_illinois.diff()
plt.plot(series_illinois_diff.index, series_illinois_diff.values, label="Illinois")
#plt.xlabel("Date")
plt.ylabel("New Cases")
plt.title('Illinois new Cases per day.')
plt.legend()
plt.show()