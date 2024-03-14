import requests, json
import pandas as pd
import streamlit as st

from api_data import get_api_data


result = get_api_data()
df = pd.DataFrame(result)
df['SDATE'] = df['SDATE'].apply(lambda x: x[8:10])
df = df[df['ITEMCODE'].isin(['90303', '90319'])]
df_rh02 = df[df['TIMECODE'] == 'RH02']

print(df_rh02)
col1, col2 = st.columns(2)
container1 = col1.container(border=True)
container1.header('수도권')
df_rh02_pb = df_rh02[df_rh02['ITEMCODE'] == '90303']
delta = round(df_rh02_pb[df_rh02_pb['STATIONCODE'] == 1].iloc[-1]['VALUE'] - df_rh02_pb[df_rh02_pb['STATIONCODE'] == 1].iloc[-2]['VALUE'], 4)
container1.metric('납 측정수치', df_rh02_pb[df_rh02_pb['STATIONCODE'] == 1].iloc[-1]['VALUE'], f'{delta} ng/m\u00B3')

df_rh02_ca = df_rh02[df_rh02['ITEMCODE'] == '90319']
delta = round(df_rh02_ca[df_rh02_ca['STATIONCODE'] == 1].iloc[-1]['VALUE'] - df_rh02_ca[df_rh02_ca['STATIONCODE'] == 1].iloc[-2]['VALUE'], 4)
container1.metric('칼슘 측정수치', df_rh02_ca[df_rh02_ca['STATIONCODE'] == 1].iloc[-1]['VALUE'], f'{delta} ng/m\u00B3')