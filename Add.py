# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1121, 840)
        self.AddButton = QtWidgets.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(660, 750, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddButton.setFont(font)
        self.AddButton.setObjectName("AddButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 1041, 641))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 50, 191, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 180, 91, 31))
        self.label_2.setObjectName("label_2")
        self.Car = QtWidgets.QLineEdit(self.groupBox)
        self.Car.setGeometry(QtCore.QRect(320, 180, 261, 31))
        self.Car.setObjectName("Car")
        self.PhoneNumber = QtWidgets.QLineEdit(self.groupBox)
        self.PhoneNumber.setGeometry(QtCore.QRect(320, 60, 261, 31))
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 110, 71, 41))
        self.label_3.setObjectName("label_3")
        self.Name = QtWidgets.QLineEdit(self.groupBox)
        self.Name.setGeometry(QtCore.QRect(320, 120, 261, 31))
        self.Name.setObjectName("Name")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 240, 121, 31))
        self.label_4.setObjectName("label_4")
        self.Cast = QtWidgets.QLineEdit(self.groupBox)
        self.Cast.setGeometry(QtCore.QRect(320, 240, 261, 31))
        self.Cast.setObjectName("Cast")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(230, 360, 71, 31))
        self.label_5.setObjectName("label_5")
        self.Time = QtWidgets.QLineEdit(self.groupBox)
        self.Time.setGeometry(QtCore.QRect(320, 360, 261, 31))
        self.Time.setObjectName("Time")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 281, 31))
        self.label_6.setObjectName("label_6")
        self.Cast_2 = QtWidgets.QLineEdit(self.groupBox)
        self.Cast_2.setGeometry(QtCore.QRect(320, 300, 261, 31))
        self.Cast_2.setObjectName("Cast_2")
        self.BackButton = QtWidgets.QPushButton(Dialog)
        self.BackButton.setGeometry(QtCore.QRect(40, 750, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AddButton.setText(_translate("Dialog", "Добавить"))
        self.groupBox.setTitle(_translate("Dialog", "Информация"))
        self.label.setText(_translate("Dialog", "Номер телефона:"))
        self.label_2.setText(_translate("Dialog", "Машина:"))
        self.label_3.setText(_translate("Dialog", "ФИО:"))
        self.label_4.setText(_translate("Dialog", "Стоимость:"))
        self.label_5.setText(_translate("Dialog", "Время:"))
        self.label_6.setText(_translate("Dialog", "Амортизация отчислений:"))
        self.BackButton.setText(_translate("Dialog", "Назад"))
