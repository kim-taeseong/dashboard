import pandas as pd

def make_data_frame(data):
    '''
    data(api 호출 결과로 만든 리스트(딕셔너리가 포함되어 있음))로 data frame을 만드는 함수

    날짜 : 시간만 표시
    itemcode : 90303, 90319 <- api 문서에 있는 코드, 그 이외의 코드는 확인 필요
    timecode : rh02 -> 2시간 평균값

    매개변수
    data(list): api 호출 결과로 만든 리스트(딕셔너리가 포함되어 있음)

    return
    DataFrame
    '''
    df = pd.DataFrame(data)
    df['SDATE'] = df['SDATE'].apply(lambda x: x[8:10])
    df_rh02 = df[df['TIMECODE'] == 'RH02']
    
    return df_rh02