import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_main_window import Ui_MainWindow
from PyQt6.QtGui import QAction
import sqlite3



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #uic.loadUi('main_window3.ui',self)

        self.stackedWidget.setCurrentWidget(self.mainmenu)

        self.variants_rus_act.triggered.connect(self.runrusvar)
        self.main_act.triggered.connect(self.runmainmenu)
        mainmenu_action = QAction("Главное меню", self)
        mainmenu_action.triggered.connect(self.runmainmenu)
        self.menuBar().insertAction(self.menuBar().actions()[0], mainmenu_action)

        self.pushButton.clicked.connect(self.runrusvar)
        self.startrus_btn.clicked.connect(self.startrus)

        self.con = sqlite3.connect('use_tasks.db')

    def loadvr(self):
        cur = self.con.cursor()
        query = """SELECT task_text, task_text_mid, task_text_mid2, task_text_big FROM tasks WHERE variant = 1"""
        res = cur.execute(query).fetchall()
    def runmainmenu(self):
        self.stackedWidget.setCurrentWidget(self.mainmenu)

    def runrusvar(self):
        self.stackedWidget.setCurrentWidget(self.variantsrus)

    def startrus(self):
        cur = self.con.cursor()
        query = """SELECT task_text, task_text_mid, task_text_mid2, task_text_big FROM tasks WHERE variant = 1"""
        res = cur.execute(query).fetchall()
        self.stackedWidget.setCurrentWidget(self.variant1rus)
        if self.radioButton_r1.isChecked():
            self.vrRusTsk1_txt.setText(res[0][0])
            self.vrRusTsk1_txt_big.setText(res[0][3])
        if self.radioButton_r2.isChecked():
            self.stackedWidget.setCurrentWidget(self.variant2rus)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
