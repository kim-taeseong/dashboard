import requests, json, os

from dotenv import load_dotenv
from datetime import date

station = {
    1: '수도권',
    2: '백령도',
    3: '호남권',
    4: '중부권',
    5: '제주도',
    6: '영남권',
    7: '경기권',
    8: '충청권',
    9: '전북권',
    10: '강원권',
    11: '충북권'
}

# item code 딕셔너리
item_code = {
    '90303': '납',
    '90304': '니켈',
    '90305': '망간',
    '90314': '아연',
    '90319': '칼슘',
    '90318': '칼륨',
    '90325': '황'
}

load_dotenv()

def get_api_data(input_date=date.today().strftime('%Y%m%d')):
    api_key = os.getenv('API_KEY')
    
    url = 'http://apis.data.go.kr/1480523/MetalMeasuringResultService/MetalService'

    pageNo = 1

    result = []

    # today = date.today().strftime('%Y%m%d')

    while True:
        params = {
            'ServiceKey': api_key,
            'resultType': 'JSON',
            'date': input_date,
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

    return result