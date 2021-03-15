import IOReader as io
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
locations_data = io.open_file("pleiades-locations-latest.csv")
#names_data = io.open_file("pleiades-names-latest.csv")
#places_data = io.open_file("pleiades-places-latest.csv")

locations_data['timeRange'] = locations_data['maxDate'] - locations_data['minDate']

sphere = alt.sphere()
graticule = alt.graticule()
countries = alt.topo_feature(data.world_110m.url, 'countries')


coordinates = alt.Chart(locations_data).mark_circle().encode(
    longitude='reprLong:Q',
    latitude='reprLat:Q',
    size=alt.value(10),
    color='timeRange'
)

chart = alt.layer(
    alt.Chart(sphere).mark_geoshape(fill='lightblue'),
    alt.Chart(graticule).mark_geoshape(stroke='white', strokeWidth=0.5),
    alt.Chart(countries).mark_geoshape(fill='green'),
).project(
    type='azimuthalEqualArea', scale=400, translate=[100,500]
).properties(width=700, height=700).configure_view(stroke=None)

(chart + coordinates).show()