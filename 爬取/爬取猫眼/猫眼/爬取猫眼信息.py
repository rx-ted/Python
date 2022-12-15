import requests
from bs4 import BeautifulSoup
import struct
import json
url = "https://maoyan.com/board/4?offset="

hearers = {
    "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.25Safari / 537.36Core / 1.70.3704.400QQBrowser / 10.4.3587.400"
}


response = requests.get(url, params=hearers).text




soup = BeautifulSoup(response, 'lxml')
items = soup.select('dd')
for item in items:
    a = items
for y in a:
    print(y)


