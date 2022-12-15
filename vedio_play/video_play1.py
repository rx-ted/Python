# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_play.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import requests
from urllib import parse
import re
# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.setWindowModality(QtCore.Qt.NonModal)
#         MainWindow.resize(800, 600)
#         icon = QtGui.QIcon('img/video_player.png')
#         MainWindow.setMinimumSize(QtCore.QSize(400, 225))
#         MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
#         MainWindow.show()
#         font = QtGui.QFont()
#         font.setPointSize(1)
#         MainWindow.setFont(font)
#
#         MainWindow.setWindowIcon(icon)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
#         self.graphicsView.setGeometry(QtCore.QRect(50, 100, 700, 393))
#         self.graphicsView.setObjectName("graphicsView")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(30, 60, 80, 20))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.label.setFont(font)
#         self.label.setStyleSheet("\n"
#                                  "color: rgb(0, 0, 0);")
#         self.label.setObjectName("label")
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(110, 60, 280, 20))
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit.setFont(font)
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(410, 60, 40, 20))
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap("img/down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.pushButton.setIcon(icon1)
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(260, 520, 80, 51))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.pushButton_2.setFont(font)
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap("img/video_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.pushButton_2.setIcon(icon2)
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(450, 520, 80, 51))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.pushButton_3.setFont(font)
#         self.pushButton_3.setFocusPolicy(QtCore.Qt.TabFocus)
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap("img/video_playerT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.pushButton_3.setIcon(icon3)
#         self.pushButton_3.setObjectName("pushButton_3")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "video_player"))
#         self.label.setText(_translate("MainWindow",
#                                       "<html><head/><body><p><span style=\" color:#000000;\">电视网址</span></p></body></html>"))
#         self.pushButton.setText(_translate("MainWindow", "爬取"))
#         self.pushButton_2.setWhatsThis(_translate("MainWindow",
#                                                   "<html><head/><body><p><span style=\" font-size:16pt;\">播放</span></p></body></html>"))
#         self.pushButton_2.setText(_translate("MainWindow", "播放"))
#         self.pushButton_3.setWhatsThis(_translate("MainWindow",
#                                                   "<html><head/><body><p><span style=\" font-size:16pt;\">播放</span></p></body></html>"))
#         self.pushButton_3.setText(_translate("MainWindow", "暂停"))
#
#     def get_jiexi(self, url):
#         url = "https://jiexi.380k.com/?url={}&type=".format(url)
#         print(url)
#
#
#     def get_url(self):
#         while True:
#             url = self.lineEdit.text()
#             if url:
#                 self.get_jiexi(url)
#                 QtWidgets.QMessageBox.information(Dialog, "提示", "可以播放一下！请稍等～～～")
#                 break
#             else:
#                 QtWidgets.QMessageBox.warning(Dialog,"警告","这是不可空字符串！")
#                 break
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QMainWindow()
#     w = Ui_MainWindow()
#     w.setupUi(Dialog)
#     w.pushButton.clicked.connect(w.get_url)
#     sys.exit(app.exec_())
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys


class MainWindow(QMainWindow):
    # noinspection PyUnresolvedReferences
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('My Browser')
        # 设置窗口图标
        self.setWindowIcon(QIcon('icons/penguin.png'))
        # 设置窗口大小900*600
        self.resize(900, 600)
        self.show()

        # 设置浏览器
        self.browser = QWebEngineView()
        url = 'https://v.qq.com/x/cover/otff8quzy6b2dlw.html'
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)

        ###使用QToolBar创建导航栏，并使用QAction创建按钮
        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
        navigation_bar.setIconSize(QSize(16, 16))
        # 添加导航栏到窗口中
        self.addToolBar(navigation_bar)

        # QAction类提供了抽象的用户界面action，这些action可以被放置在窗口部件中
        # 添加前进、后退、停止加载和刷新的按钮
        back_button = QAction(QIcon('icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('icons/cross.png'), 'stop', self)
        reload_button = QAction(QIcon('icons/renew.png'), 'reload', self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        # 将按钮添加到导航栏上
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        # 添加URL地址栏
        self.urlbar = QLineEdit()
        # 让地址栏能响应回车按键信号
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)

        # 让浏览器相应url地址的变化
        self.browser.urlChanged.connect(self.renew_urlbar)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def renew_urlbar(self, q):
        # 将当前网页的链接更新到地址栏
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


# 创建应用
app = QApplication(sys.argv)
# 创建主窗口
window = MainWindow()
# 显示窗口
window.show()
# 运行应用，并监听事件
app.exec_()