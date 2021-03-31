#Volcano dataset at: https://data.humdata.org/dataset/volcano-population-exposure-index-gvm/resource/e3b1ecf0-ec47-49f7-9011-6bbb7403ef6d

import IOReader as io
import pandas as pd
import altair as alt
import numpy as np
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
locationsData = pd.read_csv("pleiades-locations-latest.csv")
volcanoData = pd.read_csv("volcano.csv")
countries = alt.topo_feature(data.world_110m.url, 'countries')

#preprocessing
locationsData['timeRange'] = locationsData['maxDate'] - locationsData['minDate']

#dropping unnecessary data
locationsData.drop(locationsData[~(
    locationsData['featureType'] == "settlement")].index, inplace=True)
locationsData.drop(
    locationsData[locationsData['timeRange'] > 60000].index, inplace=True)

#scaling specification
scaling = alt.selection_interval(bind='scales')

#width and height of window
widthValue = 700
heightValue = 700

#volcano chart specification
volcanoChart = alt.Chart(volcanoData).mark_circle().encode(
    longitude='Longitude',
    latitude='Latitude',
    color = alt.value('red'),
    tooltip = 'V_Name'
).properties(
    width=widthValue,
    height=heightValue,
)

#pleiades chart specification
pleiadesChart = alt.Chart(locationsData).mark_point(
    filled=True,
    size=10
).encode(
    longitude='reprLong',
    latitude='reprLat',
    color='timeRange:Q',
    tooltip = 'timePeriodsKeys'
).properties(
    width=widthValue,
    height=heightValue
)

#geomap parameters
scaleValue = 700
translation = [100, 800]

#geomap specification
mapData = alt.layer(
    alt.Chart(countries).mark_geoshape(fill='black'),
    volcanoChart,
    pleiadesChart
).project(
    type='equirectangular', scale=scaleValue, translate=translation
).properties(width=widthValue, height=heightValue).configure_view(stroke=None)

mapData.show()