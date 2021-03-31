#     timePeriods
# 0             M
# 5             R
# 8             H
# 10            L
# 11            T
# 14            C
# 22            4
# 24            A
# 25            O
# 27            N
# 28            2
# 29            E
# 47            U
# 52            S
# 55            I
# 78            3
# 82            B
# 100           P
# 171           1
# 265           F

import IOReader as io
import pandas as pd
import altair as alt
import numpy as np
from vega_datasets import data

alt.renderers.enable('altair_viewer')
alt.data_transformers.disable_max_rows()
df = pd.read_csv("pleiades-locations-latest.csv")

def removeDigits(dataset):
    dataset.drop(
        dataset[dataset['timePeriods'] == '1'].index, inplace=True)
    dataset.drop(
        dataset[dataset['timePeriods'] == '2'].index, inplace=True)
    dataset.drop(
        dataset[dataset['timePeriods'] == '3'].index, inplace=True)
    dataset.drop(
        dataset[dataset['timePeriods'] == '4'].index, inplace=True)

def stringContains(c, s):
    isContained = False
    s = str(s)

    for i in range(len(s)):
        if(c == s[i]):
            isContained = True

    return isContained


u = df['timePeriods'].unique()

uvLegend = {
    'M' : 2,
    'R' : 3,
    'H' : 4,
    'L' : 5,
    'T' : 6,
    'C' : 7,
    'A' : 8,
    'O' : 9,
    'N' :10,
    'E' :11,
    'U' :12,
    'S' :13,
    'I' :14,
    'K' :15,
    'Q' :16,
    'B' :17,
    'P' :18,
    'F' :19
}

uniqueValues = pd.DataFrame({'timePeriods': u,
                             'totalCount': np.zeros(len(u)),
                             'M': np.zeros(len(u)),
                             'R': np.zeros(len(u)),
                             'H': np.zeros(len(u)),
                             'L': np.zeros(len(u)),
                             'T': np.zeros(len(u)),
                             'C': np.zeros(len(u)),
                             'A': np.zeros(len(u)),
                             'O': np.zeros(len(u)),
                             'N': np.zeros(len(u)),
                             'E': np.zeros(len(u)),
                             'U': np.zeros(len(u)),
                             'S': np.zeros(len(u)),
                             'I': np.zeros(len(u)),
                             'K': np.zeros(len(u)),
                             'Q': np.zeros(len(u)),
                             'B': np.zeros(len(u)),
                             'P': np.zeros(len(u)),
                             'F': np.zeros(len(u))})

uniqueValues = uniqueValues[uniqueValues['timePeriods'].str.len().lt(2)]

removeDigits(df)
removeDigits(uniqueValues)

#print(uniqueValues)

for i in range(len(uniqueValues['timePeriods'])):
    for j in range(len(df['timePeriods'])):

        checkValue = uniqueValues.iloc[i]['timePeriods']
        datasetValue = df.iloc[j]['timePeriods']

        if stringContains(checkValue, datasetValue):
            oldValue = uniqueValues.iloc[i]['totalCount']
            uniqueValues.iat[i, 1] = oldValue + 1

            currList = list(datasetValue)

            for k in range(len(currList)):
                currValue = str(currList[k])

                if(currValue != '1' and currValue != '2' and currValue != '3' and currValue != '4'):
                    oldValue = uniqueValues.iloc[i][currValue]
                    uniqueValues.iat[i, uvLegend[currValue]] = oldValue + 1

print(uniqueValues.dtypes)
uniqueValues['totalCount'] = pd.Categorical(uniqueValues['totalCount'])

chart = alt.Chart(uniqueValues).mark_circle().encoding(
    x = 'timePeriods:N',
    y = 'totalCount:Q'
)

chart.show()