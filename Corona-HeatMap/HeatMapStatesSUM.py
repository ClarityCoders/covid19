import plotly.express as px
from plotly.offline import plot

import pandas as pd


url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df = pd.read_csv(url, converters={'fips': lambda x: str(x)})

url = "https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
df_abbrev = pd.read_csv(url)

last_date = df['date'].max()
df = df[ df['date'] == last_date]
df = df.groupby('state')['cases'].sum().to_frame()
df = pd.merge(df, df_abbrev, left_on=df.index, right_on='State')


# =============================================================================
# default color scale choices
# ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
#              'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
#              'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
#              'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
#              'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
#              'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
#              'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
#              'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
#              'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
#              'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
#              'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
#              'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
#              'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
#              'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd']
# =============================================================================

fig = px.choropleth(df, locations=df['Abbreviation'], color=df['cases'],
                    locationmode="USA-states",
                    color_continuous_scale="magma",
                    range_color=(0, 50000),
                    scope="usa"
                          )



fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
plot(fig)