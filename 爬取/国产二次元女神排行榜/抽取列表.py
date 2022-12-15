from lxml import etree  # 数据抽取
import re

with open('./zw.txt', 'r', encoding='utf-8')as f:
    text = f.read()

Proportion = re.findall('<div align="center">(.*)</div>', text)  # ['名次', '得票占比', '人气占比']

number = re.findall('<td width="10%"><div align="right">(.*)</div></td>', text)

renqi = re.findall('<td width="12%"><div align="right">(.*)</div></td>', text)

print(Proportion[0])
print(Proportion[1])
print(number[0])
print(Proportion[2])
print(renqi[0])

# 名次
# 得票占比
# 得票数
# 人气占比
# 人气值