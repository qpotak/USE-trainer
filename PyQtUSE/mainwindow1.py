import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window1.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        pass
        self.label.setText("OK")

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
