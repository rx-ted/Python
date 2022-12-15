import requests
import json
from urllib import parse


def get_headers(url, data):
    headers = {
        'client': '4',
        'version': '6955.6',
        'device': 'MuMu',
        'imei': '980000000025308',
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


def get_data():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        'client': '4',
        # '_session': '1578116907341980000000025308',
        # 'v': '1578114910',
        '_vs': '2305',
        # 'sign_ran': 'c4ffd37e4efb04d52e62ba2ae502c774',
        # 'code': '5bfd5f4e928324a5',
    }
    response = get_headers(url=url, data=data)
    # print(response.text)
    names = []
    jus = []
    menu_item_dict = json.loads(response.text)
    for menu_item1 in menu_item_dict['result']['cs']:
        for menu_item2 in menu_item1['cs']:
            for menu_item3 in menu_item2['cs']:
                name = menu_item3.get('name')
                ju = menu_item3.get('ju')
                jus.append(ju)
                names.append(name)
    print(str(names) + '\n' + str(jus))
    search_first_url = 'http://www.douguo.com/search?key='
    search_end_url = '&_vs=400'
    for name in names:
        decode_name = parse.quote(name)
        search_url = search_first_url+decode_name+search_end_url
        # print(search_url)
        res = requests.get(url=search_url,data=data).text
        print(res)
        break


get_data()
