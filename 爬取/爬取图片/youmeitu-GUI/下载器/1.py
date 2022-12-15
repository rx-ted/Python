# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
from lxml import etree
import time
import os


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        MainWindow.setWindowIcon(QtGui.QIcon('main.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 151, 41))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 781, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.progressBar)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 320, 191, 171))
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 180, 103, 24))
        self.label_6.setObjectName("label_6")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(680, 180, 51, 24))
        self.spinBox.setObjectName("spinBox")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(570, 250, 195, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 471, 371))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 520, 395, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # 按钮初始值状态
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        # self.pushButton_3.setEnabled(False)

        self.pushButton_5.clicked.connect(self.pushButton_5_clicked)
        self.pushButton_4.clicked.connect(self.pushButton_4_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "爬取图片下载器"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">爬取图片下载器</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">进度</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">状态</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">变量（491）</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "开始"))
        self.pushButton_3.setText(_translate("MainWindow", "爬取"))
        self.pushButton_2.setText(_translate("MainWindow", "暂停"))
        self.pushButton.setText(_translate("MainWindow", "退出"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">说明</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">左方有文本框，上下滑动，找找</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">自己能否需要爬取。若有，请输</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">入上方序数，然后点击确定，就</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">可以运行爬取。否则点击取消，</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">就可以关闭本窗口。</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "请输入序数： "))
        self.pushButton_5.setText(_translate("MainWindow", "Ok"))
        self.pushButton_6.setText(_translate("MainWindow", "Cannet"))

    # 开始
    def pushButton_4_clicked(self):
        start = QtWidgets.QMessageBox.information(self, '提示', '爬取一些图片: http://m.umei.cc \n是否继续？',
                                                  QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No,
                                                  QtWidgets.QMessageBox.No)
        if start == QtWidgets.QMessageBox.Ok:
            self.Start()
        else:
            pass

    def Start(self):
        urlTags = 'http://m.umei.cc/tags/'
        html = requests.get(url=urlTags).content.decode('utf-8')
        html1 = etree.HTML(html)
        lis = html1.xpath('/html/body/div[4]/div/a')
        url_head = 'http://m.umei.cc'
        self.titles = []
        self.hrefs = []
        while True:
            self.my_path = QtWidgets.QFileDialog.getOpenFileName(self, '获取绝对地址', '/', '文本格式(*.md)')
            if self.my_path[0]:
                try:
                    # 清空
                    with open(self.my_path[0], 'w', encoding='utf-8')as f:
                        f.write('')
                    self.textEdit.append("清空数据成功！")
                    with open(self.my_path[0], 'r', encoding='utf-8')as f:
                        f.read()
                    self.textEdit.append("成功获取绝对地址！")
                    self.textEdit.append(str(self.my_path[0]))
                    break
                except:
                    self.textEdit.append("打开文件失败，可能是文件内型错误")

        for li in lis:
            href = li.get('href')
            title = li.get('title')
            self.titles.append(title)
            spelling_url = url_head + href
            self.hrefs.append(spelling_url)
            # self.textEdit.append(str(title + '→' + spelling_url))
            with open(self.my_path[0], 'a', encoding='utf-8')as f:
                f.write(title + '→')
                f.write(spelling_url + '→')
        self.f = open(self.my_path[0], 'r', encoding='utf-8').read().split('→')
        self.totals = int((len(self.f) - 1) / 2)
        s = "一共爬取" + str(self.totals) + "个网址\n故写入你所选的绝对地址。"
        self.textEdit.append(s)
        self.Schedule()
        self.pushButton_3.setEnabled(True)

    def Schedule(self):
        self.label_4.setText('正在保存着')
        self.Action()
        self.textEdit.append('保存成功！')
        self.label_4.setText('')

    def Action(self):
        while self.step < 99:
            for i in range(0, self.totals):
                # self.Second_Spiser(i)
                self.step = int((i / self.totals) * 100)
                self.progressBar.setValue(self.step)
                time.sleep(0.001)
        else:
            self.step = 0
            self.textEdit.append('Done!')
            self.progressBar.setValue(self.step)

    # 暂停
    def pushButton_2_clicked(self):
        pass

    # 爬取
    def pushButton_3_clicked(self):
        for i in range(0, self.totals):
            s = str("第%d条\t" % (i + 1)) + self.f[2 * i]
            self.textEdit.append(s)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.spinBox.setEnabled(True)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(self.totals)
        self.spinBox.setSingleStep(10)
        if self.pushButton_5.clicked is not True:
            self.Done()

    def Done(self):
        # print("Hello")
        self.textEdit.append('请点击OK，返回主窗口继续操作。请勿重复，若重复的话，就默认你点击最后一下的序数，以上的序数作废。')

    # ok
    def pushButton_5_clicked(self):
        spinboxValue = self.spinBox.value()
        spell = "你点击第%d条,正在寻找图片链接" % spinboxValue
        self.textEdit.append(spell)
        QtWidgets.QMessageBox.information(self, '提示', '已经记下来所需要的序数。')
        # 创建新文件夹
        path = os.getcwd()
        path = path + '\\' + 'Image'
        self.textEdit.append(self.Build_new_field(new_field_path=path))
        path = path + '\\'
        url = self.f[2 * spinboxValue + 1]
        h = requests.get(url=url)
        if h.status_code == 200:
            text = h.content.decode('utf-8')
        else:
            pass
        html = etree.HTML(text)
        lis = html.xpath('/html/body/div[8]/ul/li/a')
        count = 1
        for li in lis:
            href = li.get('href')  # 爬取图片组网址
            alt = li.xpath('./img')[0].get('alt')  # 爬取图片组标题
            src = li.xpath('./img')[0].get('lazysrc')  # 爬取图片封面地址
            s = f"第%d条：%s\t%s\t封面:%s,提取成功！" % (count, alt, href, src)
            self.textEdit.append(s)
            self.getUrl(alt, href, path)
            count = count + 1
        s = self.textEdit.toPlainText()
        path = os.getcwd()
        with open(f'{path}\\.log', 'a+')as f:
            f.write(s)
            f.close()


    def getUrl(self, title, url, path):
        for j in range(1, 20):
            url1 = url
            if j > 1:
                url1 = url1[:-4] + '_' + str(j) + '.htm'
            # self.Schedule_Download(j)
            self.textEdit.append(url1)
            self.DownloadsImg(j, title, url1, path)

    def DownloadsImg(self, Number, Theme, Url, path):
        res = requests.get(url=Url)
        path = path + Theme
        self.Build_new_field(path)
        path = path + '\\'

        if res.status_code == 200:
            response = res.content.decode('utf-8')

            html = etree.HTML(response)
            lis = html.xpath('//*[@id="ArticleBox"]/p/a/img')
            for li in lis:
                src1 = li.get('src')  # 图片组里面的某一个网址
                if str(src1)[:4] == 'http' or str(src1)[:5] == 'https':
                    img = requests.get(url=src1)
                    if img.status_code == 200:
                        with open(f'{path}{str(Number)}.jpg', 'wb')as f:
                            f.write(img.content)
                            s = (f"第{str(Number)}张标题为{Theme}的图片", "下载成功!!!")
                            self.textEdit.append(str(s))
                            self.update()
                    else:
                        with open(f'{path}\\日志.txt', 'a+')as f:
                            f.writelines(f"错误记录：{Number}, {Theme}, {Url}, {src1}")
                            s = (src1, "此网址不存在!!!")
                            self.textEdit.append(str(s))
                else:
                    pass
        else:
            pass

    def Build_new_field(self, new_field_path):
        #     # 创建文件夹
        isExists = os.path.exists(new_field_path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(new_field_path)
            s = new_field_path + ' 创建成功'
            return s
        else:
            # 如果目录存在则不创建，并提示目录已存在
            s = new_field_path + ' 目录已存在'
            return s

    def Schedule_Download(self, j):
        self.label_4.setText('正在下载并保存')
        self.change_data(j)
        self.textEdit.append('保存成功！')
        self.label_4.setText('')

    def change_data(self, j):
        while self.step < 99:
            self.step = int((j / 20) * 100)
            self.progressBar.setValue(self.step)
            time.sleep(0.001)
        else:
            self.step = 0
            self.textEdit.append('Done!')
            self.progressBar.setValue(self.step)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
