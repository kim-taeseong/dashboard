from api_data import get_api_data, item_code, station
from datetime import datetime
from data_frame import make_data_frame

import streamlit as st

# station code와 그에 따른 이름 세팅
station_code = st.session_state['station']
station_name = station[station_code]

# 페이지에 출력
st.title(f'오늘 {station_name} 대기환경')
col1, col2, col3 = st.columns([2, 1, 1])
col1.caption(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
selected_date = col2.date_input('날짜를 선택하세요', datetime.today())

# api를 통해 데이터 get
result = get_api_data(selected_date.strftime('%Y%m%d'))

df_rh02 = make_data_frame(result)

# station_code에 따라 특정 연구소 지역에 대한 자료만 필터링
df_rh02_station = df_rh02[df_rh02['STATIONCODE'] == station_code]

# 납, 칼슘 데이터에 대한 그래프를 각각 나타내기 위해 dataFrame pivot -> itemcode를 컬럼으로 위치 변경
pivot_df_rh02_station = df_rh02_station.pivot(index='SDATE', columns='ITEMCODE', values='VALUE')

# 알아보기 쉬운 이름으로 인덱스, 컬럼 이름 변경
pivot_df_rh02_station.rename_axis(index='시간', inplace=True)
pivot_df_rh02_station.rename(columns=item_code, inplace=True)

# x축 시간이 세로로 표시 됨 -> 문자열에서 숫자로 변경
pivot_df_rh02_station.index = pivot_df_rh02_station.index.astype('uint64')

options_list = ['전체']

for i in item_code.values():
    options_list.append(i)


# 나머지 페이지 출력
selected_item = col3.selectbox(label='성분을 선택하세요', options=options_list)
if selected_item == '전체':
    st.line_chart(pivot_df_rh02_station)
else:
    st.line_chart(pivot_df_rh02_station[selected_item])
st.page_link('main.py', label='메인화면', use_container_width=True)