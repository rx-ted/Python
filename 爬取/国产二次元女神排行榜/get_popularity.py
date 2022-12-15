import re

with open('./zw.txt', 'r', encoding='utf-8')as f:
    text = f.read()


popularity_re = ' <td width="12%"><div align="right">(.*)</div></td>'
get_popularity = re.findall(popularity_re, text)
print(get_popularity)
