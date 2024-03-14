import requests, json
import pandas as pd
import streamlit as st


api_key = 'r/I00lQI9L3oTZvdhYAQm7SxmEKhZxI9Fh0TOw6YANaLq7xNj8yGaoywgeFrmnM/peR1xDdHPv/xaib38ges6w=='

url = 'http://apis.data.go.kr/1480523/MetalMeasuringResultService/MetalService'

pageNo = 1

result = []

while True:
    params = {
        'ServiceKey': api_key,
        'resultType': 'JSON',
        'date': '20240314',
        'numOfRows': 1000,
        'pageNo': pageNo,
        # 'timecode': 'RH24'
    }
    response = requests.get(url, params=params)
    json_response = json.loads(response.text)
    result += json_response['MetalService']['item']

    if  pageNo * 1000 >= json_response['MetalService']['totalCount']:
        break

    pageNo += 1

# print(result)

df = pd.DataFrame(result)
df['SDATE'] = df['SDATE'].apply(lambda x: x[8:10])
df = df[df['ITEMCODE'].isin(['90303', '90319'])]
df_rh02 = df[df['TIMECODE'] == 'RH02']

print(df_rh02)
df_rh02_pb = df_rh02[df_rh02['ITEMCODE'] == '90303']
delta = round(df_rh02_pb[df_rh02_pb['STATIONCODE'] == 1].iloc[-1]['VALUE'] - df_rh02_pb[df_rh02_pb['STATIONCODE'] == 1].iloc[-2]['VALUE'], 4)
st.metric('납 측정수치', df_rh02_pb[df_rh02_pb['STATIONCODE'] == 1].iloc[-1]['VALUE'], f'{delta} ng/m\u00B3')

df_rh02_ca = df_rh02[df_rh02['ITEMCODE'] == '90319']
delta = round(df_rh02_ca[df_rh02_ca['STATIONCODE'] == 1].iloc[-1]['VALUE'] - df_rh02_ca[df_rh02_ca['STATIONCODE'] == 1].iloc[-2]['VALUE'], 4)
st.metric('칼슘 측정수치', df_rh02_ca[df_rh02_ca['STATIONCODE'] == 1].iloc[-1]['VALUE'], f'{delta} ng/m\u00B3')