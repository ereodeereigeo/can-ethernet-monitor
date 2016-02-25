from PySide import QtGui
from ui.disenos.dialogs import dialog_can_bridge


class EthernetDialog(QtGui.QDialog, dialog_can_bridge.Ui_CanBridgeDialog):

    def __init__(self):
        super(EthernetDialog, self).__init__()
        self.setupUi(self)