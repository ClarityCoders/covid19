from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import pandas as pd
import datetime

figure(num=None, figsize=(16,12))

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df = pd.read_csv(url)
#df = pd.read_csv('us-counties.csv')


last_date = df['date'].max()
df_last_date = df[ df['date'] == last_date]
series_last_date = df_last_date.groupby('state')['cases'].sum()
series_last_date = series_last_date.nlargest(5)

print(series_last_date)

plt.style.use('seaborn-deep')

# doesn't have to add up to 100
slices = series_last_date.values
labels = series_last_date.index

# 1 Do this then talk about formatting--------------------------------------------------------------
#plt.pie(slices, labels=labels, wedgeprops={"edgecolor":"black"})

# 2 Talk about explode
explode = (0,0.1,0,0,0)
explode = (0.1,0.1,0.1,0.1,0.1)

#plt.pie(slices, labels=labels, explode=explode, wedgeprops={"edgecolor":"black"}, autopct='%.1f%%', shadow=True)
plt.pie(slices, labels=labels, explode=explode, wedgeprops={"edgecolor":"black"}, autopct='%.1f%%')

plt.show()