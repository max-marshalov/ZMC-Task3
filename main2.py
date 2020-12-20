from task_window_2 import Ui_MainWindow_2
from dialog_2 import Ui_Dialog_2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3


class Dialog_2(QMainWindow, Ui_Dialog_2):
    def __init__(self, path, params=None):
        super(Dialog_2, self).__init__()
        self.setupUi(self)
        self.path = path
        self.params = params
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
        if not self.params:
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
        else:
            try:
                print(self.params)
                id = self.curs.execute(
                    """select deal_id from deals where date = "{}" and prod_name = "{}" and client_name = "{}" and price = {}""".format(
                        self.params[0], self.params[1], self.params[2], float(self.params[3]))).fetchone()[0]
                self.curs.execute("""update deals set date = "{}", prod_name = "{}", client_name = "{}", price = {} where deal_id = {}
                """.format(self.date.text(),
                           self.prod_name.text(),
                           self.client_name.text(),
                           self.price.value(), id))
                self.conn.commit()
                self.conn.close()
                self.cls()
            except Exception as er:
                print(er)


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
        self.tableWidget.cellClicked.connect(self.upd)

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
                self.dialog = Dialog_2(self.path, params=x)
                self.dialog.show()
                self.close()

            except Exception as error:
                print(error)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task2("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
