"""
检测　
    １．下载失败或者下载但反应慢，抛出异常
    ２．下载时候，因异常而强制退出下载系统
    ３．下载时候，用户有事或者其他的事而暂停下载，保存在下载进度记录
    ４．下载时候，检查是否安全，下载是否过度，限制下载速度
    ５．初始化友好的界面，最好用ＧＵＩ
    ６．是否可以保存网盘/数据库/硬盘等等
    ７．留下建议框，若有建议就可以输入，方便多了
"""

import os, sys
import requests
from bs4 import BeautifulSoup
import re
from contextlib import closing
import time



class Animation():
    def __init__(self):
        super(Animation, self).__init__()
        self.path = self.build_new_field(self.get_platform())
        # print(self.path) # D:\\Pics\\Animation\\
        self.Source_name()

    def get_platform(self):
        if sys.platform == 'win32':
            path = 'D:\\Pics\\Animation\\'
            return path
        elif sys.platform == 'linux':
            path = os.environ['HOME'] + '/Pics/Animation/'
            return path
        else:
            return None

    def build_new_field(self, new_field_path):
        # 创建文件夹
        # 判断结果
        # print(new_field_path)
        if not os.path.exists(new_field_path):
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(new_field_path)  # 连续创建，若父不在，则创建
            print(new_field_path + ' 创建成功')
            return new_field_path
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(new_field_path + ' 目录已存在')
            return new_field_path

    def Source_name(self):
        print('''由于自己的能力不足，\n被限制只搜索第一页，\n以后等自己能力提升，\n回来时继续优化代码。''')
        name = input("请输入你想要搜索的名字：")
        if name == 'exit' or name == '退出' or name == '0':
            print('你正在退出中……')
            time.sleep(2)
            exit(0)
        # post
        url = 'https://www.dmzj.com/dynamic/o_search/index'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
            'Host': 'www.dmzj.com',
            'Origin': 'https://www.dmzj.com'
        }
        data = {
            'keywords': name
        }
        try:
            response = requests.post(url=url, data=data, headers=headers,verify=False)

        except requests.exceptions.SSLError as e :
            requests.get('http://www.dmzj.com')
        else:
            if response.status_code == 200:
                self.source_right_name(response.text)
            else:
                print(response.status_code)

    def source_right_name(self, html):
        soup = BeautifulSoup(html, 'lxml')
        tab_con = soup.find('div', 'tab-con autoHeight')
        # print(tab_con)
        update_con = tab_con.find_all('a')
        # print(update_con)
        self.Tabs = []
        for i in update_con:
            title = i.get('title')
            href = i.get('href')
            if href[:6] != 'https:':
                href = 'https:' + href
            # print(title,href)
            if title != None and href != None:
                self.Tabs.append(title)
                self.Tabs.append(href)
            else:
                break
        #
        # print(self.Tabs)
        self.chose_Name_searched(self.Tabs)
        pass

    # 被搜索的名字，选择
    def chose_Name_searched(self, tabs):
        for i in range(0, int(len(tabs) / 4)):
            print("第{}个名字是:{},传送(想看请点击或者复制上网):{}".format(i + 1, tabs[4 * i], tabs[4 * i + 1]))
        num = int(input('请输入序号:'))
        while True:
            if num <= len(tabs) / 4 and num > 0:
                name = tabs[4 * (num - 1)]
                href = tabs[4 * (num - 1) + 1]
                self.get_info(href, name)
                break
            elif num == 0:
                print('你正在退出中……')
                time.sleep(2)
                exit(0)
            else:
                print("超过序号或者输入字符串错误，请输入对应序号！")

    def get_info(self, url, save_dir):
        headers = {
            'Host': 'www.dmzj.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36'
        }
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        list_con_li = soup.find('ul', 'list_con_li autoHeight')
        # print(list_con_li)
        comic_list = list_con_li.find_all('a')
        Directory = []  # 目录
        for li in comic_list:
            title = li.get('title')
            Directory.append(title)
            href = li.get('href')
            Directory.append(href)
        # print(Directory)

        self.get_iamges(Directory, save_dir)

    def get_iamges(self, Directory, save_dir):
        for i in range(0, int(len(Directory) / 2)):
            title = Directory[2 * i]
            # 创建目录标题
            D_path = self.build_new_field(self.path + save_dir) + '\\'
            if not os.path.exists(D_path + title):
                os.mkdir(D_path + title)
            # print(D_path+title)
            href = Directory[2 * i + 1]

            headers = {
                # 'Host': 'www.dmzj.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36'
            }
            r = requests.get(url=href, headers=headers).text
            html = BeautifulSoup(r, 'lxml')
            script_info = html.script
            # print(script_info)
            pics_number = re.findall('\d{13,14}', str(script_info))
            N4 = re.findall('\|(\d{4})\|', str(script_info))
            N5 = re.findall('\|(\d{5})\|', str(script_info))
            # print(pics_number)
            # print(N5)
            # print(N4)
            # 拼接法
            for pic in pics_number:
                spell_url = 'https://images.dmzj.com/img/' + 'chapterpic' + '/' + N4[0] + '/' + N5[
                    0] + '/' + pic + '.jpg'
                self.down_img(spell_url, pic, title, href, D_path + title)
            # time.sleep(3)

    def down_img(self, img_url, num, title, href, path):
        # print(title,img_url,num)

        down_header = {
            'Referer': href,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36'

        }
        time.sleep(5)
        try:
            with closing(requests.get(url=img_url, headers=down_header, stream=True, verify=False)) as reponse:
                chunk_size = 1024
                content_size = int(reponse.headers['content-length'])

                if reponse.status_code == 200:
                    print('文件大小：%.2f KB ' % (content_size / chunk_size))
                    with open('{0}\\{1}.jpg'.format(path, num), 'wb')as f:
                        for data in reponse.iter_content(chunk_size=chunk_size):
                            f.write(data)
                else:
                    print('链接异常')
            print('下载完成')
        except requests.exceptions.SSLError as e:
            print(e)


if __name__ == '__main__':
    A = Animation()
