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
    container.page_link('pages/station1.py', label='상세페이지', use_container_width=True)
# if 'station' not in st.session_state:
#     st.session_state['station'] = None

# def set_session(station):
#     st.session_state['station'] = station

# if container1.button('그래프', on_click=set_session(1), use_container_width=True):
#     st.switch_page('pages/station1.py')