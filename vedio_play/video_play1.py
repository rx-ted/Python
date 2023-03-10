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
#                                       "<html><head/><body><p><span style=\" color:#000000;\">????????????</span></p></body></html>"))
#         self.pushButton.setText(_translate("MainWindow", "??????"))
#         self.pushButton_2.setWhatsThis(_translate("MainWindow",
#                                                   "<html><head/><body><p><span style=\" font-size:16pt;\">??????</span></p></body></html>"))
#         self.pushButton_2.setText(_translate("MainWindow", "??????"))
#         self.pushButton_3.setWhatsThis(_translate("MainWindow",
#                                                   "<html><head/><body><p><span style=\" font-size:16pt;\">??????</span></p></body></html>"))
#         self.pushButton_3.setText(_translate("MainWindow", "??????"))
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
#                 QtWidgets.QMessageBox.information(Dialog, "??????", "???????????????????????????????????????")
#                 break
#             else:
#                 QtWidgets.QMessageBox.warning(Dialog,"??????","???????????????????????????")
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
        # ??????????????????
        self.setWindowTitle('My Browser')
        # ??????????????????
        self.setWindowIcon(QIcon('icons/penguin.png'))
        # ??????????????????900*600
        self.resize(900, 600)
        self.show()

        # ???????????????
        self.browser = QWebEngineView()
        url = 'https://v.qq.com/x/cover/otff8quzy6b2dlw.html'
        # ????????????????????? URL
        self.browser.setUrl(QUrl(url))
        # ???????????????????????????
        self.setCentralWidget(self.browser)

        ###??????QToolBar???????????????????????????QAction????????????
        # ???????????????
        navigation_bar = QToolBar('Navigation')
        # ?????????????????????
        navigation_bar.setIconSize(QSize(16, 16))
        # ???????????????????????????
        self.addToolBar(navigation_bar)

        # QAction?????????????????????????????????action?????????action?????????????????????????????????
        # ??????????????????????????????????????????????????????
        back_button = QAction(QIcon('icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('icons/cross.png'), 'stop', self)
        reload_button = QAction(QIcon('icons/renew.png'), 'reload', self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        # ??????????????????????????????
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        # ??????URL?????????
        self.urlbar = QLineEdit()
        # ???????????????????????????????????????
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)

        # ??????????????????url???????????????
        self.browser.urlChanged.connect(self.renew_urlbar)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def renew_urlbar(self, q):
        # ??????????????????????????????????????????
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


# ????????????
app = QApplication(sys.argv)
# ???????????????
window = MainWindow()
# ????????????
window.show()
# ??????????????????????????????
app.exec_()