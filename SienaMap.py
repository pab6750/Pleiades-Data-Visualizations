#Siena UID = 62adf57abfdf2645abe652f7caa19880
#Siena ID = 413293

import pandas as pd
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
df = pd.read_csv("pleiades-places-latest.csv")

df.drop(
    df[df['id'] < 413293].index, inplace=True)
df.drop(
    df[df['id'] > 413310 ].index, inplace=True)

chart = alt.Chart(df).mark_circle().encode(
    longitude='reprLong',
    latitude='reprLat',
    tooltip='geoContext'
)

chart.show()