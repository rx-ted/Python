from fake_useragent import UserAgent
import requests


class Spider():

    # 定义参数（不可改变的）
    def Useragent(self):
        UA = UserAgent()
        header = {
            'User-Agent': UA.random,
        }
        return header

    # 访问网络
    def getUrl(self, url):
        # print(url, Spider.Useragent(self))
        response = requests.get(url=url, headers=Spider.Useragent(self))
        if not response.status_code == 200:
            return 404
            pass
        return response.content.decode('utf-8')


# if __name__ == '__main__':
#     s = Spider()
#     s.get_html()
