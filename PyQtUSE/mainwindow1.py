import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window2.ui', self)

        self.stackedWidget.setCurrentWidget(self.mainmenu)

        self.pushButton.clicked.connect(self.runrusvar)
        self.startrus_btn.clicked.connect(self.startrus)
        self.v1r_btn_to_vr.clicked.connect(self.runrusvar)
        self.v2r_btn_to_vr.clicked.connect(self.runrusvar)

    def runrusvar(self):
        self.label.setText("OK")
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
