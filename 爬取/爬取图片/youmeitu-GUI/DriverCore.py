from mainwindow import *
from secondspider import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from mainwindow import Ui_mainWindow

path = 'C:\\Users\\Administrator\\1.txt'


class parents_window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.mainUI = Ui_mainWindow()
        self.mainUI.setupUi(self)


class child_window(QDialog):
    def __init__(self1, parent=None):
        QDialog.__init__(self1, parent)

        self1.secondUI = Ui_spider()
        self1.secondUI.setupUi(self1)


class Done():
    # 爬取按钮 一切任务
    def done(self1, i):
        f = open(path, 'w+')
        f.write(str(i))
        f.close()

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = parents_window()
    ChildWindow = child_window()
    btn = MainWindow.mainUI.pushButton_2
    btn.clicked.connect(ChildWindow.show)
    MainWindow.show()
    sys.exit(app.exec_())
