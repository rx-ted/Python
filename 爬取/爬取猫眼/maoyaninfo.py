# 网络请求包
import requests
# 网页选择器 筛选数据的
from bs4 import BeautifulSoup
# 数据以字典的格式存储到文件中 python对象不支持文件写入
import json
# from excel_write import  save_to_excel
import xlwt

# 猫眼网址
# url = 'https://maoyan.com/board/4?offset='

# 定义游览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}


# 去获取数据
def getPage(url):
    # 异常处理 可以避免因为网络导致程序报错崩溃
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None


# 获取电影信息
def getInfo(html):
    # 使用BeautifulSoup()获取电影名、放映时间、评分、主演、排行
    soup = BeautifulSoup(html, 'lxml')

    # 筛选
    items = soup.select('dd')

    for item in items:
        index = item.find(name='i', class_='board-index').get_text()
        name = item.find(name='p', class_='name').get_text()
        star = item.find(name='p',class_='star').get_text().strip()[3:]
        releasetime = item.find(name='p', class_='releasetime').get_text()
        score = item.find(name='p',class_='score').get_text()

        # 返回数据
        yield {
            "排名": index,
            "电影名": name,
            "主演": star,
            "放映时间": releasetime,
            "评分": score
        }

    # print(items)


def writedata(file):
    # 文件处理
    with open('manyan_info.txt', 'a', encoding='utf-8')as f:
        f.write(json.dumps(file, ensure_ascii=False)+'\n')



def save_to_excel(doc_save_path, sheet_name, data):
    f = xlwt.Workbook()
    sheet = f.add_sheet(sheet_name, cell_overwrite_ok=True)
    for row, row_data in enumerate(data):
        for column, column_data in enumerate(row_data):
            sheet.write(row, column, str(column_data))
    f.save(doc_save_path+".xls")

# save_to_excel(item)

#函数入口
if __name__ == '__main__':
    for i in range(0, 101, 10):
        url = f'https://maoyan.com/board/4?offset={i}'
        html = getPage(url)

        for item in getInfo(html):
            print(item)
            writedata(item)
            save_to_excel("猫眼信息", "信息1", item)

