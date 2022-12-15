from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import requests
import json
mpl.rcParams['font.family']='STFangsong'
labels = ["9.5+分", "9.0-9.5分", "8.5-9.0分", "8.0-8.5分", "8.0-分"]
fracs = [14, 80, 271, 274, 183]
plt.pie(fracs, labels=labels, autopct='%.0f%%')
plt.show()

for i in range(0, 100, 10):
    url = 'https://maoyan.com/board/4?offset=%d'%i
# https://jn.58.com/shouji/?PGTID=0d100000-0010-9734-6caa-ad87876744&ClickID=1
# response = requests.get(url, params=None).text
    web_data = requests.get(url, params=None).text

    #response = BaseException(web_data, 'lxml')

    # print(web_data)
    _web = BeautifulSoup(web_data, 'lxml')
    infos = _web.select('dd')
    items = _web.select('#app > div > div > div.main > dl > dd:nth-child(1) > div > div > div.movie-item-info > p.name')
    releasetimes = _web.select('#app > div > div > div.main > dl > dd:nth-child(1) > div > div > div.movie-item-info > p.releasetime')
    scores = _web.select('#app > div > div > div.main > dl > dd:nth-child(1) > div > div > div.movie-item-number.score-num > p')


# #app > div > div > div.main > dl > dd:nth-child(1) > div > div > div.movie-item-info > p.name > a
# time = _web.select('#app > div > div > div.main > dl > dd:nth-child(1) > div > div > div.movie-item-info > p.releasetime')



    for item,releasetime,score in zip(items,releasetimes,scores):
        data = {
            # 'board-index board-index-1': scores.get_text(),
            # 电影名
            'title': item.get_text().strip().split(),
            # 放映时间
            'releasetime': releasetime.get_text().strip().split(),
            # 评分
            'score': score.get_text()
        }
        # 整理一下
        # 依次获取每个元素。
        for maoyan_info in data:
                maoyan_info = str(data)
                print("猫眼信息：", maoyan_info)


