# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '爬取图片下载器.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Form(object):
    def setupUi(self, Form):
        # 创造界面
        Form.setObjectName("Form")
        # 窗口大小
        Form.resize(640, 480)
        # 不可最大化
        Form.setMinimumSize(QtCore.QSize(640, 480))
        #
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 70, 500, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 开始按钮
        self.start = QtWidgets.QPushButton(self.layoutWidget)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        # 恢复按钮
        self.recove = QtWidgets.QPushButton(self.layoutWidget)
        self.recove.setObjectName("recove")
        self.horizontalLayout.addWidget(self.recove)
        # 暂停按钮
        self.suspend = QtWidgets.QPushButton(self.layoutWidget)
        self.suspend.setObjectName("suspend")
        self.horizontalLayout.addWidget(self.suspend)
        # 停止/终止按钮
        self.stop = QtWidgets.QPushButton(self.layoutWidget)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        # 退出按钮
        self.exit = QtWidgets.QPushButton(self.layoutWidget)
        self.exit.setObjectName("exit")
        self.horizontalLayout.addWidget(self.exit)
        # 进度标签
        self.label = QtWidgets.QLabel(Form)
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
        self.schedule = QtWidgets.QProgressBar(Form)
        self.schedule.setGeometry(QtCore.QRect(80, 130, 540, 20))
        self.schedule.setProperty("value", 24)
        self.schedule.setObjectName("schedule")
        # read_list
        self.read_list = QtWidgets.QListWidget(Form)
        self.read_list.setGeometry(QtCore.QRect(80, 170, 540, 300))
        self.read_list.setObjectName("read_list")
        # 记录
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("记录")
        # 标题
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(200, 20, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("爬取图片下载器")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "爬取图片下载器"))
        self.start.setText(_translate("Form", "开始"))
        self.recove.setText(_translate("Form", "恢复"))
        self.suspend.setText(_translate("Form", "暂停"))
        self.stop.setText(_translate("Form", "终止"))
        self.exit.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "进度"))
        self.label_2.setText(_translate("Form", "记录"))
        self.title.setText(_translate("Form", "爬取图片下载器"))


