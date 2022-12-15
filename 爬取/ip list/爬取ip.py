import requests
import re
from lxml import etree
import time
import os
import urllib3

urllib3.disable_warnings()  # 警告

# 用列表存放有效ip代理
alive_ip = ['http', 'https']


class Getip():
    # 初始
    def initial(self):
        path = os.getcwd()
        with open(path + '\\' + 'ip_list.txt', 'w')as f:
            f.write(' ')
        f.close()

        path = os.getcwd()
        with open(path + '\\' + '国内ip数据.txt', 'a+')as f:
            f.write(' ')
        f.close()

        print("清理文件并初始化成功！")

    # 定义
    def define(self):
        pass

    # 拼写
    def spell_url(self):
        urlHead = 'https://www.xicidaili.com/'
        url_heads = ['nn', 'nt', 'wn', 'wt']
        nn_url = 'https://www.xicidaili.com/nn/'  # 国内高匿代理
        nt_url = 'https://www.xicidaili.com/nt/'  # 国内普通代理
        wn_url = 'https://www.xicidaili.com/wn/'  # 国内https代理
        wt_url = 'https://www.xicidaili.com/wt/'  # 国内http代理
        print('1.国内高匿代理\n2.国内普通代理\n3.国内https代理\n4.国内http代理\n0.退出窗口')
        flag = True
        while flag:
            Number = int(input("请输入对应的序号："))  # 输出str->int
            if Number == 1:
                self.getUrl(nn_url)
                flag = False
            elif Number == 2:
                self.getUrl(nt_url)
                flag = False
            elif Number == 3:
                self.getUrl(nt_url)
                flag = False
            elif Number == 4:
                self.getUrl(wn_url)
                flag = False

            elif Number == 0:
                exit(0)
                flag = True
            else:
                print("输入序号错误，请重新输入！\n")

    def getUrl(self, gurl):
        headers = {
            'Host': 'www.xicidaili.com',
            # 'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRmYWU2MWNjMjBjNTVhMWY4ZWQyNTAwYjVjZmY4ZmI0BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTN4RUlwY2N5ZEVlRUQ3d2l2blFuRVZ1WVlkQ3BXdUFUTUtHWCtSTFpqUGc9BjsARg%3D%3D--a1b03cf9dfc1e99fe65a840119ea38bd0fbe1386; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1583638711,1583663888; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1583666413',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'https://www.xicidaili.com/',
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        my_proxies = {
            'http': 'http://121.239.128.176:8118'
        }
        for i in range(1, 2):
            path = '国内ip数据.txt'
            url = gurl + str(i)
            # print(url)
            text = requests.get(url=url, headers=headers, proxies=my_proxies).text
            for j in range(0, 101):
                html = etree.HTML(text)
                tbodies = html.xpath(f'//*[@id="ip_list"]/tr[{j}]')
                # print(etree.tostring(tbodies, encoding='utf-8').decode('utf-8'))

                for k in tbodies:
                    h = etree.tostring(k, encoding='utf-8').decode('utf-8')
                    # print(h)
                    re_ip = '''<td>(.*)</td>\n.*<td>(.*)</td>\n.*<td>\n.*<a href=".*">(.*)</a>\n.*</td>\n.*<td class="country">.*</td>\n.*<td>(.*)</td>'''
                    lis = re.findall(re_ip, h)
                    if lis:
                        # print(lis)
                        self.write_data(data=lis, mypath=path)  # 写数据
                        self.spell_ip(lis)  # 拼写ip

                    else:
                        pass
            time.sleep(0.5)


    def spell_ip(self, datas):
        for data in datas:
            ip = data[0] + ':' + data[1]
            # print(ip)
            self.test_alive(ip)  # ip是否有效

    def test_alive(self, proxy):

        for i in alive_ip:
            spell_ip = i + '//:' + proxy
            for j in alive_ip:
                proxies = {j: spell_ip}
                # print(proxies)

                r = requests.get('https://www.baidu.com', proxies=proxies, timeout=3, verify=False)
                if r.status_code == 200:
                    print(proxies)
                    self.write_ip(proxies)
                    break
                else:
                    pass

    def write_ip(self, proxy):
        path = os.getcwd()
        with open(path + '\\' + 'ip_list.txt', 'a+')as f:
            f.write(str(proxy) + '\n')
        f.close()

    def write_data(self, data, mypath):
        path = os.getcwd()
        with open(path + '\\' + mypath, 'a+')as f:
            f.write(str(data) + '\n')
        f.close()


if __name__ == '__main__':
    g = Getip()
    g.initial()  # 回到初始值
    g.spell_url()

