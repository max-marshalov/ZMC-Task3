from task_window_1 import Ui_MainWindow_1
from dialog import Ui_Dialog_1
from task_window_2 import Ui_MainWindow_2
from dialog_2 import Ui_Dialog_2
from task_window_3 import Ui_MainWindow_3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3


class Dialog(QMainWindow, Ui_Dialog_1):
    def __init__(self, path):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.path = path
        self.date.setDisplayFormat('dd/MM/yyyy')
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        self.sam = self.price.value() * self.count.value()
        self.Sum.display(self.sam)
        self.pushButton_save.clicked.connect(self.save)
        self.price.valueChanged.connect(self.shw)
        self.count.valueChanged.connect(self.shw)
        self.pushButton_close.clicked.connect(self.cls)

    def cls(self):
        self.wind = UI_Task1("bd.db")
        self.wind.show()
        self.close()

    def shw(self):
        self.sam = self.price.value() * self.count.value()
        self.Sum.display(self.sam)

    def save(self):
        try:
            print(self.date.text(),
                  self.prod_name.text(),
                  self.count.value(),
                  self.price.value(),
                  self.sam)
            self.curs.execute(
                """  insert into products(date, prod_name, count, price, sum) values("{}", "{}", {}, {}, {})""".format(

                    self.date.text(),
                    self.prod_name.text(),
                    self.count.value(),
                    self.price.value(),
                    self.sam))  # это обычное число
            print('xxx')
            self.conn.commit()
            self.conn.close()
            print("ok")
        except Exception as er:
            print(er)
        self.cls()


class UI_Task1(QMainWindow, Ui_MainWindow_1):
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
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.pushButton_add.clicked.connect(self.win)
        self.pushButton_add.clicked.connect(self.add_table)
        self.pushButton_close.clicked.connect(self.close)

        self.pushButton_sdelki.clicked.connect(self.go_to_sdelki)
        self.pushButton_buh.clicked.connect(self.go_to_buh)

    def go_to_sdelki(self):
        self.wndw = UI_Task2('bd.db')
        self.close()
        self.wndw.show()

    def go_to_buh(self):
        self.wndw = UI_Task3('bd.db')
        self.close()
        self.wndw.show()

    def get_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        data = cur.execute("SELECT * FROM products").fetchall()
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
        self.tableWidget.setItem(n, 4, QTableWidgetItem())

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


class Dialog_2(QMainWindow, Ui_Dialog_2):
    def __init__(self, path):
        super(Dialog_2, self).__init__()
        self.setupUi(self)
        self.path = path
        self.date.setDisplayFormat('dd/MM/yyyy')
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_close.clicked.connect(self.cls)

    def cls(self):
        self.wind = UI_Task2("bd.db")
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


class UI_Task2(QMainWindow, Ui_MainWindow_2):
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

        self.pushButton_mat.clicked.connect(self.go_to_mat)
        self.pushButton_buh.clicked.connect(self.go_to_buh)

    def go_to_mat(self):
        self.wndw = UI_Task1('bd.db')
        self.close()
        self.wndw.show()

    def go_to_buh(self):
        self.wndw = UI_Task3('bd.db')
        self.close()
        self.wndw.show()

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
        self.dg = Dialog_2(self.path)
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


class UI_Task3(QMainWindow, Ui_MainWindow_3):
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

        self.pushButton_mat.clicked.connect(self.go_to_mat)
        self.pushButton_sdelki.clicked.connect(self.go_to_sdelki)

    def go_to_mat(self):
        self.wndw = UI_Task1('bd.db')
        self.close()
        self.wndw.show()

    def go_to_sdelki(self):
        self.wndw = UI_Task2('bd.db')
        self.close()
        self.wndw.show()

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
    mainWindow = UI_Task1("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
