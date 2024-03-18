import streamlit as st

st.markdown(
    '''
    # 대기 중 중금속 성분 수치 대시보드
    
    ### 대기환경연구소 지역별로 시간에 따른 중금속 성분 수치를 보여주는 대시보드

    - 메인 화면에는 지역별로 보여줌(_지역은 수도권, 백령도, 호남권, 중부권, 제주도, 영남권, 경기권, 충청권, 전북권, 강원권, 충북권으로 나뉘어져있음_)

    - 메인 화면에서는 가장 최근 데이터를 보여주고, 그 전 데이터와의 비교를 통해 값의 증감을 또한 보여줌

    - 메인 화면에서 그래프 버튼을 클릭하면, 시간에 따른 값의 변화를 볼 수 있음

    - 데이터는 api를 통해 실시간으로 얻음

    **API 상세 - https://www.data.go.kr/data/15016368/openapi.do#tab_layer_detail_function**
    '''
)
st.divider()
st.page_link('main.py', label='메인화면', use_container_width=True)