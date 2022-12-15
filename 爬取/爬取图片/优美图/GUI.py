import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
import time
import os
import random
import requests
from lxml import etree

'''
 python -m PyQt5.uic.pyuic 下载器.ui -o 下载器.py
'''
class UI(QWidget):
    def GetMainurl(self):
        pass

    # 创建文件夹
    def Build_new_field(new_field_path):
        #     # 创建文件夹
        isExists = os.path.exists(new_field_path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(new_field_path)
            print(new_field_path + ' 创建成功')
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(new_field_path + ' 目录已存在')

    # 不可改的参数
    def Parameter(self):
        # 目标网址
        self.url = 'http://m.umei.cc/tags/'
        # 请求头
        '''
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
        '''
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_19d597dda6fff717a20d276fa907bd17=1579874963,1579962492; Hm_lpvt_19d597dda6fff717a20d276fa907bd17=1579964664',
            'Host': 'm.umei.cc',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'
        }
        self.urlHead = 'http://m.umei.cc/'
        self.saveField_path = 'd:\\data'  # 要保存文件夹位置

    def Geturl_data(self):
        # 得到网页数据
        response = requests.get(self.url, headers=self.headers).content.decode('utf-8')
        # 用lxml进行提取数据
        html = etree.HTML(response)
        lis = html.xpath('/html/body/div[4]/div/a')
        for li in lis:
            href = li.get('href')
            title = li.get('title')
            print(href, title)
            spelling_url = self.urlHead + href  # 拼写网址头+爬取href等于完整网址
            print(spelling_url)

    def Start(self):
        # print('开始使用')
        self.Geturl_data()

    def Stop(self):
        print("停止功能")

    # 恢复功能
    def Recove(self):
        print('继续使用|恢复使用')

    # 暂停功能
    def Suspend(self):
        # os.system('pause')
        print("暂停功能")

    def Exit(self):
        reply = QMessageBox.question(self, 'Quit', 'Do you save this data? Convenient to continue to use next time.',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            with open('d:\\data\\1.txt', 'w')as f:
                f.write("jiaohuxhui")
            sys.exit(app.exec_())
            # From.accept()
            # From.close()
        else:
            # From.ignore()
            # From.close()
            sys.exit(app.exec_())

    def initUI(self, From):
        self.layoutWidget = QtWidgets.QWidget(From)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 70, 500, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 开始按钮
        self.start = QtWidgets.QPushButton(self.layoutWidget)
        self.start.setObjectName("start")
        # 按钮被触发事件
        self.start.clicked.connect(self.Start)
        self.horizontalLayout.addWidget(self.start)
        # 恢复按钮
        self.recove = QtWidgets.QPushButton(self.layoutWidget)
        self.recove.setObjectName("recove")
        self.recove.clicked.connect(self.Recove)
        self.horizontalLayout.addWidget(self.recove)
        # 暂停按钮
        self.suspend = QtWidgets.QPushButton(self.layoutWidget)
        self.suspend.setObjectName("suspend")
        self.suspend.clicked.connect(self.Suspend)
        self.horizontalLayout.addWidget(self.suspend)
        # 停止/终止按钮
        self.stop = QtWidgets.QPushButton(self.layoutWidget)
        self.stop.setObjectName("stop")
        self.stop.clicked.connect(self.Stop)
        self.horizontalLayout.addWidget(self.stop)

        # 退出按钮
        self.exit = QtWidgets.QPushButton(self.layoutWidget)
        self.exit.setObjectName("exit")
        # self.exit.clicked.connect(From.close)
        self.exit.clicked.connect(self.Exit)

        self.horizontalLayout.addWidget(self.exit)

        # 进度标签
        self.label = QtWidgets.QLabel(From)
        self.label.setGeometry(QtCore.QRect(30, 130, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("进度")

        # 下载进度
        self.schedule = QtWidgets.QProgressBar(From)
        self.schedule.setGeometry(QtCore.QRect(80, 130, 540, 20))
        self.schedule.setProperty("value", 90)
        self.schedule.setObjectName("schedule")
        # read_list
        self.label_1 = QtWidgets.QListWidget(From)
        self.label_1.setGeometry(QtCore.QRect(80, 170, 540, 300))
        # self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setObjectName("read_list")
        # 记录
        self.label_2 = QtWidgets.QLabel(From)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("记录")
        # 标题
        self.title = QtWidgets.QLabel(From)
        self.title.setGeometry(QtCore.QRect(200, 20, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("爬取图片下载器")

        self.retranslateUi(From)
        QtCore.QMetaObject.connectSlotsByName(From)
        time.sleep(0.2)
        # self.show()

    def retranslateUi(self, Form):
        # 窗口标题
        # self.setWindowTitle("爬取图片下载器")
        # 创造界面
        From.setObjectName('From')
        From.centralWidget = QtWidgets.QWidget(From)
        # 窗口大小
        From.resize(640, 480)
        # 不可最大化
        From.setMinimumSize(QtCore.QSize(640, 480))
        _translate = QtCore.QCoreApplication.translate
        From.setWindowIcon(QIcon('icon.ico'))
        Form.setWindowTitle(_translate("Form", "爬取图片下载器"))
        self.start.setText(_translate("Form", "开始"))
        self.recove.setText(_translate("Form", "恢复"))
        self.suspend.setText(_translate("Form", "暂停"))
        self.stop.setText(_translate("Form", "终止"))
        self.exit.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "进度"))
        # self.label_1.setText(_translate("Form", "列表"))
        self.label_2.setText(_translate("Form", "记录"))
        self.title.setText(_translate("Form", "爬取图片下载器"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    From = QtWidgets.QMainWindow()
    ui = UI()
    ui.initUI(From)
    From.show()
    sys.exit(app.exec_())
