import requests
import json
import tkinter
url_head = 'https://nuexini.gq/bdp.php?url='
# http://pan.baidu.com/s/1qWGbSIg
s = input("请输入带有提取码的网盘地址:")

url = url_head+s
# print(type(url))
# 
response = requests.get(url=url).text

print((dict(response)))