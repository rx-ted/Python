import urllib.request
import requests
from bs4 import BeautifulSoup
import xlwt

main_url = 'https://home.meishichina.com/recipe.html'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"
}
url = urllib.request.Request(url=main_url, headers=headers)
proxies = {"http": "183.230.179.164:8060"}

#

# def get_data():
hander = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(hander)
resp = opener.open(url)
html = resp.read().decode('utf-8')
# with open('./fine_food.txt', 'w', encoding='utf-8')as fp:
#     fp.write(html)


#
# res = requests.get(main_url,headers=headers)
# print(res)

# def read_data():
# with open('./fine_food.txt', 'r', encoding='utf-8')as fp:
#     html = fp.read()

soup = BeautifulSoup(html, 'lxml')

content = soup.select('#recipeindex_living > ul.on > li > a')

links = []
titles = []

for n in content:
    link = n.get('href')
    title = n.get('title')
    links.append(link)
    titles.append(title)
    # print(n)
# print(titles)
# print(links)
'''
links = ['https://home.meishichina.com/recipe-493694.html', 'https://home.meishichina.com/space-11984358.html',]
title = ['玫瑰花雪耳糖水', '黎明GIgi']
'''
# print(len(links))
# print(len(titles))

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('最新推荐', cell_overwrite_ok=True)
sheet.write(0, 0, 'ID')
sheet.write(0, 1, 'homepage_name')
sheet.write(0, 2, 'homepage')
sheet.write(0, 3, "menu")
sheet.write(0, 4, 'menu_home_url')
for i in range(0, int(len(titles) / 2)):
    sheet.write(i + 1 + 1, 0, i)
    sheet.write(i + 1, 1, titles[i * 2])
    sheet.write(i + 1, 2, links[i * 2])
    sheet.write(i + 1, 3, titles[i * 2 - 1])
    sheet.write(i + 1, 4, links[i * 2 - 1])
#
book.save('./美食天下_最新推荐.xls')
print('写入文件成功！')
