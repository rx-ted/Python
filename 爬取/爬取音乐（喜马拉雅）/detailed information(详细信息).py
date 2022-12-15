import requests
url = "https://www.ximalaya.com/revision/play/album?albumId=19349717&pageNum=1&sort=1&pageSize=30"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400",
    # 变化的
    "xm-sign": "7276fef4aa82b13932deb79be68e9090(63)1565163216317(30)1565163217012"
    # 上面的  链接网址https://www.ximalaya.com/        寻找getCurenntUser  然后xm-sign后面复制到上面
        }

response = requests.get(url, headers=header).json()

print(requests)

