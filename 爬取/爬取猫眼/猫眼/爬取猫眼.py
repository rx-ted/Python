
from bs4 import BeautifulSoup
# 网络请求包 它能获取到网站上的前端源代码
import requests
# json 在文件处理中 python没有办法把一个对象写入文件中 字典就是python中的一个对象
import json

# 这种数据结构是一种典型的字典格式
# 作用 定义浏览器
headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}

# 获取请求页面




def getPage(url):
    # 异常处理 保证我们的程序不会因为网络原因导致程序崩溃
    try:
        respose = requests.get(url, headers=headers)
        if requests.status_codes == 200:
            return respose.text
        else:
            return None
    except Exception:
        return None


# 获取电影消息
def getinfo(html1):
    # 使用BeautifulSoup匹配电影的索引 海报 电影名 主演 评分
    soup = BeautifulSoup(html1, 'lxml')
    items = soup.select('dd')

    for item in items:
        index = item.find(name='i', calss_='board-index').get_text()
        name = item.find(name='p', calss_='name').get_text()
        start = item.find(name='p', class_='star').get_text().strip()
        time = item.find(name='p', class_='releasetime').get_text()
        score = item.find(name='p', class_='score').get_text()
    yield {
        '排名': index,
        '电影名称': name,
        '主演': start,
        '上映时间': time,
        '评分': score
    }

# 写入文件
def writedata(fiel):
    # 文件处理
    with open('maoyaninfo.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(fiel, ensure_ascii=False) + '\n')


if __name__ == "__main__":
    for num in [i*10 for i in range(11)]:
        url = "https://maoyan.com/board/4?offset="+str(num)
        html1 = getPage(url)

        for item in getinfo(html1):
            print(item)
            writedata(item)
