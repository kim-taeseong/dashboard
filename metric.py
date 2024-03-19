from api_data import item_code, station

import streamlit as st

def make_metric(data, container, station_code):
    '''
    데이터 프레임을 기반으로 연구소 지역의 대기 중 납, 칼슘 수치를 나타내는 metric 생성 함수(현재 시간 기준으로 가장 최근 데이터와 그 전 데이터 비교값도 출력)

    매개변수
    data(DataFrame): api 호출의 결과로 만든 데이터프레임
    container(DeltaGenerator): streamli의 container
    station_code(int): 대기환경연구소 코드
    '''
    if station_code not in station.keys():
        return
    
    # 값에 따라 다른 결과를 보여주기 위해 session state 사용
    if 'station' not in st.session_state:
        st.session_state['station'] = None

    # 버튼의 on_click에 쓸 함수
    def set_session(station):
        st.session_state['station'] = station

    # container header
    container.header(station[station_code])
    col1, col2 = container.columns(2)
    try:
        for i, key in enumerate(item_code.keys()):
            # 각 성분 metric
            df_rh02_key = data[data['ITEMCODE'] == key]
            after_key = df_rh02_key[df_rh02_key['STATIONCODE'] == station_code].iloc[-1]['VALUE']
            before_key = df_rh02_key[df_rh02_key['STATIONCODE'] == station_code].iloc[-2]['VALUE']
            delta = round(after_key - before_key, 4)
            if i % 2 == 0:
                col1.metric(f'{item_code[key]} 측정수치', after_key, f'{delta} ng/m\u00B3', 'inverse')
            else:
                col2.metric(f'{item_code[key]} 측정수치', after_key, f'{delta} ng/m\u00B3', 'inverse')

        if container.button('그래프', on_click=set_session(station_code), use_container_width=True, key=station_code):
            st.switch_page('pages/station.py')
    except IndexError:
        for i, key in enumerate(item_code.keys()):
            # 각 성분 metric
            df_rh02_key = data[data['ITEMCODE'] == key]
            if i % 2 == 0:
                col1.metric(f'{item_code[key]} 측정수치', '---')
            else:
                col2.metric(f'{item_code[key]} 측정수치', '---')

        container.write('해당하는 데이터가 없습니다.')
        # container.page_link('pages/station1.py', label='상세페이지', use_container_width=True, disabled=True)
        container.button('그래프', use_container_width=True, disabled=True, key=station_code)