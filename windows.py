from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import Start
import Add
import Works
import Lose
import Result
import Form
import Database as db
import traceback
from datetime import date

DATETIME_FORMAT = "yyyy-MM-dd"

class addWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(addWindow, self).__init__(parent)
        self.ui = Add.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.BackButton.clicked.connect(self.BackBtnClicked)

        self.ui.AddButton.clicked.connect(self.AddBtnClicked)

        self.ui.AddWorkButton.clicked.connect(self.AddWorkBtnClicked)

        self.ui.DelWorkButton.clicked.connect(self.DelWorkBtnClicked)

        self.ui.WorksBox.addItems(db.Database.GetTypesWork())

    def BackBtnClicked(self):
        self.close()

    def AddWorkBtnClicked(self):
        work = self.ui.WorksBox.currentText()
        self.ui.listWidget.addItem(work)

    def DelWorkBtnClicked(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.count() - 1)

    def AddBtnClicked(self):
        items = []
        #while self.ui.listWidget.count() > 0:
        #    items.append(self.ui.listWidget.takeItem(0).text())
        str = self.ui.calendarWidget.selectedDate().toString(DATETIME_FORMAT)
        s = self.ui.listWidget.takeItem(0).text()
        data = db.DataOrders(
            int(self.ui.PhoneNumber.text()),
            int(self.ui.Cast.text()),
            float(self.ui.Time.text()),
            s,
            self.ui.Name.text(),
            self.ui.Car.text(),
            str,
            int(self.ui.Cast_2.text())
        )
        #try:
        db.Database.AddData(data)
        #except ValueError:
            #print(traceback.format_exc())


class WorksWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WorksWindow, self).__init__(parent)
        self.ui = Works.Ui_Dialog()
        self.ui.setupUi(self)

        self._Fill()

        self.ui.AddButton.clicked.connect(self.AddBtnClicked)
        self.ui.DelButton.clicked.connect(self.DelBtnClicked)

    def AddBtnClicked(self):
        str = self.ui.AddLine.text()
        self.ui.listWidget.addItem(str)
        db.Database.AddTypeWork(str)
        self.ui.AddLine.clear()

    def DelBtnClicked(self):
        str = self.ui.DelLine.text()
        self.ui.listWidget.clear()
        db.Database.DeleteWork(str)
        self._Fill()
        self.ui.DelLine.clear()

    def _Fill(self):
        works = db.Database.GetTypesWork()
        self.ui.listWidget.addItems(works)


class LoseWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoseWindow, self).__init__(parent)
        self.ui = Lose.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.AddButton.clicked.connect(self.AddBtnClicked)
        self.ui.DelButton.clicked.connect(self.DelBtnClicked)

        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setColumnWidth(0, 125)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 500)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Дата', 'Количество', 'Цель')
        )
        self.Update()

    def Update(self):
        self.ui.tableWidget.clear()
        list = db.Database.GetExpenses('0000-00-00', date.today())
        self.ui.tableWidget.setRowCount(len(list))

        row = 0
        for tup in list[::-1]:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item.__str__())
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def AddBtnClicked(self):
        lose = db.DataExpenses(
            self.ui.calendarWidget.selectedDate().toString(DATETIME_FORMAT),
            int(self.ui.Count.text()),
            self.ui.Target.text()
        )
        db.Database.AddExpenses(lose)
        self.ui.Target.clear()
        self.ui.Count.clear()
        self.Update()

    def DelBtnClicked(self):
        items = []
        for e in self.ui.tableWidget.selectedItems():
            items.append(e.text())
        if len(items) > 0:
            db.Database.DeleteExpenses(items[0], items[1], items[2])
            self.Update()


class ResultWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ResultWindow, self).__init__(parent)
        self.ui = Result.Ui_Dialog()
        self.ui.setupUi(self)


class FormWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FormWindow, self).__init__(parent)
        self.ui = Form.Ui_Dialog()
        self.ui.setupUi(self)


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Start.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.AddButton.clicked.connect(self.AddBtnClicked)

        self.ui.WorksButton.clicked.connect(self.WorksBtnClicked)

        self.ui.LoseButton.clicked.connect(self.LoseBtnClicked)

        self.ui.ResultButton.clicked.connect(self.ResultBtnClicked)

        self.ui.FormButton.clicked.connect(self.FormBtnClicked)

    def AddBtnClicked(self):
        self.dialog = addWindow(self)
        self.dialog.show()

    def WorksBtnClicked(self):
        self.dialog = WorksWindow(self)
        self.dialog.show()

    def LoseBtnClicked(self):
        self.dialog = LoseWindow(self)
        self.dialog.show()

    def ResultBtnClicked(self):
        self.dialog = ResultWindow(self)
        self.dialog.show()

    def FormBtnClicked(self):
        self.dialog = FormWindow(self)
        self.dialog.show()


