import IOReader as io
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
dataset = io.open_file("pleiades-locations-latest.csv")
#names_data = io.open_file("pleiades-names-latest.csv")
#places_data = io.open_file("pleiades-places-latest.csv")

dataset['timeRange'] = dataset['maxDate'] - dataset['minDate']
dataset.drop(
    dataset[dataset['timeRange'] > 60000].index, inplace=True)
dataset.drop(
    dataset[dataset['reprLat'] < 0].index, inplace=True)
dataset.drop(dataset[~(
    dataset['featureType'] == "settlement")].index, inplace=True)

chart = alt.Chart(dataset).mark_circle().encode(
    x='reprLong:Q',
    y='reprLat:Q',
    color='featureType',
    tooltip='timePeriodsKeys'
).properties(
    width=600,
    height=600
)

chart.show()