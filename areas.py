#excel reference at: https://www.youtube.com/watch?v=QKM7q4fHYOU
#IMPORTANT: make these the average, and add more dimensions
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

#rescaling area
maxArea = df['area'].max()
minArea = df['area'].min()

originalRange = maxArea - minArea

scaledMax = 3000
scaledMin = 0

scaledRange = scaledMax - scaledMin

df['scaledArea'] = (((df['area'] - minArea) * scaledRange) / originalRange) + scaledMin

#rescaling reprLat
maxReprLat = df['reprLat'].max()
minReprLat = df['reprLat'].min()

originalRange = maxReprLat - minReprLat

scaledMax = 3000
scaledMin = 0

scaledRange = scaledMax - scaledMin

df['scaledReprLat'] = (((df['reprLat'] - minReprLat) * scaledRange) / originalRange) + scaledMin

#rescaling reprLong

maxReprLong = df['reprLong'].max()
minReprLong = df['reprLong'].min()

originalRange = maxReprLong - minReprLong

scaledMax = 3000
scaledMin = 0

scaledRange = scaledMax - scaledMin

df['scaledReprLong'] = (((df['reprLong'] - minReprLong) * scaledRange) / originalRange) + scaledMin

#dropping unnecessary data

df.drop(df[df['scaledArea'] == 0].index, inplace=True)
df = df[df['timePeriodsKeys'].str.split(",").str.len().lt(2)]

#chart specification
chart = alt.Chart(df).transform_window(
    index='count()'
).transform_fold(
    ['scaledArea', 'maxDate', 'minDate', 'scaledReprLat', 'scaledReprLong']
).mark_line().encode(
    x='key:N',
    y='average(value):Q',
    color=alt.Color('timePeriods', legend=None)
).properties(width=500)

chart.show()