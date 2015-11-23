# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import codecs
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import socket
import struct
import binascii
from collections import deque
from decodificador.decodificador import VariablesCan

decoder = VariablesCan()

multicast_group = '239.255.60.60'
server_addres = ('', 4876)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_addres)
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
# mw = QtGui.QMainWindow()
# mw.resize(800,800)
pg.setConfigOption('background', 'w')
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000, 600)
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

# añadir diccionario de identificadores



# terminar con manual del motor
# b'501' : [ ['current_setpoint'],['speed_setpoint']],\
# b'502' : [['bus_current_setpoint']]
# funciones de conversión de datos



def update():
    global curve1, curve2, curve3, historicos_temperatura_CELDA, historicos_temperatura_PCB, historico_voltaje_bus_dc,\
        p1, p2
    try:
        data, address = sock.recvfrom(1024)
        hexdata = binascii.hexlify(data)
        listaid = []
        inicio = 37
        fin = 40
        ident = '0'
        # print (hexdata)
        while len(ident) > 0:
            ident = hexdata[inicio:fin]
            listaid.append(ident)
            inicio += 28
            fin += 28
        inicio_datos = 44
        for key in listaid:

            identificadores = decoder.identificadores(key)

            for elemento in identificadores:

                tipo, largo = decoder.return_data(key, elemento)
                fin_datos = inicio_datos + largo
                dato = hexdata[inicio_datos:fin_datos]
                # print (dato)
                # invertir dato
                n = 2
                dato_der = [dato[i: i + n] for i in range(0, len(dato), n)]
                dato_inv = b''.join(dato_der[::-1])
                # print (dato_inv)
                # hacer conversión
                dato_conv = decoder.conversion_data(dato_inv, tipo)

                print(elemento, '= ', dato_conv)
                inicio_datos = inicio_datos + elemento[1]
            inicio_datos += 12
        '''if identificador == filtro_temperatura:


            temperatura

            temperatura_pcb = hexdata[-8:-4]
            temperatura_celda = hexdata[-4::]

            temperatura_pcb = int(temperatura_pcb[2:4] + temperatura_pcb[0:2], 16)/10.0
            temperatura_celda = int(temperatura_celda[2:4] + temperatura_celda[0:2], 16)/10.0

            historicos_temperatura_CELDA.append(temperatura_celda)
            historicos_temperatura_PCB.append(temperatura_pcb)

            curve1.setData(historicos_temperatura_PCB)
            curve2.setData(historicos_temperatura_CELDA)

        if identificador == filtro_wavescultor:
            voltaje = hexdata[-16:-8]
            voltaje = voltaje[6:8] + voltaje[4:6] + voltaje[2:4] + voltaje[0:2]
            float_voltaje = struct.unpack('!f', codecs.decode(voltaje,'hex'))[0]
            print(float_voltaje)
            
            historico_voltaje_bus_dc.append(float_voltaje)
            curve3.setData(historico_voltaje_bus_dc)
        '''
    except KeyboardInterrupt:
        sock.close()


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
