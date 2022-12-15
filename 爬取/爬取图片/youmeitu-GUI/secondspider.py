# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '二次爬取.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from DriverCore import *


class Ui_spider(QtWidgets.QMainWindow):
    def setupUi(self1, spider):
        spider.setObjectName("spider")
        spider.resize(700, 300)
        spider.setMinimumSize(QtCore.QSize(700, 300))
        spider.setMaximumSize(QtCore.QSize(700, 300))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        spider.setFont(font)
        spider.setWindowIcon(QIcon('icon.ico'))

        self1.formLayoutWidget = QtWidgets.QWidget(spider)
        self1.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 241))
        self1.formLayoutWidget.setObjectName("formLayoutWidget")
        self1.formLayout = QtWidgets.QFormLayout(self1.formLayoutWidget)
        self1.formLayout.setContentsMargins(0, 0, 0, 0)
        self1.formLayout.setObjectName("formLayout")
        self1.label = QtWidgets.QLabel(self1.formLayoutWidget)
        self1.label.setTextFormat(QtCore.Qt.RichText)
        self1.label.setScaledContents(False)
        self1.label.setAlignment(QtCore.Qt.AlignCenter)
        self1.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self1.label.setObjectName("label")
        self1.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self1.label)
        self1.textEdit2 = QtWidgets.QTextEdit(self1.formLayoutWidget)
        self1.textEdit2.setObjectName("textEdit")
        self1.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self1.textEdit2)
        self1.horizontalLayoutWidget = QtWidgets.QWidget(spider)
        self1.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 260, 451, 31))
        self1.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self1.horizontalLayout = QtWidgets.QHBoxLayout(self1.horizontalLayoutWidget)
        self1.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self1.horizontalLayout.setObjectName("horizontalLayout")
        self1.pushButton = QtWidgets.QPushButton(self1.horizontalLayoutWidget)
        self1.pushButton.setObjectName("pushButton")
        self1.pushButton.clicked.connect(self1.pushButton_clicked)

        self1.horizontalLayout.addWidget(self1.pushButton)
        self1.pushButton_2 = QtWidgets.QPushButton(self1.horizontalLayoutWidget)
        self1.pushButton_2.setObjectName("pushButton_2")
        self1.pushButton_2.clicked.connect(spider.close)
        self1.horizontalLayout.addWidget(self1.pushButton_2)
        self1.label_3 = QtWidgets.QLabel(spider)
        self1.label_3.setGeometry(QtCore.QRect(500, 100, 181, 171))
        self1.label_3.setTextFormat(QtCore.Qt.AutoText)
        self1.label_3.setScaledContents(False)
        self1.label_3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self1.label_3.setObjectName("label_3")
        self1.label_2 = QtWidgets.QLabel(spider)
        self1.label_2.setGeometry(QtCore.QRect(500, 60, 103, 24))
        self1.label_2.setObjectName("label_2")
        self1.spinBox = QtWidgets.QSpinBox(spider)
        self1.spinBox.setGeometry(QtCore.QRect(610, 60, 51, 24))
        # 设置上下限大小
        self1.spinBox.setMinimum(1)
        self1.spinBox.setMaximum(500)
        self1.spinBox.setSingleStep(10)
        self1.spinBox.setObjectName("spinBox")
        self1.retranslateUi(spider)
        QtCore.QMetaObject.connectSlotsByName(spider)

    def pushButton_clicked(self1):
        spinboxValue = self1.spinBox.value()
        self1.textEdit2.append('请点击取消，返回主窗口继续操作。请勿重复，若重复的话，就默认你点击最后一下的序数，以上的序数作废。')
        QMessageBox.information(self1, '提示', '已经记下来所需要的序数。')
        if self1.pushButton_2.clicked is not False:
            Done.done(self1, spinboxValue)

    def getSpinboxValue(self1):
        return

    def retranslateUi(self1, spider):
        _translate = QtCore.QCoreApplication.translate
        spider.setWindowTitle(_translate("spider", "Spider"))
        self1.label.setText(_translate("spider",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">需要爬取的序数</span></p></body></html>"))
        self1.pushButton.setText(_translate("spider", "确定"))
        self1.pushButton_2.setText(_translate("spider", "取消"))
        self1.label_3.setText(_translate("spider",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">说明</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">左方有文本框，上下滑动，找找</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">自己能否需要爬取。若有，请输</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">入上方序数，然后点击确定，就</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">可以运行爬取。否则点击取消，</span></p><p align=\"justify\"><span style=\" font-size:8pt;\">就可以关闭本窗口。</span></p></body></html>"))
        self1.label_2.setText(_translate("spider", "输入序数：  "))
