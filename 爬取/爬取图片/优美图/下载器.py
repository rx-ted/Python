# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '下载器.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import random
import requests
from lxml import etree
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    # 界面设计
    def setupUi(self, Dialog):
        # 主要界面
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 650)
        # 图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Wallpaper/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setProperty("ico", icon)
        # 标题
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

        # 开始按钮
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        # 暂停按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        # 恢复/继续
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        # 终止
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        # 退出/关闭窗口
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 120, 831, 70))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")

        # 进度
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)

        # 进度
        self.progressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.progressBar)

        # 状态
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        # 状态框
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        # 多行文本编辑
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 210, 831, 410))
        self.textEdit.setObjectName("textEdit")
        # QQ群
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 630, 130, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        # 网络地址
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 630, 370, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.pushButton_5.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #重新翻译界面
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "爬取图片下载器"))
        self.label.setText(_translate("Dialog", "爬取图片下载器"))
        self.pushButton.setText(_translate("Dialog", "开始"))
        self.pushButton_2.setText(_translate("Dialog", "暂停"))
        self.pushButton_3.setText(_translate("Dialog", "继续"))
        self.pushButton_4.setText(_translate("Dialog", "终止"))
        self.pushButton_5.setText(_translate("Dialog", "退出"))
        self.label_2.setText(_translate("Dialog", "进度"))
        self.label_3.setText(_translate("Dialog", "状态"))
        self.label_4.setText(_translate("Dialog", "变量字符串"))
        self.label_5.setText(_translate("Dialog", "QQ群：935233077"))
        self.label_6.setText(_translate("Dialog", "传送地址:15524561325132"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    From = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(From)
    From.show()
    sys.exit(app.exec_())

