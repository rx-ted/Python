import requests


headers = {
    'Referer': 'https://www.mzitu.com/192348',

    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'

}
url2 = int(input("输入最大的数字:  "))
url1 = input("除去后6位的网址:")

url3 = '.jpg'
for x in range(1, url2+1):
    x = str(x)
    i = (x.zfill(2))
    print(i)
    url = url1+i+url3
    response = requests.get(url, headers=headers).content
    # print(response.content)

    with open(f'images/{i}.jpg', 'wb')as f:
        f.write(response)
        f.close()

