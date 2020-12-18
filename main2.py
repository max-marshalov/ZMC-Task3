from task_window_2 import Ui_MainWindow
from dialog_2 import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3


class Dialog(QMainWindow, Ui_Dialog):
    def __init__(self, path):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.path = path
        self.date.setDisplayFormat('dd/MM/yyyy')
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_close.clicked.connect(self.cls)

    def cls(self):
        self.wind = UI_Task1("bd.db")
        self.wind.show()
        self.close()

    def save(self):
        try:
            print(self.date.text(),
                  self.prod_name.text(),
                  self.client_name.text(),
                  self.price.value())
            self.curs.execute(
                """  insert into deals(date, prod_name, client_name, price) values("{}", "{}", "{}", {})""".format(

                    self.date.text(),
                    self.prod_name.text(),
                    self.client_name.text(),
                    self.price.value()))  # это обычное число
            print('xxx')
            self.conn.commit()
            self.conn.close()
            print("ok")
        except Exception as er:
            print(er)
        self.cls()


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.setupUi(self)
        self.data = self.get_data()
        for i in range(len(self.data)):
            self.add()
        self.update_list()

        self.rows = self.tableWidget.rowCount() + 1
        self.t = 1

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.pushButton_add.clicked.connect(self.win)
        self.pushButton_add.clicked.connect(self.add_table)
        self.pushButton_close.clicked.connect(self.close)

    def get_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        data = cur.execute("SELECT * FROM deals").fetchall()
        con.close()
        print(data)
        return data

    def add(self):
        n = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(n + 1)
        self.tableWidget.setItem(n, 0, QTableWidgetItem())
        self.tableWidget.setItem(n, 1, QTableWidgetItem())
        self.tableWidget.setItem(n, 2, QTableWidgetItem())
        self.tableWidget.setItem(n, 3, QTableWidgetItem())

    def add_table(self):
        self.tableWidget.setRowCount(self.rows)
        self.rows += 1

    def win(self):
        self.dg = Dialog(self.path)
        self.dg.show()
        self.close()

    def update_list(self):
        try:
            self.data[self.tableWidget.rowCount() - 1][self.tableWidget.columnCount()]
            for i in range(self.tableWidget.rowCount()):
                for j in range(self.tableWidget.columnCount()):
                    self.tableWidget.item(i, j).setText(str(self.data[i][j + 1]))
        except Exception as error:
            QMessageBox.critical(self, "Ошибка", "Сохраните данные перед тем как выполнять сортировку", QMessageBox.Ok)
            print(error, "update_list")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
