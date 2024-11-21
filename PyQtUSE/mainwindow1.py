import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from ui_main_window import Ui_MainWindow
from PyQt6.QtGui import QAction
import sqlite3


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('main_window3.ui',self)

        self.stackedWidget.setCurrentWidget(self.mainmenu)

        self.variants_rus_act.triggered.connect(self.runrusvar)
        self.main_act.triggered.connect(self.runmainmenu)
        mainmenu_action = QAction("Главное меню", self)
        mainmenu_action.triggered.connect(self.runmainmenu)
        self.menuBar().insertAction(self.menuBar().actions()[0], mainmenu_action)

        self.pushButton.clicked.connect(self.runrusvar)
        self.startrus_btn.clicked.connect(self.startrus)
        self.pushButton.clicked.connect(self.runrusvar)
        self.check_btn.clicked.connect(self.cheking)

        self.con = sqlite3.connect('use_tasks.db')

        self.answeredt = [self.tsk1ans, self.tsk2ans, self.tsk3ans, self.tsk4ans, self.tsk5ans, self.tsk6ans,
                          self.tsk7ans, self.tsk8ans, self.tsk9ans, self.tsk10ans, self.tsk11ans, self.tsk12ans,
                          self.tsk13ans, self.tsk14ans, self.tsk15ans, self.tsk16ans, self.tsk17ans, self.tsk18ans,
                          self.tsk19ans, self.tsk20ans, self.tsk21ans, self.tsk22ans, self.tsk23ans, self.tsk24ans,
                          self.tsk25ans, self.tsk26ans]

    def loadvr(self):
        cur = self.con.cursor()
        query = """SELECT task_text, task_text_mid, task_text_mid2, task_text_big FROM tasks WHERE variant = 1"""
        res = cur.execute(query).fetchall()

    def runmainmenu(self):
        self.stackedWidget.setCurrentWidget(self.mainmenu)

    def runrusvar(self):
        self.stackedWidget.setCurrentWidget(self.variantsrus)

    def cheking(self):
        answers = []
        for edt in self.answeredt:
            if edt.text().strip():
                answers.append(edt.text().strip())
            else:
                answers.append('нет ответа')
        cur = self.con.cursor()
        if self.radioButton_r1.isChecked():
            v = 1
        elif self.radioButton_r2.isChecked():
            v = 2
        elif self.radioButton_r3.isChecked():
            v = 3
        query = f"""SELECT answer FROM tasks WHERE variant = {v}"""
        res = cur.execute(query).fetchall()
        correct_answers = [row[0] for row in res]
        tablelist = []
        for i in range(len(answers)):
            if answers[i] == correct_answers[i]:
                tablelist.append('Верно')
            elif answers[i] == 'нет ответа':
                tablelist.append('Нет ответа')
            else:
                tablelist.append('Не верно')
        print(tablelist)
        self.results_tbl.setRowCount(len(answers))
        for row in range(len(answers)):
            self.results_tbl.setItem(row, 0, QTableWidgetItem(answers[row]))
            self.results_tbl.setItem(row, 1, QTableWidgetItem(correct_answers[row]))
            self.results_tbl.setItem(row, 2, QTableWidgetItem(tablelist[row]))

    def startrus(self):
        if self.radioButton_r1.isChecked():
            n = 0
            vd = 1
        if self.radioButton_r2.isChecked():
            n = 27
            vd = 2
        if self.radioButton_r2.isChecked():
            n = 54
            vd = 3
        cur = self.con.cursor()
        query = f"""SELECT task_text, task_text_mid, task_text_mid2, task_text_big FROM tasks WHERE variant = {vd}"""
        res = cur.execute(query).fetchall()
        self.stackedWidget.setCurrentWidget(self.variant1rus)

        self.vrRusTsk1_txt.setText(res[n][0])
        self.vrRusTsk1_txt_big.setText(res[n][3])

        self.vrRusTsk2_txt.setText(res[n + 1][0])
        self.vrRusTsk2_txt_big.setText(res[n + 1][3])
        self.vrRusTsk2_txt_mid.setText(res[n + 1][1])

        self.vrRusTsk3_txt.setText(res[n + 2][0])
        self.vrRusTsk3_txt_big.setText(res[n + 2][3])
        self.vrRusTsk3_txt_mid.setText(res[n + 2][1])

        self.vrRusTsk4_txt.setText(res[n + 3][0])
        self.vrRusTsk4_txt_mid.setText(res[n + 3][1])

        self.vrRusTsk5_txt.setText(res[n + 4][0])
        self.vrRusTsk5_txt_mid.setText(res[n + 4][1])

        self.vrRusTsk6_txt.setText(res[n + 5][0])
        self.vrRusTsk6_txt_mid.setText(res[n + 5][1])

        self.vrRusTsk7_txt.setText(res[n + 6][0])
        self.vrRusTsk7_txt_mid.setText(res[n + 6][1])

        self.vrRusTsk8_txt.setText(res[n + 7][0])
        self.vrRusTsk8_txt_mid.setText(res[n + 7][1])
        self.vrRusTsk8_txt_mid2.setText(res[n + 7][2])

        self.vrRusTsk9_txt.setText(res[n + 8][0])
        self.vrRusTsk9_txt_mid.setText(res[n + 8][1])

        self.vrRusTsk10_txt.setText(res[n + 9][0])
        self.vrRusTsk10_txt_mid.setText(res[n + 9][1])

        self.vrRusTsk11_txt.setText(res[n + 10][0])
        self.vrRusTsk11_txt_mid.setText(res[n + 10][1])

        self.vrRusTsk12_txt.setText(res[n + 11][0])
        self.vrRusTsk12_txt_mid.setText(res[n + 11][1])

        self.vrRusTsk13_txt.setText(res[n + 12][0])
        self.vrRusTsk13_txt_mid.setText(res[n + 12][1])

        self.vrRusTsk14_txt.setText(res[n + 13][0])
        self.vrRusTsk14_txt_mid.setText(res[n + 13][1])

        self.vrRusTsk15_txt.setText(res[n + 14][0])
        self.vrRusTsk15_txt_mid.setText(res[n + 14][1])

        self.vrRusTsk16_txt.setText(res[n + 15][0])
        self.vrRusTsk16_txt_mid.setText(res[n + 15][1])

        self.vrRusTsk17_txt.setText(res[n + 16][0])
        self.vrRusTsk17_txt_mid.setText(res[n + 16][1])

        self.vrRusTsk18_txt.setText(res[n + 17][0])
        self.vrRusTsk18_txt_mid.setText(res[n + 17][1])

        self.vrRusTsk19_txt.setText(res[n + 18][0])
        self.vrRusTsk19_txt_mid.setText(res[n + 18][1])

        self.vrRusTsk20_txt.setText(res[n + 19][0])
        self.vrRusTsk20_txt_mid.setText(res[n + 19][1])

        self.vrRusTsk21_txt.setText(res[n + 20][0])
        self.vrRusTsk21_txt_mid.setText(res[n + 20][1])

        self.vrRusTsk22_txt.setText(res[n + 21][0])
        self.vrRusTsk22_txt_mid.setText(res[n + 21][1])
        self.vrRusTsk22_txt_mid2.setText(res[n + 21][2])

        self.vrRusTsk23_txt.setText(res[n + 22][0])
        self.vrRusTsk23_txt_mid.setText(res[n + 22][1])
        self.vrRusTsk23_txt_big.setText(res[n + 22][3])

        self.vrRusTsk24_txt.setText(res[n + 23][0])
        self.vrRusTsk24_txt_mid.setText(res[n + 23][1])
        self.vrRusTsk24_txt_big.setText(res[n + 23][3])

        self.vrRusTsk25_txt.setText(res[n + 24][0])
        self.vrRusTsk25_txt_big.setText(res[n + 24][3])

        self.vrRusTsk26_txt.setText(res[n + 25][0])
        self.vrRusTsk26_txt_big.setText(res[n + 25][3])

        self.vrRusTsk27_txt.setText(
            f"""
            Напишите сочинение-рассуждение по проблеме исходного текста «{res[n + 26][0]}» Сформулируйте позицию автора (рассказчика) по указанной проблеме.
            Прокомментируйте, как в тексте раскрывается эта позиция. Включите в комментарий два примера-иллюстрации из прочитанного текста, важные для понимания позиции автора (рассказчика), и поясните их. Укажите и поясните смысловую связь между приведёнными примерами-иллюстрациями. 
            Сформулируйте и обоснуйте своё отношение к позиции автора (рассказчика) по проблеме исходного текста. Включите в обоснование пример-аргумент, опираясь на читательский, историко-культурный или жизненный опыт.
            (Не допускается обращение к таким жанрам, как комикс, аниме, манга, фанфик, графический роман, компьютерная игра.) Объём сочинения  — не менее 150 слов.
            Работа, написанная без опоры на прочитанный текст (не по данному тексту) или не самостоятельно, не оценивается. Если сочинение представляет собой полностью переписанный или пересказанный исходный текст без каких бы то ни было комментариев, такая работа оценивается 0 баллов. 
            Сочинение пишите аккуратно и разборчиво, соблюдая нормы современного русского литературного языка."""
        )
        self.vrRusTsk27_txt_big.setText(res[n + 26][3])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
