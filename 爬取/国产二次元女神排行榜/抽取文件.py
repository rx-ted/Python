
from lxml import etree  # 数据抽取
with open('./ns.txt', 'r', encoding='utf-8')as f:
    text = f.read()

# html = BeautifulSoup(text)
html1 = etree.HTML(text)

# table = html.select('table')
trs = html1.xpath('//tr[@bgcolor="#FFFEE1"]')[0]
for tr in trs:
    text = ((etree.tostring(tr, encoding='utf8').decode('utf8')))
    break

with open('zw.txt', 'w', encoding='utf-8')as f:
    f.write(text)

'''
/html/body/table[1]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]


'''