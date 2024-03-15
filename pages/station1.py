from api_data import get_api_data
from datetime import datetime
from data_frame import make_data_frame

import streamlit as st
import pandas as pd

# api를 통해 데이터 get
result = get_api_data()

df_rh02 = make_data_frame(result)

# 수도권(1)에 대한 자료만 필터링
df_rh02_station01 = df_rh02[df_rh02['STATIONCODE'] == 1]

# 납, 칼슘 데이터에 대한 그래프를 각각 나타내기 위해 dataFrame pivot -> itemcode를 컬럼으로 위치 변경
pivot_df_rh02_station01 = df_rh02_station01.pivot(index='SDATE', columns='ITEMCODE', values='VALUE')

# 알아보기 쉬운 이름으로 인덱스, 컬럼 이름 변경
pivot_df_rh02_station01.rename_axis(index='시간', inplace=True)
pivot_df_rh02_station01.rename(columns={'90303': '납', '90319': '칼슘'}, inplace=True)

# x축 시간이 세로로 표시 됨 -> 문자열에서 숫자로 변경
pivot_df_rh02_station01.index = pivot_df_rh02_station01.index.astype('uint64')

# 페이지에 출력
st.title('오늘 수도권 대기환경')
st.caption(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
st.line_chart(pivot_df_rh02_station01, color=['#FF0000', '#FFA500'])
st.page_link('main.py', label='메인화면', use_container_width=True)