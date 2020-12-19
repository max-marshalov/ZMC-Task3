from task_window_3 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3


class UI_Task3(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super().__init__()
        self.setupUi(self)
        self.path = path
        self.calendarWidget.selectionChanged.connect(self.calendar)
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        try:
            self.un = self.curs.execute(
                """select sum(price) from deals""").fetchone()[0] - \
                      self.curs.execute("""select sum(sum) from products""").fetchone()[0]
            self.unity_cash.setText(str(self.un))
        except Exception as er:
            print(er)

    def calendar(self):
        self.date = self.calendarWidget.selectedDate().toString('dd/MM/yyyy')
        try:
            self.dc1 = self.curs.execute(
                """select sum(price) from deals where deals.date = "{}" """.format(self.date)).fetchone()[0]
            self.dc2 = self.curs.execute(
                """select sum(sum) from products where products.date = "{}" """.format(self.date)).fetchone()[
                0]
            if not self.dc1:
                if not self.dc2:
                    self.dc = 0
                else:
                    self.dc = 0 - self.dc2
            elif not self.dc2:
                if not self.dc1:
                    self.dc = 0
                else:
                    self.dc = self.dc1
            else:
                self.dc = self.dc1 - self.dc2
            self.date_cash.setText(str(self.dc))
        except Exception as er:
            print(er)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task3("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
