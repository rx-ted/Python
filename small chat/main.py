# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import random


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.define()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 699)
        self.label_textinfo = QtWidgets.QLabel(Form)
        self.label_textinfo.setGeometry(QtCore.QRect(10, 80, 121, 30))
        self.label_textinfo.setTextFormat(QtCore.Qt.AutoText)
        self.label_textinfo.setObjectName("label_textinfo")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 10, 111, 56))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_getip = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getip.setObjectName("lineEdit_getip")
        self.verticalLayout.addWidget(self.lineEdit_getip)
        self.lineEdit_getport = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getport.setObjectName("lineEdit_getport")
        self.verticalLayout.addWidget(self.lineEdit_getport)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 41, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_ip = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ip.setObjectName("label_ip")
        self.verticalLayout_2.addWidget(self.label_ip)
        self.label_port = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_port.setObjectName("label_port")
        self.verticalLayout_2.addWidget(self.label_port)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(200, 10, 81, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_getip = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_getip.setEnabled(True)
        self.pushButton_getip.setObjectName("pushButton_getip")
        self.verticalLayout_3.addWidget(self.pushButton_getip)
        self.pushButton_getport = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_getport.setEnabled(True)
        self.pushButton_getport.setObjectName("pushButton_getport")
        self.verticalLayout_3.addWidget(self.pushButton_getport)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(290, 10, 318, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_tcp = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_tcp.setObjectName("comboBox_tcp")
        self.comboBox_tcp.insertItem(1, 'tcp 客户端')
        self.comboBox_tcp.insertItem(2, 'tcp 服务端')
        self.comboBox_tcp.insertItem(3, 'udp 客户端')
        self.comboBox_tcp.insertItem(4, 'udp 服务端')
        self.comboBox_tcp.insertItem(5, '无')
        self.verticalLayout_4.addWidget(self.comboBox_tcp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Connection = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_Connection.setObjectName("pushButton_Connection")
        self.horizontalLayout.addWidget(self.pushButton_Connection)
        self.pushButton_Disconnect = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_Disconnect.setObjectName("pushButton_Disconnect")
        self.horizontalLayout.addWidget(self.pushButton_Disconnect)
        self.pushButton_cls = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_cls.setObjectName("pushButton_cls")
        self.horizontalLayout.addWidget(self.pushButton_cls)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 650, 75, 41))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 130, 601, 381))
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 530, 521, 161))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_getip, self.lineEdit_getport)

        self.pushButton_getip.clicked.connect(self.button_click_get_ip)
        self.pushButton_getport.clicked.connect(self.button_clicked_get_port)
        self.pushButton_cls.clicked.connect(self.cls)
        self.pushButton_Connection.clicked.connect(self.connection)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "tcp/udp"))
        self.label_textinfo.setText(_translate("Form",
                                               "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#0000ff;\">信息区域</span></p></body></html>"))
        self.label_ip.setText(_translate("Form", "ip"))
        self.label_port.setText(_translate("Form", "端口"))
        self.pushButton_getip.setText(_translate("Form", "获取ip"))
        self.pushButton_getport.setText(_translate("Form", "随机端口"))
        self.pushButton_Connection.setText(_translate("Form", "连接"))
        self.pushButton_Disconnect.setText(_translate("Form", "断开"))
        self.pushButton_cls.setText(_translate("Form", "清除信息"))
        self.pushButton.setText(_translate("Form", "发送"))

    def define(self):
        host_name = socket.gethostname()
        self.ip = socket.gethostbyname(host_name)
        # self.lineEdit_getip.setText('120.0.0.0')
        self.lineEdit_getip.setText(self.ip)
        self.port = random.randint(0, 9999)
        self.lineEdit_getport.setText(str(self.port))

    def button_click_get_ip(self):
        host_name = socket.gethostname()
        self.ip = socket.gethostbyname(host_name)
        self.lineEdit_getip.setText(self.ip)

    def button_clicked_get_port(self):
        self.port = random.randint(0, 9999)
        self.lineEdit_getport.setText(str(self.port))

    def cls(self):
        self.lineEdit_getip.setText('')
        self.lineEdit_getport.setText('')
        self.textEdit.setText('')
        self.listWidget.clear()

    def connection(self):
        address = (self.ip, self.port)
        S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        S.bind(address)
       

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_Form()
    w.show()

    sys.exit(app.exec_())
