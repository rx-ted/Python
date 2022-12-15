import requests
import json

def handle_requests(url, data):
    # 协议头定义
    headers = {
        'client': '4',
        'version': '6955.6',
        'device': 'MuMu',
        'imei':'980000000025308',
        "channel": "qqkp",
        "resolution": "1440*810",
        "dpi": "1.6875",
        "brand": "Android",
        "scale": "1.6875",
        "timezone": "28800",
        "language": "zh",
        "cns": "3",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36",
        'newbie': '1',
        'reach': '1',
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "Host": "api.douguo.net",
    }
    response = requests.post(url=url, headers=headers, data=data)
    return response


def heandle_index():
    # 豆果美食网址
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    # url = 'http:www.douguo.com/search?key=5o6S6aqo&_vs=400'
    data = {
        'client': '4',
        '_vs': '2305',
    }
    response = handle_requests(url=url, data=data)
    print(response.text)
    # index_response_dict =json.loads(response.text)
    # for index_item in index_response_dict['result']['cs']:
    #     # print(index_item)
    #     for index_item_1 in index_item['cs']:
    #         # print(index_item_1)
    #         for item in index_item_1['cs']:
    #             print(item)



heandle_index()
