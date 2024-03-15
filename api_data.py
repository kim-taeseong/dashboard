import requests, json, os

from dotenv import load_dotenv
from datetime import date
load_dotenv()

def get_api_data():
    api_key = os.getenv('API_KEY')
    
    url = 'http://apis.data.go.kr/1480523/MetalMeasuringResultService/MetalService'

    pageNo = 1

    result = []

    today = date.today().strftime('%Y%m%d')

    while True:
        params = {
            'ServiceKey': api_key,
            'resultType': 'JSON',
            'date': today,
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

    return result