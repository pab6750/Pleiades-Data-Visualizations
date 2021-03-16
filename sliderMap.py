import IOReader as io
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
dataset = io.open_file("pleiades-locations-latest.csv")
#names_data = io.open_file("pleiades-names-latest.csv")
#places_data = io.open_file("pleiades-places-latest.csv")

#preprocessing
dataset['timeRange'] = dataset['maxDate'] - dataset['minDate']
dataset.drop(
    dataset[dataset['timeRange'] > 60000].index, inplace=True)
dataset.drop(
    dataset[dataset['reprLat'] < 0].index, inplace=True)


#slider
scales = alt.selection_interval(bind='scales')
minDateSlider = alt.binding_range(min=-750, max=2000, step=10)
minDateSel = alt.selection_single(name="minDate", fields=['minDate'],
                                   bind=minDateSlider, init={'minDate': -750})

chart = alt.Chart(dataset).mark_circle().encode(
    x='reprLong:Q',
    y='reprLat:Q',
    color='timePeriodsKeys',
    tooltip = 'timePeriodsKeys'
).properties(
    width=600,
    height=600
).add_selection(
    minDateSel,
    scales
).transform_filter(
    alt.datum.minDate < minDateSel.minDate
)

chart.show()