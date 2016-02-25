import socket
from PySide import QtCore


class EthernetThread(QtCore.QThread):

    def __init__(self):
        super(EthernetThread, self).__init__()
        self._socket_configuration = dict(port=1, ip=())

    def __setitem__(self, key, value):
        if key == 'ip':
            assert isinstance(value, tuple), 'la ip debe ser una tupla'
            assert len(value) == 4, 'formato de la ip incorrecto: {}'.format(value)
            self._socket_configuration['ip'] = value
        elif key == 'port':
            assert isinstance(value, int), 'el puerto debe ser un valor entero'
            self._socket_configuration['port'] = value

    def __repr__(self):
        return 'Socket Thread conectado a: ip: {}, puerto: {}'.format(self._socket_configuration['ip'],
                                                                      self._socket_configuration['port'])

    def __getitem__(self, item):
        return self._socket_configuration[item]

    def conectarse(self):
        pass

    def desconectarse(self):
        pass

    def start(self, *args, **kwargs):
        pass