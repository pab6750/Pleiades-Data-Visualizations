#IMPORTANT: make these the average, and add more dimensions
import IOReader as io
import pandas as pd
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
data = io.open_file("pleiades-locations-latest.csv")
#names_data = io.open_file("pleiades-names-latest.csv")
#places_data = io.open_file("pleiades-places-latest.csv")

# alt.Chart(source).transform_window(
#     index='count()'
# ).transform_fold(
#     ['petalLength', 'petalWidth', 'sepalLength', 'sepalWidth']
# ).mark_line().encode(
#     x='key:N',
#     y='value:Q',
#     color='species:N',
#     detail='index:N',
#     opacity=alt.value(0.5)
# ).properties(width=500)

pc = alt.Chart(data).transform_window(
    index='count()'
).transform_fold(
    []
).mark_line().encode(
    x='',
    y='',
    color='',
).properties(width=500)

pc.show()