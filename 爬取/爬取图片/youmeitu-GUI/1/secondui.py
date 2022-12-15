# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from mainui import Ui_MainWindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(140, 130, 91, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(250)
        self.spinBox.setSingleStep(10)
        self.spinBox.setMinimum(0)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        self.pushButton.clicked.connect(self.pushButton_clicked)

        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def pushButton_clicked(self):
        v = self.spinBox.value()
        print("hello%d" % v)
        self.mu = Ui_MainWindow()

        self.mu.lineEdit.setText(str(v))






    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
