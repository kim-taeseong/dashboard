import requests, json
import pandas as pd
import streamlit as st

from api_data import get_api_data
from metric import make_metric

result = get_api_data()
df = pd.DataFrame(result)
df['SDATE'] = df['SDATE'].apply(lambda x: x[8:10])
df = df[df['ITEMCODE'].isin(['90303', '90319'])]
df_rh02 = df[df['TIMECODE'] == 'RH02']

print(df_rh02)
col1, col2 = st.columns(2)
container1 = col1.container(border=True)


make_metric(df_rh02, container1, 1)
container1.page_link('pages/station1.py', label='상세페이지', use_container_width=True)