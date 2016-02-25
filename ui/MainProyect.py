import sys
import PySide
from PySide import QtCore
from PySide import QtGui
from ui.disenos.mainwindow import mainwindow


class MainProyect(QtGui.QMainWindow, mainwindow.Ui_MainWindow):

    def __int__(self, parent=None):
        super().__int__()
        self.setupUi(self)

print(PySide.__version__)

app = QtGui.QApplication(sys.argv)
window = MainProyect()
window.show()
app.exec_()