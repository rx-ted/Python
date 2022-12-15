import requests
import time
import re


def init(begin_page, end_page):
    for i in range(begin_page, end_page + 1):
        url = f'https://www.mzitu.com/page/{i}'
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
                'Referer': 'https://www.mzitu.com/'
            }
            response = requests.get(url, headers=headers).text
            print("第%d页" % i)
        # print(response)
            image_info = re.findall("data-original='(.*)' alt='(.*?)'", response)
            for image_url, name in image_info:
                print(image_url, name)
                html = requests.get(image_url, headers=headers).content
            # print(html)
                with open("images/" + name + ".jpg", 'wb')as f:
                # b ：表示二进制,图片、视频、音乐等等
                    f.write(html)
                    f.close()
        # time.sleep(2)
        except:
            return False

if __name__ == '__main__':
    print("网址：https://www.mzitu.com/" + "\n" + "页数从第1页到第229页" + '\n' + "你可以随意输入页数")
    begin_page = int(input("首页："))
    end_page = int(input("末页："))
    init(begin_page, end_page)
