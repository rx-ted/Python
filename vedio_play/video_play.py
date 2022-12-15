# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_play.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 225))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.show()
        font = QtGui.QFont()
        font.setPointSize(1)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/img/video_player.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
                                 "color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 280, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 60, 40, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 520, 80, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/video_player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 520, 80, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.TabFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/video_playerT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(50, 110, 700, 393))
        # self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#000000;\">电视网址</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "爬取"))
        self.pushButton_2.setWhatsThis(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:16pt;\">播放</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "播放"))
        self.pushButton_3.setWhatsThis(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:16pt;\">播放</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "暂停"))

    def get_jiexi(self, url):
        with open('DPlayer.min.js', 'r', encoding='utf-8')as f:
            s = f.read()
        url = "https://jiexi.380k.com/?url={}&type=".format(url)
        page = QtWebEngineWidgets.QWebEnginePage()

        # page.runJavaScript(s)
        # https://apd-vliveachy.apdcdn.tc.qq.com/vqq/moviets.tc.qq.com/Apg8smLj3eoWJGWYIFG5sQjds2ONpuKN-cSmlcMTCnmA/uwMROfz2r5zAoaQXGdGnCmdf648-D5cjn-5rfP_pUfhaDIH-/7EA0VR_lvPJzobqvi7i-spECE1iC7HRjtIMcdM4Cu5D32FHCOSqCt5Vp9NGHMtGBM1U16wDyzcHgMCfgE_Bw475bQ0snH63CMdtht69qW6_wjsjXL3tOskrEi63CpyvFpu3uK-bHsC9XkxQXuEBeSQ/a0033i504y4.321003.ts.m3u8?ver=4

        # self.webView.setUrl(QtCore.QUrl(url))
        # 添加浏览器到窗口中
        self.webView.url()
        # self.webView.load(QtCore.QUrl(url))
        self.webView.load(QtCore.QUrl(url))
        # self.webView.setPage(page)
        # QtWidgets.QMainWindow.setCentralWidget(self.webView)
        self.webView.show()

        # https://v.qq.com/x/cover/otff8quzy6b2dlw.html
        Dialog.setCentralWidget(self.webView)

        print(url)

    def get_url(self):
        while True:
            url = self.lineEdit.text()
            if url:
                self.get_jiexi(url)
                QtWidgets.QMessageBox.information(Dialog, "提示", "可以播放一下！请稍等～～～")
                break
            else:
                QtWidgets.QMessageBox.warning(Dialog, "警告", "这是不可空字符串！")
                break


if __name__ == '__main__':
    import sys

    # QtWidgets.QGridLayout()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    w = Ui_MainWindow()
    w.setupUi(Dialog)
    w.pushButton.clicked.connect(w.get_url)
    sys.exit(app.exec_())
