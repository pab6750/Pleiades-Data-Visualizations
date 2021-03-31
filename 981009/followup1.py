import IOReader as io
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
dataset = io.open_file("pleiades-locations-latest.csv")

countries = alt.topo_feature(data.world_110m.url, 'countries')

#preprocessing
dataset['timeRange'] = dataset['maxDate'] - dataset['minDate']
dataset.drop(
    dataset[dataset['timeRange'] > 60000].index, inplace=True)
dataset.drop(
    dataset[dataset['reprLat'] < 0].index, inplace=True)


#width and height of window
widthValue = 700
heightValue = 700

#slider
minDateSlider = alt.binding_range(min=-750, max=2000, step=10)
minDateSel = alt.selection_single(name="minDate", fields=['minDate'],
                                   bind=minDateSlider, init={'minDate': -750})

#chart specification
chart = alt.Chart(dataset).mark_circle().encode(
    longitude='reprLong',
    latitude='reprLat',
    color=alt.Color('timePeriodsKeys:N', legend=None),
    tooltip = 'timePeriodsKeys'
).properties(
    width=widthValue,
    height=heightValue,
).add_selection(
    minDateSel
).transform_filter(
    alt.datum.minDate < minDateSel.minDate
)

#geomap parameters
scaleValue = 350
translation = [100, 630]

#geomap specification
mapData = alt.layer(
    alt.Chart(countries).mark_geoshape(fill='black'),
).project(
    type='equirectangular', scale=scaleValue, translate=translation
).properties(width=widthValue, height=heightValue).configure_view(stroke=None)

(mapData + chart).show()