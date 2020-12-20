from task_window_1 import Ui_MainWindow_1
from dialog import Ui_Dialog_1
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3


class Dialog(QMainWindow, Ui_Dialog_1):
    def __init__(self, path, params=None):
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
        self.params = params

    def cls(self):
        self.wind = UI_Task1("bd.db")
        self.wind.show()
        self.close()

    def shw(self):
        self.sam = self.price.value() * self.count.value()
        self.Sum.display(self.sam)

    def save(self):
        if not self.params:
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
        else:
            try:
                print(self.params)
                id = self.curs.execute(
                    """select prod_id from products where date = "{}" and prod_name = "{}" and count = {} and price = {} and sum = {}""".format(
                        self.params[0], self.params[1], int(self.params[2]), float(self.params[3]),
                        float(self.params[4]))).fetchone()[0]
                self.curs.execute("""update products set date = "{}", prod_name = "{}", count = {}, price = {}, sum = {} where prod_id = {}
                """.format(self.date.text(),
                           self.prod_name.text(),
                           self.count.value(),
                           self.price.value(),
                           self.sam, id))
                self.conn.commit()
                self.conn.close()
                self.cls()
            except Exception as er:
                print(er)


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
        self.tableWidget.cellClicked.connect(self.upd)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.pushButton_add.clicked.connect(self.win)
        self.pushButton_add.clicked.connect(self.add_table)
        self.pushButton_close.clicked.connect(self.close)

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

    def upd(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        # msg.setIconPixmap(pixmap)  # Своя картинка

        msg.setWindowTitle("Изменить данные")
        msg.setText("Вы хотите изменить данные?")
        # msg.setInformativeText("Хотите сохранить информацию перед выходом?")

        msg.addButton('Отмена', QMessageBox.YesRole)
        ok_button = msg.addButton('Изменить', QMessageBox.AcceptRole)
        # close_button = msg.addButton('Закрыть', QMessageBox.RejectRole)

        msg.exec()
        if msg.clickedButton() == ok_button:
            try:
                a = self.tableWidget.currentRow()
                x = []
                for i in range(self.tableWidget.columnCount()):
                    x.append(self.tableWidget.item(a, i).text())
                self.dialog = Dialog(self.path, params=x)
                self.dialog.show()
                self.close()

            except Exception as error:
                print(error)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
