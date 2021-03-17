#excel reference at: https://www.youtube.com/watch?v=QKM7q4fHYOU

import IOReader as io
import pandas as pd
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
df = pd.read_csv("pleiades-locations-latest.csv")

#the following values are approximations and they may vary depending on the position on the planet.
distanceBetweenLatitudes = 111000
distanceBetweenLongitudes = 97000

df['timeRange'] = df['maxDate'] - df['minDate']
df.drop(
    df[df['timeRange'] > 60000].index, inplace=True)

df['area'] = (df['topRightX'] - df['bottomLeftX']) * (df['topRightY'] - df['bottomLeftY'])

maxArea = df['area'].max()
minArea = df['area'].min()

originalRange = maxArea - minArea

scaledMax = 3000
scaledMin = 0

scaledRange = scaledMax - scaledMin

df['scaledArea'] = (((df['area'] - minArea) * scaledRange) / originalRange) + scaledMin

df.drop(df[df['scaledArea'] == 0].index, inplace=True)
df.drop(df[df.index % 60 != 0].index, inplace=True)

chart = alt.Chart(df).transform_window(
    index='count()'
).transform_fold(
    ['scaledArea', 'maxDate', 'minDate']
).mark_line().encode(
    x='key:N',
    y='value:Q',
    color='timePeriodsKeys'
).properties(width=500)

chart.show()