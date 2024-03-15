import requests, json
import pandas as pd
import streamlit as st

from api_data import get_api_data
from metric import make_metric
from data_frame import make_data_frame


result = get_api_data()
df_rh02 = make_data_frame(result)
print(df_rh02)
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

for i, col in enumerate(row1 + row2 + row3 + row4):
    container = col.container(border=True)
    make_metric(df_rh02, container, i+1)