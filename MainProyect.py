from ui.disenos.mainwindow import mainwindow
from PySide import QtGui
from PySide import QtCore


class MainProyect(QtGui.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self):
        super(MainProyect, self).__init__()
        self.setupUi(self)

app = QtGui.QApplication([])
window = MainProyect()
window.show()
app.exec_()