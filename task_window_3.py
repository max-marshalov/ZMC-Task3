# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_window_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 361, 211))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.unity_cash = QtWidgets.QLabel(self.centralwidget)
        self.unity_cash.setGeometry(QtCore.QRect(140, 220, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unity_cash.setFont(font)
        self.unity_cash.setObjectName("unity_cash")
        self.date_cash = QtWidgets.QLabel(self.centralwidget)
        self.date_cash.setGeometry(QtCore.QRect(140, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_cash.setFont(font)
        self.date_cash.setObjectName("date_cash")
        self.pushButton_sdelki = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sdelki.setGeometry(QtCore.QRect(420, 330, 75, 23))
        self.pushButton_sdelki.setObjectName("pushButton_sdelki")
        self.pushButton_mat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mat.setGeometry(QtCore.QRect(330, 330, 75, 23))
        self.pushButton_mat.setObjectName("pushButton_mat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Общий доход:"))
        self.label_6.setText(_translate("MainWindow", "Доход за день:"))
        self.unity_cash.setText(_translate("MainWindow", "0"))
        self.date_cash.setText(_translate("MainWindow", "0"))
        self.pushButton_sdelki.setText(_translate("MainWindow", "Сделки"))
        self.pushButton_mat.setText(_translate("MainWindow", "Расходники"))
