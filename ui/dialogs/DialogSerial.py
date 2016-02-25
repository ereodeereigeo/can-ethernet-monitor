
from PySide import QtGui
from ui.disenos.dialogs import dialog_puerto_com


class SerialDialog(QtGui.QDialog, dialog_puerto_com.Ui_SerialDialog):

    def __init__(self):
        super(SerialDialog, self).__init__()
        self.setupUi(self)