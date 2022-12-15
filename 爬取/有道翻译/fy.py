import urllib
import urllib.request
from urllib import parse
from urllib.request import urlopen
import re

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule '

headers = {
    "Host": " fanyi.youdao.com",
    # "Connection":" keep-alive"
    # "Content-Length":" 239"
    "Accept": " application/json, text/javascript, */*; q=0.01",
    # "Origin":" http://fanyi.youdao.com"
    "X-Requested-With": " XMLHttpRequest",
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3759.400",
    "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",

}
print("英文——>中文，却不能互换（中文——>英文）")
print("要求不输入数字！！！否则结果空白"+'\n'+"谢谢配合")
key = input("请输入翻译的字、词、句：")
formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15666123735877",
    "sign": "975f61c20b74a25ceb892744e446dd24",
    "ts": "1566612373587",
    "bv": "ab0bbc00a178252a56d63e303de6c883",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}

data = urllib.parse.urlencode(formdata).encode('utf-8')
request = urllib.request.Request(url, data=data, headers=headers)
response = urllib.request.urlopen(request).read().decode('utf-8')
# print(response)
# y = re.findall(r'"src":(.*?)', response)
z = re.findall('[^\x00-\xff]', response)

for y in z:
    print(y, end='')


'''

'''
