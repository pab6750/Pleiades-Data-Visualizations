import IOReader as io
import pandas as pd
import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
df = pd.read_csv("pleiades-locations-latest.csv")

df['timeRange'] = df['maxDate'] - df['minDate']
df.drop(df[df['timeRange'] > 60000].index, inplace=True)
df.drop(df[type(df['bbox']) == "<class 'float'>"].index, inplace=True)
print(df['bbox'][0])
# df.loc[:, 'bottomLeftLong'] = df['bbox'].map(lambda x: x)
df['bottomLeftLong'] = df['bbox'].apply(lambda x: print(type(x)))
# print(df['bottomLeftLong'])

# df['numericBbox'] = df['bbox'].str.split(", ")
# df['area'] = df['bottomLeftLong'][0] + df['bottomLeftLong'][1]

# df['area'] = (float(df['bbox'].to_string(index=False, max_rows=1).split(
#    ", ")[2])       - float(df['bbox'].to_string(index=False, max_rows=1).split(
#    ", ")[0]))      * (float(df['bbox'].to_string(index=False, max_rows=1).split(
#    ", ")[3][:-24]) - float(df['bbox'].to_string(index=False, max_rows=1).split(", ")[2]))


# print(df['bottomLeftLong'])
# chart1 = alt.Chart(df).mark_point().encode(
#    x='timeRange',
#    y='area',
#    color='featureType',
# )


# chart1.show()
