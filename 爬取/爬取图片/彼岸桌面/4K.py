import requests
from lxml import etree
import random
import os
import time
import imghdr


def url_status(url, method):
    '''
    User-agent: *
    '''
    # 请求头
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4021.2 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']
    UserAgent = random.choice(user_agent_list)
    headers = {
        'Host': 'pic.netbian.com',
        'User-Agent': UserAgent
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200 and method == 'text':
            response.encoding = 'gbk'
            return response.text
        elif response.status_code == 200 and method == 'content':
            response.encoding = 'gbk'
            return response.content

        elif response.status_code == 400:
            return '网络错误'

        else:
            return '状态码：', response.status_code
    except requests.exceptions.RequestException as e:
        print(e)


def get_url():
    '''
    Disallow: /d/
    Disallow: /e/class/
    Disallow: /e/config/
    Disallow: /e/data/
    Disallow: /e/enews/
    Disallow: /e/update/
    '''
    html = url_status(url=url, method='text')
    # html = etree.HTML(html)
    # tabs = html.xpath('/html/body/div[2]/div[@id="main"]/div[2]/a')
    # print(type(tabs), len(tabs))
    bq0 = ['title', 'href']
    x_path0 = '/html/body/div[2]/div[@id="main"]/div[2]/a'
    get_xpath(html, x_path0, *bq0)
    x_path1 = '/html/body/div[2]/div[@id="main"]/div[3]/ul/li/a'
    get_img(get_xpath(html, x_path1, *bq0))


def get_xpath(Parseurl, Xpath, *bq):
    html0 = etree.HTML(Parseurl)
    get_Data = html0.xpath(Xpath)
    print(type(get_Data), len(get_Data))
    # 自动命名
    auto_name = locals()
    for i in range(0, len(bq)):
        auto_name[bq[i]] = []

    datas = {}
    for i in range(0, len(bq)):
        for li in get_Data:
            if bq[i] == 'href' or bq[i] == 'src':
                auto_name[bq[i]].append(url + li.get('{0}'.format(bq[i])))
            else:
                auto_name[bq[i]].append(li.get('{0}'.format(bq[i])))

    for i in range(0, int(len(auto_name[bq[0]]))):
        datas[auto_name[bq[len(bq) - 2]][i]] = auto_name[bq[len(bq) - 1]][i]
    # print(datas)
    # get_img(datas)
    return datas


def get_img(classify):
    for title, img_url in classify.items():
        # print(title, img_url)
        html = url_status(url=img_url, method='text')
        bq = ['alt', 'src']
        xpath = '//*[@id="img"]/img'
        download_img(get_xpath(html, xpath, *bq))

        # break
    # //*[@id="img"]/img


def download_img(download_url):
    for title, img_url in download_url.items():
        print(title, img_url)

        img_content = url_status(img_url, method='content')
        time.sleep(0.2)
        Filename = '{}{}.jpg'.format(mkdir_folder(path), title)
        try:
            with open(Filename, 'wb')as f:
                f.write(img_content)
        except:
            pass
        code = imghdr.what(Filename)
        print(code)
        if code is None:
            os.remove(Filename)
            print('删除无效的文件:%s' % Filename)
        else:
            print('创建图片成功，标题：%s，图片格式:%s,存储位置：%s' % (title, imghdr.what(Filename), Filename))


def mkdir_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print('创建成功:%s' % folder_path)
        return folder_path

    else:
        print(folder_path + ' 目录已存在')
        return folder_path


# http://pic.netbian.com/downpic.php?id=24695&classid=66
# http://pic.netbian.com/downpic.php?id=25791

if __name__ == '__main__':
    url = 'http://pic.netbian.com'
    path = 'd:/图片/'
    # url_status()
    get_url()
