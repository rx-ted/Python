'''
http://zkapi.myzaker.com/2019ncov/ncov_local_info_flow_api.php?need_user_info=Y&user_appoint_province=%E6%B1%9F%E8%8B%8F&user_appoint_city=%E5%B8%B8%E5%B7%9E&province_name=%E6%B1%9F%E8%8B%8F&city=%E5%B8%B8%E5%B7%9E
http://huodong.myzaker.com/h/2019ncov/map.php?need_user_info=Y&user_appoint_province=%E6%B1%9F%E8%8B%8F&user_appoint_city=%E5%B8%B8%E5%B7%9E&province_name=%E6%B1%9F%E8%8B%8F&city=%E5%B8%B8%E5%B7%9E
http://zkapi.myzaker.com/2019ncov/ncov_local_info_flow_api.php?need_user_info=Y
http://huodong.myzaker.com/h/2019ncov/map.php?need_user_info=Y
'''

import requests
from urllib.parse import quote
import json
import sys

# if sys.getdefaultencoding() != resp.encoding:            #resp.encoing用于查询网页所采用的编码格式
#     reload(sys)
#     sys.setdefaultencoding(resp.encoding)

url = 'http://zkapi.myzaker.com/2019ncov/ncov_get_position.php?need_user_info=Y&user_appoint_province=&user_appoint_city='
text = requests.get(url=url).text
data = text.encode('utf-8').decode('unicode_escape')
lis = json.loads(data)
s = '安徽'
# province 省份
cities = []
provinces = []
for li in lis['data']['positions_list']:
    provinces.append(li['value'])
    print(li['value'], end=' ')
print('\n')
flag = True
while flag:
    province = input("输入省份：")
    if provinces.count(province):
        print('正确')
        flag = False
    else:
        print('错误')

    for li in lis['data']['positions_list']:
        if province in li['value']:
            print('找到了你输入的省份...')
            print('找到了', len(li['children_list']), '个地点', '\n请选择如下城市中的任何一个:')
            for i in li['children_list']:
                cities.append(i['value'])
                print(i['value'], end=' ')
            print('\n')
        else:
            pass

# print(cities)
flag = True
while flag:
    city = input("输入城市：")
    if cities.count(city):
        print('正确')
        flag = False
    else:
        print('错误')
'''
# url加密
# 拼写url
http://huodong.myzaker.com/2019ncov/ncov_local_info_flow_api.php?need_user_info=Y

http://zkapi.myzaker.com/2019ncov/ncov_local_info_flow_api.php?need_user_info=Y
&user_appoint_province={}&user_appoint_city={}&province_name={}&city={}
'''
# 省份
# print()
# # 城市
# print()
url_news = f'http://zkapi.myzaker.com/2019ncov/ncov_local_info_flow_api.php?need_user_info=Y&user_appoint_province={quote(province)}&user_appoint_city={quote(city)}&province_name={quote(province)}&city={quote(city)}'
proxy = {
    'http': 'https://112.250.107.37:53281'
}
headers = {
    'Connection': 'keep-alive',
    'Content-Encoding': 'gzip',
    'Content-Type': 'text/html; charset=utf-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
}
html = requests.get(url=url_news, headers=headers, proxies=proxy,timeout=5).text
print(html)
