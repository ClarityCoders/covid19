import plotly.express as px
from plotly.offline import plot

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd


url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df = pd.read_csv(url, converters={'fips': lambda x: str(x)})


last_date = df['date'].max()
df = df[ df['date'] == last_date]

fig = px.choropleth(df, geojson=counties, locations='fips', color='cases',
                           color_continuous_scale="sunsetdark",
                           range_color=(0, 500),
                           scope="usa",
                          )

plot(fig)