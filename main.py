import streamlit as st

from api_data import get_api_data
from metric import make_metric
from data_frame import make_data_frame

result = get_api_data()
df_rh02 = make_data_frame(result)

row1 = st.columns(2)
row2 = st.columns(2)
row3 = st.columns(2)
row4 = st.columns(2)
row5 = st.columns(2)
row6 = st.columns(2)

for i, col in enumerate(row1 + row2 + row3 + row4 + row5 + row6):
    container = col.container(border=True)
    make_metric(df_rh02, container, i+1)