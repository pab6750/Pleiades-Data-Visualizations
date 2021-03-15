import IOReader as io
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
data = io.open_file("pleiades-locations-latest.csv")
#names_data = io.open_file("pleiades-names-latest.csv")
#places_data = io.open_file("pleiades-places-latest.csv")

chart = alt.Chart(data).mark_rect().encode(
    x='title',
    y='title',
    color=color=alt.condition('', alt.ColorValue('white'), alt.ColorValue('black')),
    tooltip='timePeriodsKeys'
)