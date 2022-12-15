import requests
import re
from lxml import etree  # 数据抽取
import xlwt

# 爬取的网站
url = "http://www.ttpaihang.com/vote/rankresult-1501.html"
# 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.17 Safari/537.36'
}
# ip代理
# ip_url = '183.230.179.164:8060'
proxies = {'http': '183.230.179.164:8060',
           }

# 爬取网站

req = requests.get(url=url, headers=headers, proxies=proxies)

# 储存为文本，格式转化utf-8
req.encoding = 'gbk'
# 以str格式
text = req.text

# 解析网页
html = etree.HTML(text)
# 抽取 tr 树形
trs = html.xpath('//tr[@bgcolor="#FFFEE1"]')[0]
# 遍历法
for tr in trs:
    text = (etree.tostring(tr, encoding='utf8').decode('utf8'))

Proportion = re.findall('<div align="center">(.*)</div>', text)  # ['名次', '得票占比', '人气占比']

number = re.findall('<td width="10%"><div align="right">(.*)</div></td>', text)

renqi = re.findall('<td width="12%"><div align="right">(.*)</div></td>', text)

# print(Proportion[0])
# print(Proportion[1])
# print(number[0])
# print(renqi[0])

# 抽取名次 列表
Ranking_re = ' <td height="30"><font color="#FF0000">(.*)</font>、<a href="(.*)" target="_blank">(.*)</a></td>'
name_top = []
Rankings = re.findall(Ranking_re, text)
for Ranking in Rankings:
    name_top.append(Ranking)
print(name_top)

# 抽取得票 列表
get_ticket_re = '<td width="10%"><div align="right">(.*)</div></td>'
get_ticket = re.findall(get_ticket_re, text)
print(get_ticket)

# 抽取人气值
popularity_re = ' <td width="12%"><div align="right">(.*)</div></td>'
get_popularity = re.findall(popularity_re, text)
print(get_popularity)

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('国产二次元女神排行榜', cell_overwrite_ok=True)
sheet.write(0, 0, '排名')
sheet.write(0, 1, Proportion[0])
sheet.write(0, 2, Proportion[1])
sheet.write(0, 5, "图片网址")
for row in range(0, 1217):
    sheet.write(row + 1, 0, str(name_top[row][0]))
    sheet.write(row + 1, 1, str(name_top[row][2]))
    sheet.write(row + 1, 2, str(number[row * 2 + 1]))
    sheet.write(row, 3, str(number[row * 2]))
    sheet.write(row, 4, str(renqi[row]))
    sheet.write(row + 1, 0, str(name_top[row][1]))
    # break

book.save('./hh.xls')
print('写入文件成功！')
