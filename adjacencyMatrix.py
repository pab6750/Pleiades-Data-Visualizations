import IOReader as io
import altair as alt
import pandas as pd
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
dataset = io.open_file("pleiades-locations-latest.csv")
#names_data = io.open_file("pleiades-names-latest.csv")
#places_data = io.open_file("pleiades-places-latest.csv")

#(alt.datum.field1 == 'value1') | (alt.datum.field2 == 'value2')
#alt.condition(alt.datum.timePeriods == alt.datum.timePeriods, alt.ColorValue('white'), alt.ColorValue('black'))

chart = alt.Chart(dataset.reset_index()).mark_rect().encode(
    x=alt.X('index', title=None),
    y=alt.Y('index', title=None),
    color='timePeriods',
    tooltip='timePeriods'
)

chart.show()