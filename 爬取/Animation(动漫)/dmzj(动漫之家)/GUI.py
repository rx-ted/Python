# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('mainwindow')
        self.resize(640, 480)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 15, 80, 30))
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(130, 15, 200, 30))
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(500, 20, 120, 20))
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 600, 300))
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 15, 90, 30))
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 400, 93, 28))
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 400, 93, 28))
        self.retranslateUi()
        self.show()

    def retranslateUi(self):
        self.label.setText(
            "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">输入动漫</span></p></body></html>")
        self.label_2.setText("状态：")
        self.pushButton.setText("搜索")
        self.pushButton_2.setText("恢复数据")
        self.pushButton_3.setText("打断下载")


if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    m = main_window()
    sys.exit(app.exec_())
