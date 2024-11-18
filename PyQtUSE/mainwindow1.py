import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_main_window2 import Ui_MainWindow
from PyQt6.QtGui import QAction




class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #self.setupUi(self)
        uic.loadUi('main_window3.ui',self)

        self.stackedWidget.setCurrentWidget(self.mainmenu)

        self.variants_rus_act.triggered.connect(self.runrusvar)
        self.main_act.triggered.connect(self.runmainmenu)
        mainmenu_action = QAction("Главное меню", self)
        mainmenu_action.triggered.connect(self.runmainmenu)
        self.menuBar().insertAction(self.menuBar().actions()[0], mainmenu_action)

        self.pushButton.clicked.connect(self.runrusvar)
        self.startrus_btn.clicked.connect(self.startrus)


    def runmainmenu(self):
        self.stackedWidget.setCurrentWidget(self.mainmenu)

    def runrusvar(self):
        self.stackedWidget.setCurrentWidget(self.variantsrus)

    def startrus(self):
        if self.radioButton_r1.isChecked():
            self.stackedWidget.setCurrentWidget(self.variant1rus)
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
