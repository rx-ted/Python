import csv      # 操作CSV数据
import requests     # 负责爬取

# url = 'http://www.7799520.com/api/user/pc/list/search?gender=2&marry=1&page=1'

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"
}
with open('../files/wzly.csv', 'w', encoding='utf-8',newline='')as f:

    header = ['username', 'avatar','birthdayyear', 'city','education', 'gender', 'height','marry', 'monolog', 'monologflag', 'province', 'salary','userid']
    write = csv.DictWriter(f, header)    # 申明头部信息
    write.writeheader()     #写入头部
    for i in range(1, 21):     # 20页*20张图片=400页
        print(f'爬取到第{i}页')
        url = f'http://www.7799520.com/api/user/pc/list/search?gender=2&marry=1&page={i}'    # 要爬取的
        # 插值字符串
        response = requests.get(url, headers=headers)           # 负责请求对面服务器 下载数据>源代码>json
        js = response.json()
        for data in js['data']['list']:
            write.writerow(data)


