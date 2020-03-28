import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('countiesinfotest.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(1, 100, len(colorscale) - 1))
fips = df_sample['FIPS'].tolist()
values = df_sample['Corona Virus Cases'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=True,
    show_hover=False, centroid_marker={'opacity': 0},
    asp=2.9, title='Corona Virus Cases',
    legend_title='Corona Virus Cases'
)

fig.layout.template = None
fig.show()