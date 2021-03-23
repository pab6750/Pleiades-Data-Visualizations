import IOReader as io
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
locations_data = io.open_file("pleiades-locations-latest.csv")
#names_data = io.open_file("pleiades-names-latest.csv")
#places_data = io.open_file("pleiades-places-latest.csv")

locations_data['timeRange'] = locations_data['maxDate'] - locations_data['minDate']
locations_data.drop(
    locations_data[locations_data['timeRange'] > 60000].index, inplace=True)
locations_data.drop(locations_data[~(
    locations_data['featureType'] == "settlement")].index, inplace=True)


sel = alt.selection_interval()

#alt.Color('species', legend=None)


chart = alt.Chart(locations_data).mark_point().encode(
    x='reprLong:Q',
    y='timeRange',
    color=alt.condition(sel, alt.Color('timePeriodsKeys:N', legend=None), alt.value('gray')),
    tooltip='timePeriodsKeys'
).add_selection(
    sel
)

text = alt.Chart(locations_data).transform_filter(sel).mark_text(
    align='left',
    baseline='top',
).encode(
    x=alt.value(5),
    y=alt.value(5),
    text=alt.Text('average(timeRange):Q', format='.1f'),
)

(chart + text).show()
