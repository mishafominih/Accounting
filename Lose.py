# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lose.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1119, 838)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 1061, 401))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.AddButton = QtWidgets.QPushButton(self.groupBox)
        self.AddButton.setGeometry(QtCore.QRect(810, 320, 231, 61))
        self.AddButton.setObjectName("AddButton")
        self.Count = QtWidgets.QLineEdit(self.groupBox)
        self.Count.setGeometry(QtCore.QRect(150, 51, 121, 31))
        self.Count.setObjectName("Count")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 151, 31))
        self.label.setObjectName("label")
        self.Target = QtWidgets.QLineEdit(self.groupBox)
        self.Target.setGeometry(QtCore.QRect(430, 50, 601, 31))
        self.Target.setObjectName("Target")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(310, 49, 151, 31))
        self.label_2.setObjectName("label_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 120, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Добавить расходы"))
        self.AddButton.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "Сколько?"))
        self.label_2.setText(_translate("Dialog", "На что?"))