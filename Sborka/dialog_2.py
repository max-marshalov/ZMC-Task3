# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 360)
        Dialog.setMinimumSize(QtCore.QSize(350, 360))
        Dialog.setMaximumSize(QtCore.QSize(350, 360))
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setGeometry(QtCore.QRect(250, 320, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(20, 320, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")
        self.date = QtWidgets.QDateEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(140, 20, 181, 22))
        self.date.setObjectName("date")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.prod_name = QtWidgets.QLineEdit(Dialog)
        self.prod_name.setGeometry(QtCore.QRect(140, 52, 181, 20))
        self.prod_name.setObjectName("prod_name")
        self.price = QtWidgets.QDoubleSpinBox(Dialog)
        self.price.setGeometry(QtCore.QRect(140, 110, 121, 22))
        self.price.setMinimum(0.00)
        self.price.setMaximum(10000000.0)
        self.price.setObjectName("price")
        self.client_name = QtWidgets.QLineEdit(Dialog)
        self.client_name.setGeometry(QtCore.QRect(140, 80, 181, 20))
        self.client_name.setObjectName("client_name")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_close.setText(_translate("Dialog", "Закрыть"))
        self.label.setText(_translate("Dialog", "Дата"))
        self.label_2.setText(_translate("Dialog", "Название"))
        self.label_3.setText(_translate("Dialog", "Покупатель"))
        self.pushButton_save.setText(_translate("Dialog", "Сохранить"))
        self.label_4.setText(_translate("Dialog", "Цена"))
