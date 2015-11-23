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
dicc_variables = {
    b'400': [['ident_m1', 8, 'uint32'], ['tritium_id_m1', 8, 'uint32']],
    b'440': [['ident_m2', 8, 'uint32'], ['tritium_id_m2', 8, 'uint32']],
    b'401': [['receive_error_count_m1', 2, 'uint8'], ['transmit_error_count_m1', 2, 'uint8'],
             ['active_motor_m1', 4, 'uint16'], ['error_flags_m1', 4, 'uint16'], ['limit_flags_m1', 4, 'uint16']],
    b'441': [['receive_error_count_m2', 2, 'uint8'], ['transmit_error_count_m2', 2, 'uint8'],
             ['active_motor_m2', 4, 'uint16'], ['error_flags_m2', 4, 'uint16'], ['limit_flags_m2', 4, 'uint16']],
    b'402': [['bus_current_m1', 8, 'float32'], ['bus_voltage_m1', 8, 'float32']],
    b'442': [['bus_current_m2', 8, 'float32'], ['bus_voltage_m2', 8, 'float32']],
    b'403': [['velocity_ms_m1', 8, 'float32'], ['velocity_rpm_m1', 8, 'float32']],
    b'443': [['velocity_ms_m2', 8, 'float32'], ['velocity_rpm_m2', 8, 'float32']],
    b'404': [['phase_c_current_m1', 8, 'float32'], ['phase_b_current_m1', 8, 'float32']],
    b'444': [['phase_c_current_m2', 8, 'float32'], ['phase_b_current_m2', 8, 'float32']],
    b'405': [['vd_m1', 8, 'float32'], ['vq_m1', 8, 'float32']],
    b'445': [['vd_m2', 8, 'float32'], ['vq_m2', 8, 'float32']],
    b'406': [['id_m1', 8, 'float32'], ['iq_m1', 8, 'float32']],
    b'446': [['id_m2', 8, 'float32'], ['iq_m2', 8, 'float32']],
    b'407': [['bemfd_m1', 8, 'float32'], ['bemfq_m1', 8, 'float32']],
    b'447': [['bemfd_m2', 8, 'float32'], ['bemfq_m2', 8, 'float32']],
    b'408': [['15v_supply_m1', 8, 'float32'], ['reservado', 8, 'nada']],
    b'448': [['15v_supply_m2', 8, 'float32'], ['reservado', 8, 'nada']],
    b'409': [['3.3v_supply_m1', 8, 'float32'], ['1.9v_supply_m1', 8, 'float32']],
    b'449': [['3.3v_supply_m2', 8, 'float32'], ['1.9v_supply_m2', 8, 'float32']],
    b'40b': [['heat_sink_temp_m1', 8, 'float32'], ['motor_temp_m1', 8, 'float32']],
    b'44b': [['heat_sink_temp_m2', 8, 'float32'], ['motor_temp_m2', 8, 'float32']],
    b'40c': [['reservado', 8, 'nada'], ['dsp_board_temp_m1', 8, 'float32']],
    b'44c': [['reservado', 8, 'nada'], ['dsp_board_temp_m1', 8, 'float32']],
    b'40e': [['ah_m1', 8, 'float32'], ['odometer_m1', 8, 'float32']],
    b'44e': [['ah_m1', 8, 'float32'], ['odometer_m1', 8, 'float32']],
    b'600': [['bmu_hearthbeat', 8, 'data_u32'], ['serial_number', 8, 'data_u32']],
    b'601': [['cmu_serial_number_1', 8, 'data_u32'], ['pcb_temperature_1', 4, 'int16'],
             ['cell_temperature_1', 4, 'int16']],
    b'604': [['cmu_serial_number_2', 8, 'data_u32'], ['pcb_temperature_2', 4, 'int16'],
             ['cell_temperature_2', 4, 'int16']],
    b'607': [['cmu_serial_number_3', 8, 'data_u32'], ['pcb_temperature_3', 4, 'int16'],
             ['cell_temperature_3', 4, 'int16']],
    b'60a': [['cmu_serial_number_4', 8, 'data_u32'], ['pcb_temperature_4', 4, 'int16'],
             ['cell_temperature_4', 4, 'int16']],
    b'60d': [['cmu_serial_number_5', 8, 'data_u32'], ['pcb_temperature_5', 4, 'int16'],
             ['cell_temperature_5', 4, 'int16']],
    b'610': [['cmu_serial_number_6', 8, 'data_u32'], ['pcb_temperature_6', 4, 'int16'],
             ['cell_temperature_6', 4, 'int16']],
    b'602': [['cell0_voltage_1', 4, 'int16'], ['cell1_voltage_1', 4, 'int16'], ['cell2_voltage_1', 4, 'int16'],
             ['cell3_voltage_1', 4, 'int16']],
    b'605': [['cell0_voltage_2', 4, 'int16'], ['cell1_voltage_2', 4, 'int16'], ['cell2_voltage_2', 4, 'int16'],
             ['cell3_voltage_2', 4, 'int16']],
    b'608': [['cell0_voltage_3', 4, 'int16'], ['cell1_voltage_3', 4, 'int16'], ['cell2_voltage_3', 4, 'int16'],
             ['cell3_voltage_3', 4, 'int16']],
    b'60b': [['cell0_voltage_4', 4, 'int16'], ['cell1_voltage_4', 4, 'int16'], ['cell2_voltage_4', 4, 'int16'],
             ['cell3_voltage_4', 4, 'int16']],
    b'60e': [['cell0_voltage_5', 4, 'int16'], ['cell1_voltage_5', 4, 'int16'], ['cell2_voltage_5', 4, 'int16'],
             ['cell3_voltage_5', 4, 'int16']],
    b'611': [['cell0_voltage_6', 4, 'int16'], ['cell1_voltage_6', 4, 'int16'], ['cell2_voltage_6', 4, 'int16'],
             ['cell3_voltage_6', 4, 'int16']],
    b'603': [['cell4_voltage_1', 4, 'int16'], ['cell5_voltage_1', 4, 'int16'], ['cell6_voltage_1', 4, 'int16'],
             ['cell7_voltage_1', 4, 'int16']],
    b'606': [['cell4_voltage_2', 4, 'int16'], ['cell5_voltage_2', 4, 'int16'], ['cell6_voltage_2', 4, 'int16'],
             ['cell7_voltage_2', 4, 'int16']],
    b'609': [['cell4_voltage_3', 4, 'int16'], ['cell5_voltage_3', 4, 'int16'], ['cell6_voltage_3', 4, 'int16'],
             ['cell7_voltage_3', 4, 'int16']],
    b'60c': [['cell4_voltage_4', 4, 'int16'], ['cell5_voltage_4', 4, 'int16'], ['cell6_voltage_4', 4, 'int16'],
             ['cell7_voltage_4', 4, 'int16']],
    b'60f': [['cell4_voltage_5', 4, 'int16'], ['cell5_voltage_5', 4, 'int16'], ['cell6_voltage_5', 4, 'int16'],
             ['cell7_voltage_5', 4, 'int16']],
    b'612': [['cell4_voltage_6', 4, 'int16'], ['cell5_voltage_6', 4, 'int16'], ['cell6_voltage_6', 4, 'int16'],
             ['cell7_voltage_6', 4, 'int16']],
    b'6f4': [['soc_ah', 8, 'float_32'], ['soc_percentage', 8, 'float_32']],
    b'6f5': [['balance_soc_ah', 8, 'float_32'], ['balance_soc_percentage', 8, 'float_32']],
    b'6f6': [['charging_cell_voltage_error', 4, 'int16'], ['cell_temperature_margin', 4, 'int16'],
             ['discharging_cell_voltage_error', 4, 'int16'], ['total_pack_capacity', 4, 'uint16']],
    b'6f7': [['precharge_contactor_status', 2, 'uint8'], ['precharge_state', 2, 'uint8'], ['12v_contactor', 4, 'uint16']
        , ['reservado', 4, 'nada'],
             ['precharge_timer', 2, 'uint8'], ['precharge_timer_counter', 2, 'uint8']],
    b'6f8': [['minimum_cell_voltage', 4, 'uint16'], ['maximum_cell_voltage', 4, 'uint16'],
             ['cmu_number_minv', 2, 'uint8'], ['cell_number_minv', 2, 'uint8'], ['cmu_number_maxv', 2, 'uint8'],
             ['cell_number_maxv', 2, 'uint8']],
    b'6f9': [['minimum_cell_temp', 4, 'uint16'], ['maximum_cell_temp', 4, 'uint16'], ['cmu_number_mint', 2, 'uint8'],
             ['reservado', 2, 'nada'],
             ['cmu_number_maxt', 2, 'uint8'], {'reservado', 2, 'nada'}],
    b'6fa': [['battery_voltage', 8, 'data_u32'], ['battery_current', 8, 'data_u32']],
    b'6fb': [['battery_pack_status', 16, 'despues']],
    b'6fc': [['fan_speed0', 4, 'uint16'], ['fan_speed1', 4, 'uint16'], ['consumption_fans_contactors', 4, 'uint16'],
             ['consumption_cmus', 4, 'uint16']],
    b'6fd': [['extended_battery_status', 16, 'despues']]}


