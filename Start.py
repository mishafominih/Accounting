# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1122, 842)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 1071, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.AddButton = QtWidgets.QPushButton(self.groupBox)
        self.AddButton.setGeometry(QtCore.QRect(30, 40, 261, 71))
        self.AddButton.setObjectName("AddButton")
        self.WorksButton = QtWidgets.QPushButton(self.groupBox)
        self.WorksButton.setGeometry(QtCore.QRect(380, 40, 281, 71))
        self.WorksButton.setObjectName("WorksButton")
        self.LoseButton = QtWidgets.QPushButton(self.groupBox)
        self.LoseButton.setGeometry(QtCore.QRect(750, 40, 281, 71))
        self.LoseButton.setObjectName("LoseButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 190, 1071, 631))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.ResultButton = QtWidgets.QPushButton(self.groupBox_2)
        self.ResultButton.setGeometry(QtCore.QRect(30, 50, 261, 71))
        self.ResultButton.setAcceptDrops(False)
        self.ResultButton.setCheckable(False)
        self.ResultButton.setAutoRepeat(False)
        self.ResultButton.setAutoExclusive(False)
        self.ResultButton.setObjectName("ResultButton")
        self.FindButton = QtWidgets.QPushButton(self.groupBox_2)
        self.FindButton.setGeometry(QtCore.QRect(30, 160, 261, 71))
        self.FindButton.setObjectName("FindButton")
        self.FormButton = QtWidgets.QPushButton(self.groupBox_2)
        self.FormButton.setGeometry(QtCore.QRect(390, 50, 271, 71))
        self.FormButton.setObjectName("FormButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "работа"))
        self.AddButton.setText(_translate("Dialog", "Добавить заказ"))
        self.WorksButton.setText(_translate("Dialog", "Виды работ"))
        self.LoseButton.setText(_translate("Dialog", "Добавить расходы"))
        self.groupBox_2.setTitle(_translate("Dialog", "Статистика"))
        self.ResultButton.setText(_translate("Dialog", "Итоги"))
        self.FindButton.setText(_translate("Dialog", "Поиск"))
        self.FormButton.setText(_translate("Dialog", "Получить отчет"))
