from PyQt5 import QtWidgets
import Start
import Add
import Works
import Lose
import Result
import Form
import Database as db

class addWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(addWindow, self).__init__(parent)
        self.ui = Add.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.BackButton.clicked.connect(self.BackBtnClicked)

        self.ui.AddButton.clicked.connect(self.AddBtnClicked)

    def BackBtnClicked(self):
        self.close()

    def AddBtnClicked(self):
        pn = int(self.ui.PhoneNumber.text())
        c = int(self.ui.Cast.text())
        t = float(self.ui.Time.text())
        n = self.ui.Name.text()
        r = self.ui.Car.text()
        data = db.DataOrders(
            100,
            pn,
            c,
            t,
            "временно",
            n,
            r
        )
        db.Database.AddOrders(data)


class WorksWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(WorksWindow, self).__init__(parent)
        self.ui = Works.Ui_Dialog()
        self.ui.setupUi(self)

        #self.ui.listWidget.addItems(["1", "2", "3"])

        self.ui.AddButton.clicked.connect(self.AddBtnClicked)
        self.ui.DelButton.clicked.connect(self.DelBtnClicked)

    def AddBtnClicked(self):
        self.ui.listWidget.addItem(self.ui.AddLine.text())

    def DelBtnClicked(self):
        return 0


class LoseWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoseWindow, self).__init__(parent)
        self.ui = Lose.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.AddButton.clicked.connect(self.AddBtnClicked)

    def AddBtnClicked(self):
        return 0


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


