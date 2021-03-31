#Siena UID = 62adf57abfdf2645abe652f7caa19880
#Siena ID = 413293
#Siena connectsWith = 702,604,147,136,661,000
#Siena coordinates (lat, long) = 43.318695,11.330502

import pandas as pd
import altair as alt
import numpy as np
from vega_datasets import data

#loading data
alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
df = pd.read_csv("pleiades-places-latest.csv")

#geomap
countries = alt.topo_feature(data.world_110m.url, 'countries')

#dropping samples outside of Tuscany
df.drop(df[df['reprLat'] < 42].index, inplace=True)
df.drop(df[df['reprLat'] > 44].index, inplace=True)

df.drop(df[df['reprLong'] < 10].index, inplace=True)
df.drop(df[df['reprLong'] > 12].index, inplace=True)

#dropping samples that aren't clearly identified by one time period
df = df[df['timePeriodsKeys'].str.split(",").str.len().lt(2)]

#window height and width
widthValue = 700
heightValue = 700

#chart specifications
chart = alt.Chart(df).mark_circle().encode(
    longitude='reprLong',
    latitude='reprLat',
    color='timePeriodsKeys',
    tooltip='title'
)

#geomap parameters
scaleValue = 5300
translation = [-700, 4300]

#geomap specification
mapData = alt.layer(
    alt.Chart(countries).mark_geoshape(fill='black'),
).project(
    type='equirectangular', scale=scaleValue, translate=translation
).properties(width=widthValue, height=heightValue).configure_view(stroke=None)

(mapData + chart).show()
