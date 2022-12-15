# 爬取图片
import requests
import csv
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"
}
with open('../files/wzly.csv', encoding='utf-8')as f:  # 读取csv数据链接
    reader = csv.DictReader(f)
    for r in reader:
        # r :每一行数据
        print(r['username'])
        try:
            response = requests.get(r['avatar'], headers=headers)  # 下载图片
            #   r['avatar']:表示图片的链接
            # png：rgba  jpg ：rgb
            with open(f'../images/{r["username"]}.png', 'wb')as f1:  # 保存图片
                f1.write(response.content)  # 把图片数据写入到文件里面去
        except:
            pass
