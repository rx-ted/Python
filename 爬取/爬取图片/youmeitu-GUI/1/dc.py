from mainui import *
from secondui import *
from PyQt5.QtWidgets import *
import sys


class big_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(big_window, self).__init__()
        self.setupUi(self)



class small_window(QDialog,Ui_Dialog):
    def __init__(self):
        super(small_window, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Parent = big_window()
    child = small_window()
    btn = Parent.pushButton
    btn.clicked.connect(child.show)
    Parent.show()
    sys.exit(app.exec_())
