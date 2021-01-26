import  random

from PyQt5 import QtWidgets
import  windows as w
import sys

app = QtWidgets.QApplication([])

application = w.StartWindow()
application.show()

sys.exit(app.exec())