import requests
from bs4 import BeautifulSoup
import re
import json
from lxml import etree
import os

# 获取数据
def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4021.2 Safari/537.36',
        'Host': 'zhainanba.net'
    }
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        print("200! success get a url!")
        return resp
    else:
        return False


# 提取数据
def parse_url():
    zhainan_url = 'http://zhainanba.net/'
    rep = get_url(url=zhainan_url).text
    # print(rep)
    #     soup = BeautifulSoup(rep, 'lxml')
    #     div = soup.select('body > section > div > div > div.most-comment-posts')
    #     for list1 in div:
    #         ul = list1.find(name='ul')
    #         for list2 in ul:
    #             # li = list2.find(name='p')
    #             string = '''
    #             <li><p class="text-muted"><a class="post-like" data-event="like" data-pid=".*" href="javascript:;"><i class="glyphicon glyphicon-thumbs-up"></i>赞 (<span>(.*)</span>)</a></p><span class=".*">.*</span><a href="(.*)" target="_blank" title="(.*)">.*</a></li>
    # '''
    #             # data = re.findall(string,str(list2))
    html = etree.HTML((rep))
    lis = html.xpath("/html/body/section/div/div/div/ul/li")
    li = []
    for list in lis:
        # span = list.get('span')
        # print(list)
        li.append(etree.tostring(list, encoding='utf8').decode('utf8'))   
    print('success to spider !')

    # 创建文件
    path = 'd:\data'
    filename = 'info.txt'
    file_path=path+'\\'+filename
    if not os.path.exists(path):
        os.makedirs(path)
    text = 'cd {} && type nul> {}'.format(path,filename)
    os.system(str(text))
    # 写入文件
    with open (file_path,mode='w',encoding='utf-8')as f:
        f.write(str(li))
        f.close()
        print('success to write !')

# 解析数据
def Parse_data():
    with open('d:\data\info.txt','r',encoding='utf-8')as f:
        data = f.read()
        print(data)
        span = re.findall('<span>(\d+)<\/span>',data)
        ref = re.findall(r'(href="http:\/\/zhainanba.net\/\d+.html")',data)
        title = re.findall('href="http:\/\/zhainanba.net\/\d+.html" title="(.*)">.*</a></li>\'',data)
        
        print(title)




if __name__ == "__main__":
    # parse_url()
    Parse_data()