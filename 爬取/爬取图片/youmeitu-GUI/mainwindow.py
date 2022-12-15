# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from spider import *
from lxml import etree
import time
# from secondspider import Ui_spider


class Ui_mainWindow(QtWidgets.QMainWindow):
    # def __init__(self):
    #     super(Ui_spider).__init__()
    #     self.setupUi()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(850, 650)
        mainWindow.setMinimumSize(QtCore.QSize(850, 650))
        mainWindow.setMaximumSize(QtCore.QSize(850, 650))
        mainWindow.setSizeIncrement(QtCore.QSize(850, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setProperty("ico", icon)
        self.label = QtWidgets.QLabel(mainWindow)
        self.label.setGeometry(QtCore.QRect(310, 10, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(mainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 70, 510, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.formLayoutWidget = QtWidgets.QWidget(mainWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 120, 831, 70))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.progressBar)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.textEdit = QtWidgets.QTextEdit(mainWindow)
        self.textEdit.setGeometry(QtCore.QRect(10, 210, 831, 410))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(mainWindow)
        self.label_5.setGeometry(QtCore.QRect(20, 630, 130, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(mainWindow)
        self.label_6.setGeometry(QtCore.QRect(440, 630, 370, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.retranslateUi(mainWindow)

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.pushButton_5.clicked.connect(mainWindow.close)

        # 按钮初始值状态
        # self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def pushButton_clicked(self):
        start = QMessageBox.information(self, '提示', '爬取一些图片: http://m.umei.cc \n是否继续？', QMessageBox.Ok | QMessageBox.No,
                                        QMessageBox.No)
        if start == QMessageBox.Ok:
            # pass
            self.Start()
        else:
            pass

    # 开始程序
    def Start(self):
        urlTags = 'http://m.umei.cc/tags/'
        html = Spider.getUrl(self, urlTags)
        html1 = etree.HTML(html)
        lis = html1.xpath('/html/body/div[4]/div/a')
        url_head = 'http://m.umei.cc'
        self.titles = []
        self.hrefs = []
        while True:
            self.my_path = QFileDialog.getOpenFileName(self, '获取绝对地址', '/', '文本格式(*.md);;文本格式(.*txt)')
            if self.my_path[0]:
                try:
                    # 清空
                    with open(self.my_path[0], 'w', encoding='utf-8')as f:
                        f.write('')
                    self.textEdit.append("清空数据成功！")
                    with open(self.my_path[0], 'r', encoding='utf-8')as f:
                        f.read()
                    self.textEdit.append("成功获取绝对地址！")
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
        self.schedule()

        # 进度界面设置

    def schedule(self):
        self.f = open(self.my_path[0], 'r', encoding='utf-8').read().split('→')
        self.totals = int((len(self.f) - 1) / 2)
        s = "一共爬取" + str(self.totals) + "个网址\n故写入你所选的绝对地址。"
        self.textEdit.append(s)
        self.timer = QBasicTimer()
        self.step = 0
        self.label_4.setText('正在保存着')
        self.Action()
        self.textEdit.append('保存成功！')
        self.label_4.setText('')
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(False)

        # 进度进行判断

    def Action(self):
        while self.step < 99:
            for i in range(0, self.totals):
                # self.Second_Spiser(i)
                self.step = int((i / self.totals) * 100)
                self.progressBar.setValue(self.step)
                time.sleep(0.01)
        else:
            self.step = 0
            self.textEdit.append('Done!')
            self.progressBar.setValue(self.step)

    def secondspider(self, i):
        self.textEdit.append(str(i))
        pass

    # 暂停
    def pushButton_3_clicked(self):
        pass

    # 终止，一切都停止任务，需要询问
    def pushButton_3_clicked(self):
        pass

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "爬取图片下载器"))
        self.label.setText(_translate("mainWindow", "爬取图片下载器"))
        self.pushButton.setText(_translate("mainWindow", "开始"))
        self.pushButton_2.setText(_translate("mainWindow", "爬取"))
        self.pushButton_3.setText(_translate("mainWindow", "暂停"))
        self.pushButton_4.setText(_translate("mainWindow", "终止"))
        self.pushButton_5.setText(_translate("mainWindow", "退出"))
        self.label_2.setText(_translate("mainWindow", "进度"))
        self.label_3.setText(_translate("mainWindow", "状态"))
        self.textEdit.setHtml(_translate("mainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.label_5.setText(_translate("mainWindow", "QQ群：935233077"))
        self.label_6.setText(_translate("mainWindow", "传送地址:15524561325132"))
