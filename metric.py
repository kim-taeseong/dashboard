station = {
    1: '수도권',
    2: '백령도',
    3: '호남권',
    4: '중부권',
    5: '제주도',
    6: '영남권',
    7: '경기권',
    8: '충췅권',
    9: '전북권',
    10: '강원권',
    11: '충북권'
}

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
    # container header
    container.header(station[station_code])
    try:
        # 납 성분 metric
        df_rh02_pb = data[data['ITEMCODE'] == '90303']
        after_pb = df_rh02_pb[df_rh02_pb['STATIONCODE'] == station_code].iloc[-1]['VALUE']
        before_pb = df_rh02_pb[df_rh02_pb['STATIONCODE'] == station_code].iloc[-2]['VALUE']
        delta = round(after_pb - before_pb, 4)
        container.metric('납 측정수치', after_pb, f'{delta} ng/m\u00B3')

        # 칼슘 성분 metric
        df_rh02_ca = data[data['ITEMCODE'] == '90319']
        after_ca = df_rh02_ca[df_rh02_ca['STATIONCODE'] == station_code].iloc[-1]['VALUE']
        before_ca = df_rh02_ca[df_rh02_ca['STATIONCODE'] == station_code].iloc[-2]['VALUE']
        delta = round(after_ca -before_ca , 4)
        container.metric('칼슘 측정수치', after_ca, f'{delta} ng/m\u00B3')
        container.page_link('pages/station1.py', label='상세페이지', use_container_width=True)
    except IndexError:
        container.write(f'{station[station_code]}에 해당하는 데이터가 없습니다.')
