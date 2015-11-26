from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import socket
import struct
import binascii
from collections import deque

multicast_group = '239.255.60.60'
server_addres = ('', 4876)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_addres)
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

filtro_temperatura = b'601'
filtro_volt = b'602'
filtro_wavescultor = b'442'

# QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
# mw = QtGui.QMainWindow()
# mw.resize(800,800)
pg.setConfigOption('background', 'w')
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Updating plot")
p1.addLegend()
p1.setXRange(0, 100)
p1.setYRange(20, 30)
win.nextRow()

p2 = win.addPlot(title="Updating plot")
p2.setXRange(0, 100)
p2.setYRange(0, 20)
p2.addLegend()

curve1 = p1.plot(pen='y', name='TEMPERATURA PCB')
curve2 = p1.plot(pen='r', name='TEMPERATURA CELDA')

curve3 = p2.plot(pen='r', name='VOLTAJE BUS')

historicos_temperatura_PCB = deque([], maxlen=100)
historicos_temperatura_CELDA = deque([], maxlen=100)

historico_voltaje_bus_dc = deque([], maxlen=100)

def update():
    global curve1, curve2, curve3, historicos_temperatura_CELDA, historicos_temperatura_PCB, historico_voltaje_bus_dc, p1, p2
    try:
        data, address = sock.recvfrom(1024)
        hexdata = binascii.hexlify(data)
        identificador = hexdata[37:40]
        if identificador == filtro_temperatura:

            '''
            temperatura
            '''
            temperatura_pcb = hexdata[-8:-4]
            temperatura_celda = hexdata[-4::]

            temperatura_pcb = int(temperatura_pcb[2:4] + temperatura_pcb[0:2], 16)/10.0
            temperatura_celda = int(temperatura_celda[2:4] + temperatura_celda[0:2], 16)/10.0

            historicos_temperatura_CELDA.append(temperatura_celda)
            historicos_temperatura_PCB.append(temperatura_pcb)

            curve1.setData(historicos_temperatura_PCB)
            curve2.setData(historicos_temperatura_CELDA)

        elif identificador == filtro_wavescultor:
            temperatura = hexdata[-16:-8]
            temperatura = temperatura[6:8] + temperatura[4:6] + temperatura[2:4] + temperatura[0:2]
            historico_voltaje_bus_dc.append(struct.unpack('!f', codecs.decode(temperatura))[0])
            curve3.setData(historico_voltaje_bus_dc)

    except KeyboardInterrupt:
        sock.close()


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