# terminar con manual del motor
# b'501' : [ ['current_setpoint'],['speed_setpoint']],\
# b'502' : [['bus_current_setpoint']]
# funciones de conversión de datos

def uint32(dato_inv):
    return struct.unpack('!I', codecs.decode(dato_inv, 'hex'))[0]


def uint8(dato_inv):
    return struct.unpack('!B', codecs.decode(dato_inv, 'hex'))[0]


def uint16(dato_inv):
    return struct.unpack('!H', codecs.decode(dato_inv, 'hex'))[0]


def float32(dato_inv):
    return struct.unpack('!f', codecs.decode(dato_inv, 'hex'))[0]


def int8(dato_inv):
    return struct.unpack('!b', codecs.decode(dato_inv, 'hex'))[0]


def int32(dato_inv):
    return struct.unpack('!i', codecs.decode(dato_inv, 'hex'))[0]


def int16(dato_inv):
    return struct.unpack('!h', codecs.decode(dato_inv, 'hex'))[0]


def data_u32(dato_inv):
    return struct.unpack('!L', codecs.decode(dato_inv, 'hex'))[0]


def data_32(dato_inv):
    return struct.unpack('!l', codecs.decode(dato_inv, 'hex'))[0]


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
        for identificador in listaid:
            for elemento in dicc_variables[identificador]:
                fin_datos = inicio_datos + elemento[1]
                dato = hexdata[inicio_datos:fin_datos]
                # print (dato)
                # invertir dato
                n = 2
                dato_der = [dato[i: i + n] for i in range(0, len(dato), n)]
                dato_inv = b''.join(dato_der[::-1])
                # print (dato_inv)
                # hacer conversión
                if elemento[2] == 'uint32':
                    dato_conv = uint32(dato_inv)
                elif elemento[2] == 'int32':
                    dato_conv = int32(dato_inv)
                elif elemento[2] == 'uint16':
                    dato_conv = uint16(dato_inv)
                elif elemento[2] == 'int16':
                    dato_conv = int16(dato_inv)
                elif elemento[2] == 'float32':
                    dato_conv = float32(dato_inv)
                elif elemento[2] == 'uint8':
                    dato_conv = uint8(dato_inv)
                elif elemento[2] == 'int8':
                    dato_conv = int8(dato_inv)
                elif elemento[2] == 'data_u32':
                    dato_conv = data_u32(dato_inv)
                elif elemento[2] == 'data_32':
                    dato_conv = data_32(dato_inv)
                else:
                    dato_conv = 'aun no es evaluado'
                print(elemento[0], '= ', dato_conv)
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
