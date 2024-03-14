import requests, json

api_key = 'r/I00lQI9L3oTZvdhYAQm7SxmEKhZxI9Fh0TOw6YANaLq7xNj8yGaoywgeFrmnM/peR1xDdHPv/xaib38ges6w=='

url = 'http://apis.data.go.kr/1480523/MetalMeasuringResultService/MetalService'

pageNo = 1

result = []

while True:
    params = {
        'ServiceKey': api_key,
        'resultType': 'JSON',
        'date': '20230314',
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

print(result)