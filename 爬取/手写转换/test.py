import requests
import json
from lxml import etree
import re

headers = {
    "Age": "0",
    # "Content-Type": "text/html; charset=utf-8",
    "Server": "nginx",
    "Via": "http/1.1 js6-cmcdn1 ( [cMsSf ])",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_1a6016c8e736ecef523fbe2539419b5a=1583817806,1584011262; Hm_lpvt_1a6016c8e736ecef523fbe2539419b5a=1584011262",
    "Host": "www.diyiziti.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

url = 'http://www.diyiziti.com/'


def getting_data():
    data = {
        "FontInfoId": "445",  # 字体
        "FontSize": "20",  # 字号
        "FontColor": "#000000",  # 字体颜色
        "ImageWidth": "570",  # 输出图片宽度
        "ImageHeight": "120",  # 输出图片高度
        "ImageBgColor": "#FFFFFF",  # 设置图片背景
        "Content": "我爱你吗？不，我不认识啊！！！",  # 要输入的字符串
        "ActionCategory": "1",  # 行为类型
    }

    res = requests.post(url=url, json=data).text

    html = etree.HTML(res)
    imgs = html.xpath('//*[@id="imgResult"]')

    # imgs =etree.tostring(lis,encoding='utf-8').decode('utf-8')
    for img in imgs:
        # print(img)
        img_path = img.get('src')
        print(img_path)


# 得到字体
def getting_font():
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        text = res.text
        html = etree.HTML(text)
        lis = html.xpath('//*[@id="FontInfoId"]')[0]
        font = etree.tostring(lis, encoding='utf-8').decode('utf-8')
        font_item = re.findall('<option value="(\d+)">(.*)</option>&#13;', font)
        with open('font.txt', 'w')as fp:
            for item in font_item:
                f = item[0] + ':' + item[1]
                fp.write(f + '\n')
            fp.close()


getting_font()
