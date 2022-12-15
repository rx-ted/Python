import re

with open('./zw.txt', 'r', encoding='utf-8')as f:
    text = f.read()

get_ticket_re = '<td width="10%"><div align="right">(.*)</div></td>'

get_ticket = re.findall(get_ticket_re, text)

print(get_ticket)