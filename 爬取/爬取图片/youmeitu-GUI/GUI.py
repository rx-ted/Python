# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from lxml import etree
from bs4 import BeautifulSoup
import os, sys, io
import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from spider import *
from secondspider import Ui_spider
from DriverCore import *

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Wallpaper/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setProperty("ico", icon)
        self.label = QtWidgets.QLabel(Dialog)
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
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

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
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
        self.progressBar.setProperty("value", 0)
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
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 210, 831, 410))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 630, 130, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 630, 370, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        # ?????????????????????
        # self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)

        self.pushButton_5.clicked.connect(Dialog.close)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "?????????????????????"))
        self.pushButton.setText(_translate("Dialog", "??????"))
        self.pushButton_2.setText(_translate("Dialog", "??????"))
        self.pushButton_3.setText(_translate("Dialog", "??????"))
        self.pushButton_4.setText(_translate("Dialog", "??????"))
        self.pushButton_5.setText(_translate("Dialog", "??????"))
        self.label_2.setText(_translate("Dialog", "??????"))
        self.label_3.setText(_translate("Dialog", "??????"))
        self.label_4.setText(_translate("Dialog", ""))
        self.label_5.setText(_translate("Dialog", "QQ??????935233077"))
        self.label_6.setText(_translate("Dialog", "????????????:15524561325132"))

    def pushButton_clicked(self):
        start = QMessageBox.information(self, '??????', '??????????????????: http://m.umei.cc \n???????????????', QMessageBox.Ok | QMessageBox.No,
                                        QMessageBox.No)
        if start == QMessageBox.Ok:
            self.Start()
        else:
            pass
    # ????????????
    def pushButton_2_clicked(self):
        pass


    # ????????????
    def pushButton_3_clicked(self):
        pass
    # ??????
    def pushButton_4_clicked(self):
        pass

    # ??????(???????????????)
    def pushButton_5_clicked(self):
        pass

    # ??????????????????
    def Build_filed(self, new_filed_path):
        # ???????????????
        isExists = os.path.exists(new_filed_path)
        # ????????????
        if not isExists:
            os.makedirs(new_filed_path)
            return new_filed_path + '\tSuccess to mkdir this filename.'
        else:
            # ??????????????????????????????????????????
            return new_filed_path + 'The directory already exists. Do not create a folder.'
            pass  # ??????

    # ????????????
    def Start(self):
        urlTags = 'http://m.umei.cc/tags/'
        html = Spider.getUrl(self, urlTags)
        html1 = etree.HTML(html)
        lis = html1.xpath('/html/body/div[4]/div/a')
        url_head = 'http://m.umei.cc'
        self.titles = []
        self.hrefs = []
        while True:
            self.my_path = QFileDialog.getOpenFileName(self, '??????????????????', '/', '????????????(*.md);;????????????(.*txt)')
            if self.my_path[0]:
                try:
                    # ??????
                    with open(self.my_path[0], 'w', encoding='utf-8')as f:
                        f.write('')
                    self.textEdit.append("?????????????????????")
                    with open(self.my_path[0], 'r', encoding='utf-8')as f:
                        f.read()
                    self.textEdit.append("???????????????????????????")
                    break
                except:
                    self.textEdit.append("????????????????????????????????????????????????")

        for li in lis:
            href = li.get('href')
            title = li.get('title')
            self.titles.append(title)
            spelling_url = url_head + href
            self.hrefs.append(spelling_url)
            # self.textEdit.append(str(title + '???' + spelling_url))
            with open(self.my_path[0], 'a', encoding='utf-8')as f:
                f.write(title + '???')
                f.write(spelling_url + '???')

        self.schedule()
        self.textEdit.setGeometry(QtCore.QRect(10, 210, 491, 410))
        # print(f.split('???'))
        # print(len(f.split('???')))

    # ??????????????????
    def schedule(self):
        self.f = open(self.my_path[0], 'r', encoding='utf-8').read().split('???')
        self.totals = int((len(self.f) - 1) / 2)
        s = "????????????" + str(self.totals) + "?????????\n????????????????????????????????????"
        self.textEdit.append(s)
        self.timer = QBasicTimer()
        self.step = 0
        self.label_4.setText('???????????????')
        self.Action()
        self.textEdit.append('???????????????')
        self.label_4.setText('')
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(False)

    # ??????????????????
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    MainWindow = parents_window()
    ChildWindow = child_window()
    btn =Ui_Dialog.pushButton_2
    btn.clicked.connect(ChildWindow.show)

    sys.exit(app.exec_())

