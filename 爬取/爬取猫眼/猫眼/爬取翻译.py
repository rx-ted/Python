import requests

url = "https://fanyi.baidu.com/?aldtype=16047#auto/zh/"

header = {
"origin:" "https://fanyi.baidu.com",
"referer:" "https://fanyi.baidu.com/?aldtype=16047"

}

response = requests.get(url, headers=header)
print(response)
 # translate = response[]




