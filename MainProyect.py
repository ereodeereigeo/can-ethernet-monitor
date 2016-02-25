from PySide import QtGui
from PySide import QtCore
from ui.disenos.mainwindow import mainwindow
from ui.Motor.MotorModel import MotorModel
from ui.threads.Ethernet import EthernetThread, ethernet_protocol
from ui.threads.Serial import SerialThread, serial_protocol


class MainProyect(QtGui.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self):
        super(MainProyect, self).__init__()
        self.setupUi(self)
        self.motor1 = MotorModel()
        self.motor2 = MotorModel()
        self.serialthread = SerialThread.SerialThread()
        self.ethernetthread = EthernetThread.EthernetThread()

    @QtCore.Slot(dict)
    def recivir_serial(self):
        pass

    @QtCore.Slot(dict)
    def recivir_socket(self):
        pass

    def iniciar_comunicacion_socket(self):
        pass

    def iniciar_comunicacion_serial(self):
        pass

app = QtGui.QApplication([])
window = MainProyect()
window.show()
app.exec_()