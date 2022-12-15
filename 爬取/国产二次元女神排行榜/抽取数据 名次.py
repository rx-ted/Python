import re

with open('./zw.txt', 'r', encoding='utf-8')as f:
    text = f.read()



Ranking_re = ' <td height="30"><font color="#FF0000">(.*)</font>、<a href="(.*)" target="_blank">(.*)</a></td>'

name_top = []
Rankings = re.findall(Ranking_re, text)
for Ranking in Rankings:
    name_top.append(Ranking)

with open('name_top.txt', 'w', encoding='utf-8')as f:
    f.write(str(name_top))