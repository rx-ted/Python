from urllib import request
from urllib import parse

# url = 'https://www.lagou.com/'
url = 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=pachon'

headers = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=pachon',
}

from_data = {
    'first': 'true',
    'pn': '1',
    'kd': '爬虫',
}

query_data = {
    'jd': '未融资',  #
    'hy': '电商',  #
    'px': 'default',
    'gx': '全职',
    'gm': '15-50人,500-2000人',
    'city': '北京',
    'needAddtionalResult': 'false',
    'isSchoolJob': '1',
}

px = request.ProxyHandler({'http': '60.167.113.79:9999'})
opener = request.build_opener(px)

resp = request.Request(url=url, headers=headers, data=parse.urlencode(from_data).encode('utf-8'), method='post')
# rep = request.urlopen(resp,timeout=2)
rep = opener.open(resp)
print(rep.read().decode('utf-8'))
