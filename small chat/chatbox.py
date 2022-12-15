# python3.8+
# encode:utf-8
import sys
from PyQt5 import QtGui,QtCore,QtWidgets
face = ([
  ["grinning", "😀"],
  ["grin", "😁"],
  ["joy", "😂"],
  ["smiley", "😃"],
  ["smile", "😄"],
  ["sweat_smile", "😅"],
  ["laughing", "😆"],
  ["satisfied", "😆"],
  ["innocent", "😇"],
  ["smiling_imp", "😈"],
  ["wink", "😉"],
  ["blush", "😊"],
  ["yum", "😋"],
  ["relieved", "😌"],
  ["heart_eyes", "😍"],
  ["sunglasses", "😎"],
  ["smirk", "😏"],
  ["neutral_face", "😐"],
  ["expressionless", "😑"],
  ["unamused", "😒"],
  ["sweat", "😓"],
  ["pensive", "😔"],
  ["confused", "😕"],
  ["confounded", "😖"],
  ["kissing", "😗"],
  ["kissing_heart", "😘"],
  ["kissing_smiling_eyes", "😙"],
  ["kissing_closed_eyes", "😚"],
  ["stuck_out_tongue", "😛"],
  ["stuck_out_tongue_winking_eye", "😜"],
  ["stuck_out_tongue_closed_eyes", "😝"],
  ["disappointed", "😞"],
  ["worried", "😟"],
  ["angry", "😠"],
  ["rage", "😡"],
  ["cry", "😢"],
  ["persevere", "😣"],
  ["triumph", "😤"],
  ["disappointed_relieved", "😥"],
  ["frowning", "😦"],
  ["anguished", "😧"],
  ["fearful", "😨"],
  ["weary", "😩"],
  ["sleepy", "😪"],
  ["tired_face", "😫"],
  ["grimacing", "😬"],
  ["sob", "😭"],
  ["open_mouth", "😮"],
  ["hushed", "😯"],
  ["cold_sweat", "😰"],
  ["scream", "😱"],
  ["astonished", "😲"],
  ["flushed", "😳"],
  ["sleeping", "😴"],
  ["dizzy_face", "😵"],
  ["no_mouth", "😶"],
  ["mask", "😷"],
  ["smile_cat", "😸"],
  ["joy_cat", "😹"],
  ["smiley_cat", "😺"],
  ["heart_eyes_cat", "😻"],
  ["smirk_cat", "😼"],
  ["kissing_cat", "😽"],
  ["pouting_cat", "😾"],
  ["crying_cat_face", "😿"],
  ["scream_cat", "🙀"],
  ["no_good", "🙅"],
  ["ok_woman", "🙆"],
  ["bow", "🙇"],
  ["see_no_evil", "🙈"],
  ["hear_no_evil", "🙉"],
  ["speak_no_evil", "🙊"],
  ["raising_hand", "🙋"],
  ["raised_hands", "🙌"],
  ["person_frowning", "🙍"],
  ["person_with_pouting_face", "🙎"],
  ["pray", "🙏"]
])


class UI_chatbox(QtWidgets.QWidget):
    def __init__(self):
        super(UI_chatbox,self).__init__()
        self.setUi()
        self.right_menu_clicked()
    

    def setUi(self):
        self.resize(500,500)
        self.setWindowTitle("聊天框")
        self.box = QtWidgets.QListWidget(self)
        self.box.setGeometry(QtCore.QRect(10,0,480,300))
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # create menu
        self.right_menu = QtWidgets.QMenu(self)
        # self.right_menu.setGeometry(QtCore.QRect(10,450,30,30))
        # add menu
        self.right_menu.actionAt = self.right_menu.addAction(QtGui.QIcon(""), '删除')
        self.right_menu.actionAt = self.right_menu.addAction(QtGui.QIcon(""), '改名')
        self.right_menu.actionAt = self.right_menu.addAction(QtGui.QIcon(""), '移动')
        self.right_menu.actionAt = self.right_menu.addAction(QtGui.QIcon(""), '复制')
        # 显示
        self.customContextMenuRequested.connect(self.showContextMenu)


        for i in face:
           self.box.addItem(i[1])


        self.box.clicked.connect(self.clicked)

        # click menu
        self.right_menu.triggered[QtWidgets.QAction].connect(self.remove)
        # self.box.itemClicked.connect(self.item_Clicked)
        # self.box.itemDoubleClicked.connect(self.double_clicked)
        #

        self.show()

    def right_menu_clicked(self):
        '''
        右击则创建菜单

        '''




    
    def showContextMenu(self):
        item = self.box.selectedIndexes()
        if item:
            self.right_menu.show()
            self.right_menu.exec_(QtGui.QCursor.pos())
    
    
    def clicked(self,item):
        r = item.row()
        print(r)

    def item_Clicked(self,item):

        print("You choose "+item.text())
        QtWidgets.QMessageBox.information(self,"提示","你选择了"+item.text())


    def double_clicked(self,item):
        print(item.text())



    def remove(self,QAction):
        print('删除')
        pass
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = UI_chatbox()
    
    sys.exit(app.exec_())