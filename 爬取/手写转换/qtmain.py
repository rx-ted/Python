from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from lxml import etree


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.window()


class font_write():
    # 定义参数
    def define(self):
        self.font_file = 'font.txt'
        self.color_file = 'color.txt'
        self.dial = window.dial  # 滑动字号
        self.lcdNumber = window.lcdNumber  # 显示字号
        self.spinBox = window.spinBox  # 宽度
        self.spinBox_2 = window.spinBox_2  # 高度
        self.comboBox = window.comboBox  # 字体
        self.comboBox_2 = window.comboBox_2  # 字体颜色
        self.comboBox_3 = window.comboBox_3  # 背景颜色
        self.textEdit = window.textEdit  # 输入文本
        # graphicsView = window.graphicsView  # 显示图片
        self.label_11 = window.label_11  # 状态
        self.label_12 = window.label_12  # 显示

    # 初始化
    def initialization(self):


        with open(self.font_file, 'r')as f:
            text = f.readlines()
        f.close()
        for i in text:
            font = i.split(':')[1]
            self.comboBox.addItem(font)

        with open(self.color_file, 'r')as f:
            color = f.readlines()
        f.close()
        for j in color:
            colors = j.split('\t')[2]
            self.comboBox_2.addItem(colors)
            self.comboBox_3.addItem(colors)

        flag = True
        while flag:
            self.dial.valueChanged.connect(self.lcdNumber.display)
            flag = False

    def do_task(self):
        self.getting_data()
        # geturl()
        pass

    # 获取data设置
    def getting_data(self):
        font_color = self.comboBox_2.currentText()
        font = self.comboBox.currentText().strip('\n')
        background_color = self.comboBox_3.currentText()

        # 匹配字体ID
        with open(self.font_file, 'r')as f:
            text = f.readlines()
        f.close()
        for i in text:
            if font in i:
                self.font_id = i.split(':')[0]
            else:
                pass

        # 匹配字体颜色，背景颜色ID

        with open(self.color_file, 'r')as f:
            color = f.readlines()
        f.close()
        for i in color:
            if font_color in i:
                self.font_color_id = i.split('\t')[0]
                # print(self.font_color_id)
            else:
                pass
            if background_color in i:
                self.background_color_id = i.split('\t')[0]
                # print(self.background_color_id)
            else:
                pass
        # 获取文本
        self.string = self.textEdit.toPlainText()

        # 获取宽度高度
        self.width = self.spinBox.value()
        self.height = self.spinBox_2.value()
        # 获取字号
        self.font_size = self.dial.value()

        data = {
            "FontInfoId": self.font_id,  # 字体
            "FontSize": self.font_size,  # 字号
            "FontColor": self.font_color_id,  # 字体颜色
            "ImageWidth": self.width,  # 输出图片宽度
            "ImageHeight": self.height,  # 输出图片高度
            "ImageBgColor": self.background_color_id,  # 设置图片背景
            "Content": self.string,  # 要输入的字符串
            "ActionCategory": "1",  # 行为类型
        }
        self.geturl(data)
        # print(data)

    # 定义，不变
    def geturl(self, d):
        headers = {
            "Age": "0",
            # "Content-Type": "text/html; charset=utf-8",
            "Server": "nginx",
            "Via": "http/1.1 js6-cmcdn1 ( [cMsSf ])",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "Hm_lvt_1a6016c8e736ecef523fbe2539419b5a=1583817806,1584011262; Hm_lpvt_1a6016c8e736ecef523fbe2539419b5a=1584011262",
            "Host": "www.diyiziti.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        }
        url = 'http://www.diyiziti.com/'

        res = requests.post(url=url, json=d, headers=headers)
        if res.status_code == 200:
            # print("200")
            self.get_img(res.text)
        else:
            # print("error")
            self.label_11.setStyleSheet('color:red;')
            self.label_11.setText('网络错误，请稍等重新刷新')
            self.do_task()

    def get_img(self, text):
        proxies = {
            'http': '121.239.128.176:8118'
        }
        html = etree.HTML(text)
        imgs = html.xpath('//*[@id="imgResult"]')
        for img in imgs:
            # print(img)
            img_path = img.get('src')
            img = requests.get(img_path).content
            f = open('test.png', 'wb')
            f.write(img)
            f.close()
            img_byte = QtGui.QPixmap('test.png')
            self.label_12.setPixmap(img_byte)
            self.label_12.setStyleSheet("border: 2px solid red")
            self.label_12.setScaledContents(True)
        self.output()

    def output(self):
        s = '你的选择是\n字体:%s\t字号:%s\n字体颜色:%s\n背景颜色:%s\n输出图片\n宽度:%s\t高度:%s' % (
            self.font_id, self.font_size, self.font_color_id, self.background_color_id, self.width, self.height)
        self.label_11.setText(s)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # 初始化窗口
    window = MainWindow()
    # 数据初始化
    fw = font_write()
    # 显示
    window.show()
    # 按钮事件
    window.pushButton.clicked.connect(lambda: fw.do_task())
    #
    fw.define()
    fw.initialization()
    sys.exit(app.exec_())
