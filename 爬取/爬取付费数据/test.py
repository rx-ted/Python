import requests
from lxml import etree
headers = {"User-Agent": "Mozilla/5.0 (Windows NT10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko))"}
# 1.请求包图网拿到html数据
response = requests.get("https://v.qq.com/?ptag=qqbsc/", headers=headers)
# print(response.text)
# 2.抽取想要数据 视频标题 视频链接
html = etree.HTML(response.text)    # 整理文档对象
tit_list = html.xpath('//span[@class="figure_detail figure_detail_two_row "]/text()')
src_list = html.xpath('//div[@class="video-play"]/video/@src')
print(tit_list, src_list)
'''
for tit, src in zip(tit_list, src_list):
    # 3.下载视频
    content = requests.get("https:" + src).content

    # 4.保存视频
    file_name = "video\\" + tit + ".mp4"
    print("[INFO]:正在保存文件" + file_name)
    with open(file_name, "wb") as f:
        f.write(content)
'''

