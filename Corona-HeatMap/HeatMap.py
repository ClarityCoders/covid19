import plotly.express as px
from plotly.offline import plot

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

counties["features"][0]

import pandas as pd


url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df = pd.read_csv(url, converters={'fips': lambda x: str(x)})

#df_NewYork = df[ df['state'] == "New York"]
df_NewYork = df
last_date = df['date'].max()
#df = df_NewYork[ df_NewYork['date'] == last_date]
df = df_NewYork[ df_NewYork['date'] == "2020-04-01"]

fig = px.choropleth(df, geojson=counties, locations='fips', color='cases',
                           color_continuous_scale="Viridis",
                           range_color=(1000, 15000),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
plot(fig)