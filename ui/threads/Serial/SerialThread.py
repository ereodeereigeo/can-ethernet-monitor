import ui.threads.Serial
from PySide import QtCore


class SerialThread(QtCore.QThread):

    def __init__(self):
        super(SerialThread, self).__init__()
        self._serial_configuration = dict(port='', speed=0)

    def __setitem__(self, key, value):
        self._serial_configuration[key] = value

    def __str__(self):
        return 'puerto: {}, baud: {}'.format(self._serial_configuration['port'], self._serial_configuration['speed'])

    def abrir_puerto(self):
        pass

    def protocolo(self):
        pass

    def start(self, *args, **kwargs):
        pass