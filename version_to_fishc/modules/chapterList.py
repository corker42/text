from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel,pyqtSignal
from PyQt5.QtGui import QIcon,QFont
import sys,os,json

class QchapterList(QDialog):
    Signal_of_c_num = pyqtSignal(int)
    Signal_of_all_num = pyqtSignal(int)
    Signal_of_chapterNames = pyqtSignal(list)

    def __init__(self,novelName):
        super().__init__()
        self.novelName = novelName
        self.all_num = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.novelName+"  章节目录")
        if __name__ == "__main__":
            self.setWindowIcon(QIcon('../images/book.ico'))
        else:
            self.setWindowIcon(QIcon("./images/book.ico"))
        self.setFixedSize(400, 800)
        layout = QVBoxLayout()
        # 创捷列表组件
        listview = QListView()
        listModel = QStringListModel()
        self.c_list = []
        if __name__ == "__main__":
            os.chdir("../books/"+self.novelName)
        else:
            os.chdir("./books/"+self.novelName)

        with open("chapter_list.json", mode='r', encoding="utf-8") as f:
            chapters = json.loads(f.read())  # 注：read读取出来的时字符串，需要转为json对象
            for chapter in chapters:
                c_name = (str(chapter).split(":", 1))[0][2:-1]
                self.c_list.append(c_name)

        self.all_num = len(self.c_list)
        listModel.setStringList(self.c_list)

        listview.setModel(listModel)
        listview.setFont(QFont("楷体",11))
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)
        os.chdir("..")
        os.chdir("..")

    def clicked(self,item):
        QMessageBox.information(self,self.novelName,"是否跳转到：" + self.c_list[item.row()])
        self.Signal_of_c_num.emit(item.row())
        self.Signal_of_chapterNames.emit(self.c_list)
        self.Signal_of_all_num.emit(self.all_num)
        self.close()

if __name__ == "__main__":
    novelName = "斗破苍穹"
    app = QApplication(sys.argv)
    win = QchapterList(novelName)
    win.show()
    sys.exit(app.exec_())