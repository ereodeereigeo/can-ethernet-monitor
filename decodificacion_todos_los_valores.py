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
import serial
import time
import datetime
import pandas as pd

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
win.resize(1280,768)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Updating plot")
p1.addLegend()
p1.setXRange(0, 600)
p1.setYRange(0, 1000)
win.nextRow()

p2 = win.addPlot(title="Updating plot")
p2.setXRange(0, 600)
p2.setYRange(0, 200)
p2.addLegend()

curve1 = p1.plot(pen='b', name='TEMPERATURA PCB')
curve2 = p1.plot(pen='r', name='TEMPERATURA CELDA')
curve3 = p2.plot(pen='r', name='VOLTAJE BUS')

historicos_temperatura_PCB = deque([], maxlen=100)
historicos_temperatura_CELDA = deque([], maxlen=100)
historico_voltaje_bus_dc = deque([], maxlen=100)

#añadir diccionario de identificadores
dicc_variables = {b'400': [['tritium_id_m1', 8, 'uint32'], ['ident_m1', 8, 'uint32']],
 b'401': [['limit_flags_m1', 4, 'uint16'],
  ['error_flags_m1', 4, 'uint16'],
  ['active_motor_m1', 4, 'uint16'],
  ['transmit_error_count_m1', 2, 'uint8'],
  ['receive_error_count_m1', 2, 'uint8']],
 b'402': [['bus_voltage_m1', 8, 'float32'], ['bus_current_m1', 8, 'float32']],
 b'403': [['velocity_rpm_m1', 8, 'float32'], ['velocity_ms_m1', 8, 'float32']],
 b'404': [['phase_b_current_m1', 8, 'float32'],
  ['phase_c_current_m1', 8, 'float32']],
 b'405': [['vq_m1', 8, 'float32'], ['vd_m1', 8, 'float32']],
 b'406': [['iq_m1', 8, 'float32'], ['id_m1', 8, 'float32']],
 b'407': [['bemfq_m1', 8, 'float32'], ['bemfd_m1', 8, 'float32']],
 b'408': [['reservado', 8, 'nada'], ['15v_supply_m1', 8, 'float32']],
 b'409': [['1.9v_supply_m1', 8, 'float32'], ['3.3v_supply_m1', 8, 'float32']],
 b'40b': [['motor_temp_m1', 8, 'float32'],
  ['heat_sink_temp_m1', 8, 'float32']],
 b'40c': [['dsp_board_temp_m1', 8, 'float32'], ['reservado', 8, 'nada']],
 b'40e': [['odometer_m1', 8, 'float32'], ['ah_m1', 8, 'float32']],
 b'440': [['tritium_id_m2', 8, 'uint32'], ['ident_m2', 8, 'uint32']],
 b'441': [['limit_flags_m2', 4, 'uint16'],
  ['error_flags_m2', 4, 'uint16'],
  ['active_motor_m2', 4, 'uint16'],
  ['transmit_error_count_m2', 2, 'uint8'],
  ['receive_error_count_m2', 2, 'uint8']],
 b'442': [['bus_voltage_m2', 8, 'float32'], ['bus_current_m2', 8, 'float32']],
 b'443': [['velocity_rpm_m2', 8, 'float32'], ['velocity_ms_m2', 8, 'float32']],
 b'444': [['phase_b_current_m2', 8, 'float32'],
  ['phase_c_current_m2', 8, 'float32']],
 b'445': [['vq_m2', 8, 'float32'], ['vd_m2', 8, 'float32']],
 b'446': [['iq_m2', 8, 'float32'], ['id_m2', 8, 'float32']],
 b'447': [['bemfq_m2', 8, 'float32'], ['bemfd_m2', 8, 'float32']],
 b'448': [['reservado', 8, 'nada'], ['15v_supply_m2', 8, 'float32']],
 b'449': [['1.9v_supply_m2', 8, 'float32'], ['3.3v_supply_m2', 8, 'float32']],
 b'44b': [['motor_temp_m2', 8, 'float32'],
  ['heat_sink_temp_m2', 8, 'float32']],
 b'44c': [['dsp_board_temp_m1', 8, 'float32'], ['reservado', 8, 'nada']],
 b'44e': [['odometer_m1', 8, 'float32'], ['ah_m1', 8, 'float32']],
 b'600': [['serial_number', 8, 'data_u32'], ['bmu_hearthbeat', 8, 'data_u32']],
 b'601': [['cell_temperature_1', 4, 'int16'],
  ['pcb_temperature_1', 4, 'int16'],
  ['cmu_serial_number_1', 8, 'data_u32']],
 b'602': [['cell3_voltage_1', 4, 'int16'],
  ['cell2_voltage_1', 4, 'int16'],
  ['cell1_voltage_1', 4, 'int16'],
  ['cell0_voltage_1', 4, 'int16']],
 b'603': [['cell7_voltage_1', 4, 'int16'],
  ['cell6_voltage_1', 4, 'int16'],
  ['cell5_voltage_1', 4, 'int16'],
  ['cell4_voltage_1', 4, 'int16']],
 b'604': [['cell_temperature_2', 4, 'int16'],
  ['pcb_temperature_2', 4, 'int16'],
  ['cmu_serial_number_2', 8, 'data_u32']],
 b'605': [['cell3_voltage_2', 4, 'int16'],
  ['cell2_voltage_2', 4, 'int16'],
  ['cell1_voltage_2', 4, 'int16'],
  ['cell0_voltage_2', 4, 'int16']],
 b'606': [['cell7_voltage_2', 4, 'int16'],
  ['cell6_voltage_2', 4, 'int16'],
  ['cell5_voltage_2', 4, 'int16'],
  ['cell4_voltage_2', 4, 'int16']],
 b'607': [['cell_temperature_3', 4, 'int16'],
  ['pcb_temperature_3', 4, 'int16'],
  ['cmu_serial_number_3', 8, 'data_u32']],
 b'608': [['cell3_voltage_3', 4, 'int16'],
  ['cell2_voltage_3', 4, 'int16'],
  ['cell1_voltage_3', 4, 'int16'],
  ['cell0_voltage_3', 4, 'int16']],
 b'609': [['cell7_voltage_3', 4, 'int16'],
  ['cell6_voltage_3', 4, 'int16'],
  ['cell5_voltage_3', 4, 'int16'],
  ['cell4_voltage_3', 4, 'int16']],
 b'60a': [['cell_temperature_4', 4, 'int16'],
  ['pcb_temperature_4', 4, 'int16'],
  ['cmu_serial_number_4', 8, 'data_u32']],
 b'60b': [['cell3_voltage_4', 4, 'int16'],
  ['cell2_voltage_4', 4, 'int16'],
  ['cell1_voltage_4', 4, 'int16'],
  ['cell0_voltage_4', 4, 'int16']],
 b'60c': [['cell7_voltage_4', 4, 'int16'],
  ['cell6_voltage_4', 4, 'int16'],
  ['cell5_voltage_4', 4, 'int16'],
  ['cell4_voltage_4', 4, 'int16']],
 b'60d': [['cell_temperature_5', 4, 'int16'],
  ['pcb_temperature_5', 4, 'int16'],
  ['cmu_serial_number_5', 8, 'data_u32']],
 b'60e': [['cell3_voltage_5', 4, 'int16'],
  ['cell2_voltage_5', 4, 'int16'],
  ['cell1_voltage_5', 4, 'int16'],
  ['cell0_voltage_5', 4, 'int16']],
 b'60f': [['cell7_voltage_5', 4, 'int16'],
  ['cell6_voltage_5', 4, 'int16'],
  ['cell5_voltage_5', 4, 'int16'],
  ['cell4_voltage_5', 4, 'int16']],
 b'610': [['cell_temperature_6', 4, 'int16'],
  ['pcb_temperature_6', 4, 'int16'],
  ['cmu_serial_number_6', 8, 'data_u32']],
 b'611': [['cell3_voltage_6', 4, 'int16'],
  ['cell2_voltage_6', 4, 'int16'],
  ['cell1_voltage_6', 4, 'int16'],
  ['cell0_voltage_6', 4, 'int16']],
 b'612': [['cell7_voltage_6', 4, 'int16'],
  ['cell6_voltage_6', 4, 'int16'],
  ['cell5_voltage_6', 4, 'int16'],
  ['cell4_voltage_6', 4, 'int16']],
 b'6f4': [['soc_percentage', 8, 'float_32'], ['soc_ah', 8, 'float_32']],
 b'6f5': [['balance_soc_percentage', 8, 'float_32'],
  ['balance_soc_ah', 8, 'float_32']],
 b'6f6': [['total_pack_capacity', 4, 'uint16'],
  ['discharging_cell_voltage_error', 4, 'int16'],
  ['cell_temperature_margin', 4, 'int16'],
  ['charging_cell_voltage_error', 4, 'int16']],
 b'6f7': [['precharge_timer_counter', 2, 'uint8'],
  ['precharge_timer', 2, 'uint8'],
  ['reservado', 4, 'nada'],
  ['12v_contactor', 4, 'uint16'],
  ['precharge_state', 2, 'uint8'],
  ['precharge_contactor_status', 2, 'uint8']],
 b'6f8': [['cell_number_maxv', 2, 'uint8'],
  ['cmu_number_maxv', 2, 'uint8'],
  ['cell_number_minv', 2, 'uint8'],
  ['cmu_number_minv', 2, 'uint8'],
  ['maximum_cell_voltage', 4, 'uint16'],
  ['minimum_cell_voltage', 4, 'uint16']],
 b'6f9': [{2, 'reservado', 'nada'},
  ['cmu_number_maxt', 2, 'uint8'],
  ['reservado', 2, 'nada'],
  ['cmu_number_mint', 2, 'uint8'],
  ['maximum_cell_temp', 4, 'uint16'],
  ['minimum_cell_temp', 4, 'uint16']],
 b'6fa': [['battery_current', 8, 'data_u32'],
  ['battery_voltage', 8, 'data_u32']],
 b'6fb': [['battery_pack_status', 16, 'despues']],
 b'6fc': [['consumption_cmus', 4, 'uint16'],
  ['consumption_fans_contactors', 4, 'uint16'],
  ['fan_speed1', 4, 'uint16'],
  ['fan_speed0', 4, 'uint16']],
 b'6fd': [['extended_battery_status', 16, 'despues']]}
  #terminar con manual del motor
  #b'501' : [ ['current_setpoint'],['speed_setpoint']],\
  #b'502' : [['bus_current_setpoint']]

#indice de valores

diccionario_nuevo = {'1.9v_supply_m1': [],
 '1.9v_supply_m2': [],
 '12v_contactor': [],
 '15v_supply_m1': [],
 '15v_supply_m2': [],
 '3.3v_supply_m1': [],
 '3.3v_supply_m2': [],
 'active_motor_m1': [],
 'active_motor_m2': [],
 'ah_m1': [],
 'ah_m2': [],
 'balance_soc_ah': [],
 'balance_soc_percentage': [],
 'battery_current': [],
 'battery_pack_status': [],
 'battery_voltage': [],
 'bemfd_m1': [],
 'bemfd_m2': [],
 'bemfq_m1': [],
 'bemfq_m2': [],
 'bmu_hearthbeat': [],
 'bus_current_m1': [],
 'bus_current_m2': [],
 'bus_current_setpoint': [],
 'bus_voltage_m1': [],
 'bus_voltage_m2': [],
 'cell0_voltage_1': [],
 'cell0_voltage_2': [],
 'cell0_voltage_3': [],
 'cell0_voltage_4': [],
 'cell0_voltage_5': [],
 'cell0_voltage_6': [],
 'cell1_voltage_1': [],
 'cell1_voltage_2': [],
 'cell1_voltage_3': [],
 'cell1_voltage_4': [],
 'cell1_voltage_5': [],
 'cell1_voltage_6': [],
 'cell2_voltage_1': [],
 'cell2_voltage_2': [],
 'cell2_voltage_3': [],
 'cell2_voltage_4': [],
 'cell2_voltage_5': [],
 'cell2_voltage_6': [],
 'cell3_voltage_1': [],
 'cell3_voltage_2': [],
 'cell3_voltage_3': [],
 'cell3_voltage_4': [],
 'cell3_voltage_5': [],
 'cell3_voltage_6': [],
 'cell4_voltage_1': [],
 'cell4_voltage_2': [],
 'cell4_voltage_3': [],
 'cell4_voltage_4': [],
 'cell4_voltage_5': [],
 'cell4_voltage_6': [],
 'cell5_voltage_1': [],
 'cell5_voltage_2': [],
 'cell5_voltage_3': [],
 'cell5_voltage_4': [],
 'cell5_voltage_5': [],
 'cell5_voltage_6': [],
 'cell6_voltage_1': [],
 'cell6_voltage_2': [],
 'cell6_voltage_3': [],
 'cell6_voltage_4': [],
 'cell6_voltage_5': [],
 'cell6_voltage_6': [],
 'cell7_voltage_1': [],
 'cell7_voltage_2': [],
 'cell7_voltage_3': [],
 'cell7_voltage_4': [],
 'cell7_voltage_5': [],
 'cell7_voltage_6': [],
 'cell_number_maxv': [],
 'cell_number_minv': [],
 'cell_temperature_1': [],
 'cell_temperature_2': [],
 'cell_temperature_3': [],
 'cell_temperature_4': [],
 'cell_temperature_5': [],
 'cell_temperature_6': [],
 'cmu_number_maxt': [],
 'cmu_number_maxv': [],
 'cmu_number_mint': [],
 'cmu_number_minv': [],
 'cmu_serial_number_1': [],
 'cmu_serial_number_2': [],
 'cmu_serial_number_3': [],
 'cmu_serial_number_4': [],
 'cmu_serial_number_5': [],
 'cmu_serial_number_6': [],
 'consumption_cmus': [],
 'consumption_fans_contactors': [],
 'current_setpoint': [],
 'dsp_board_temp_m1': [],
 'dsp_board_temp_m2': [],
 'error_flags_m1': [],
 'error_flags_m2': [],
 'extended_battery_status': [],
 'fan_speed0': [],
 'fan_speed1': [],
 'heat_sink_temp_m1': [],
 'heat_sink_temp_m2': [],
 'id_m1': [],
 'id_m2': [],
 'ident_m1': [],
 'ident_m2': [],
 'iq_m1': [],
 'iq_m2': [],
 'limit_flags_m1': [],
 'limit_flags_m2': [],
 'maximum_cell_temp': [],
 'maximum_cell_voltage': [],
 'minimum_cell_temp': [],
 'minimum_cell_voltage': [],
 'motor_temp_m1': [],
 'motor_temp_m2': [],
 'odometer_m1': [],
 'odometer_m2': [],
 'pcb_temperature_1': [],
 'pcb_temperature_2': [],
 'pcb_temperature_3': [],
 'pcb_temperature_4': [],
 'pcb_temperature_5': [],
 'pcb_temperature_6': [],
 'phase_b_current_m1': [],
 'phase_b_current_m2': [],
 'phase_c_current_m1': [],
 'phase_c_current_m2': [],
 'precharge_contactor_status': [],
 'precharge_state': [],
 'precharge_timer': [],
 'precharge_timer_counter': [],
 'receive_error_count_m1': [],
 'receive_error_count_m2': [],
 'serial_number': [],
 'soc_ah': [],
 'soc_percentage': [],
 'speed_setpoint': [],
 'transmit_error_count_m1': [],
 'transmit_error_count_m2': [],
 'tritium_id_m1': [],
 'tritium_id_m2': [],
 'vd_m1': [],
 'vd_m2': [],
 'velocity_ms_m1': [],
 'velocity_ms_m2': [],
 'velocity_rpm_m1': [],
 'velocity_rpm_m2': [],
 'vq_m1': [],
 'vq_m2': []}
# Dataframe
dataframe_timestamp = pd.DataFrame(columns=diccionario_nuevo.keys())
dataframe_global = pd.DataFrame(columns=diccionario_nuevo.keys())
# funciones de conversión de datos
  
def uint32(dato_inv):
    return (struct.unpack('!I', codecs.decode(dato_inv, 'hex'))[0])

def uint8(dato_inv):
    return (struct.unpack('!B', codecs.decode(dato_inv, 'hex'))[0])

def uint16(dato_inv):
    return (struct.unpack('!H', codecs.decode(dato_inv, 'hex'))[0])

def float32(dato_inv):
    return (struct.unpack('!f', codecs.decode(dato_inv, 'hex'))[0])
    
def int8(dato_inv):
    return (struct.unpack('!b', codecs.decode(dato_inv, 'hex'))[0])
    
def int32(dato_inv):
    return (struct.unpack('!i', codecs.decode(dato_inv, 'hex'))[0])
    
def int16(dato_inv):
    return (struct.unpack('!h', codecs.decode(dato_inv, 'hex'))[0])
    
def data_u32(dato_inv):
    return (struct.unpack('!L', codecs.decode(dato_inv, 'hex'))[0])
    
def data_32(dato_inv):
    return (struct.unpack('!l', codecs.decode(dato_inv, 'hex'))[0])
#PuertoSerie = serial.Serial('com4', 115200)
previous = time.time()
diccionario_final = {}
def update():
    global diccionario_final,tiempo_actual,dataframe_global,dataframe_timestamp,diccionario_nuevo,previous,curve1, curve2, curve3, historicos_temperatura_CELDA, historicos_temperatura_PCB, historico_voltaje_bus_dc, p1, p2
    try:
            
        #crear dataframe
        #segundo_actual = datetime.datetime.now().replace(microsecond=0)
        # inicializar cronometro de 1 segundo
        
        #tabla = pd.DataFrame(columns = columnas, index=[segundo_actual])
        data, address = sock.recvfrom(1024)
        #data = PuertoSerie.readline()
        hexdata = binascii.hexlify(data)
        listaId = []
        inicio = 37
        fin = 40
        ident = '0'
        #print (hexdata)
        while len(ident)>0:
            ident = hexdata[inicio:fin]                
            listaId.append(ident)
            inicio = inicio + 28
            fin = fin + 28
        inicio_datos = 44
        for identificador in listaId:
            try:
                for elemento in dicc_variables[identificador]:
                    fin_datos = inicio_datos + elemento[1]
                    dato = hexdata[inicio_datos:fin_datos]
                    #print (dato)
                    #invertir dato
                    n = 2
                    dato_der = [dato[i : i+n] for i in range(0,len(dato),n)]
                    dato_inv = b''.join(dato_der[::-1])
                    #print (dato_inv)
                    #hacer conversión
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
                    #print (elemento[0],'= ', dato_conv)
                    diccionario_nuevo[elemento[0]].append(dato_conv)
                    inicio_datos = inicio_datos+ elemento[1] 
            except KeyError:
                pass
            inicio_datos = inicio_datos + 12
        tiempo_actual = time.time()
        if (tiempo_actual - previous >= 1):
            previous = tiempo_actual
            for elemento in diccionario_nuevo.keys():
                    if len(diccionario_nuevo[elemento])>0:
                        diccionario_final[elemento] = [max(diccionario_nuevo[elemento])]
                        diccionario_nuevo[elemento] = []
                    else:
                        diccionario_final[elemento] = [float('nan')]
                        diccionario_nuevo[elemento] = []
            

            dataframe_timestamp = pd.DataFrame(diccionario_final, index =[datetime.datetime.now().replace(microsecond = 0)] )                
            '''diccionario_nuevo = {'1.9v_supply_m1': [],
                                 '1.9v_supply_m2': [],
                                 '12v_contactor': [],
                                 '15v_supply_m1': [],
                                 '15v_supply_m2': [],
                                 '3.3v_supply_m1': [],
                                 '3.3v_supply_m2': [],
                                 'active_motor_m1': [],
                                 'active_motor_m2': [],
                                 'ah_m1': [],
                                 'ah_m2': [],
                                 'balance_soc_ah': [],
                                 'balance_soc_percentage': [],
                                 'battery_current': [],
                                 'battery_pack_status': [],
                                 'battery_voltage': [],
                                 'bemfd_m1': [],
                                 'bemfd_m2': [],
                                 'bemfq_m1': [],
                                 'bemfq_m2': [],
                                 'bmu_hearthbeat': [],
                                 'bus_current_m1': [],
                                 'bus_current_m2': [],
                                 'bus_current_setpoint': [],
                                 'bus_voltage_m1': [],
                                 'bus_voltage_m2': [],
                                 'cell0_voltage_1': [],
                                 'cell0_voltage_2': [],
                                 'cell0_voltage_3': [],
                                 'cell0_voltage_4': [],
                                 'cell0_voltage_5': [],
                                 'cell0_voltage_6': [],
                                 'cell1_voltage_1': [],
                                 'cell1_voltage_2': [],
                                 'cell1_voltage_3': [],
                                 'cell1_voltage_4': [],
                                 'cell1_voltage_5': [],
                                 'cell1_voltage_6': [],
                                 'cell2_voltage_1': [],
                                 'cell2_voltage_2': [],
                                 'cell2_voltage_3': [],
                                 'cell2_voltage_4': [],
                                 'cell2_voltage_5': [],
                                 'cell2_voltage_6': [],
                                 'cell3_voltage_1': [],
                                 'cell3_voltage_2': [],
                                 'cell3_voltage_3': [],
                                 'cell3_voltage_4': [],
                                 'cell3_voltage_5': [],
                                 'cell3_voltage_6': [],
                                 'cell4_voltage_1': [],
                                 'cell4_voltage_2': [],
                                 'cell4_voltage_3': [],
                                 'cell4_voltage_4': [],
                                 'cell4_voltage_5': [],
                                 'cell4_voltage_6': [],
                                 'cell5_voltage_1': [],
                                 'cell5_voltage_2': [],
                                 'cell5_voltage_3': [],
                                 'cell5_voltage_4': [],
                                 'cell5_voltage_5': [],
                                 'cell5_voltage_6': [],
                                 'cell6_voltage_1': [],
                                 'cell6_voltage_2': [],
                                 'cell6_voltage_3': [],
                                 'cell6_voltage_4': [],
                                 'cell6_voltage_5': [],
                                 'cell6_voltage_6': [],
                                 'cell7_voltage_1': [],
                                 'cell7_voltage_2': [],
                                 'cell7_voltage_3': [],
                                 'cell7_voltage_4': [],
                                 'cell7_voltage_5': [],
                                 'cell7_voltage_6': [],
                                 'cell_number_maxv': [],
                                 'cell_number_minv': [],
                                 'cell_temperature_1': [],
                                 'cell_temperature_2': [],
                                 'cell_temperature_3': [],
                                 'cell_temperature_4': [],
                                 'cell_temperature_5': [],
                                 'cell_temperature_6': [],
                                 'cmu_number_maxt': [],
                                 'cmu_number_maxv': [],
                                 'cmu_number_mint': [],
                                 'cmu_number_minv': [],
                                 'cmu_serial_number_1': [],
                                 'cmu_serial_number_2': [],
                                 'cmu_serial_number_3': [],
                                 'cmu_serial_number_4': [],
                                 'cmu_serial_number_5': [],
                                 'cmu_serial_number_6': [],
                                 'consumption_cmus': [],
                                 'consumption_fans_contactors': [],
                                 'current_setpoint': [],
                                 'dsp_board_temp_m1': [],
                                 'dsp_board_temp_m2': [],
                                 'error_flags_m1': [],
                                 'error_flags_m2': [],
                                 'extended_battery_status': [],
                                 'fan_speed0': [],
                                 'fan_speed1': [],
                                 'heat_sink_temp_m1': [],
                                 'heat_sink_temp_m2': [],
                                 'id_m1': [],
                                 'id_m2': [],
                                 'ident_m1': [],
                                 'ident_m2': [],
                                 'iq_m1': [],
                                 'iq_m2': [],
                                 'limit_flags_m1': [],
                                 'limit_flags_m2': [],
                                 'maximum_cell_temp': [],
                                 'maximum_cell_voltage': [],
                                 'minimum_cell_temp': [],
                                 'minimum_cell_voltage': [],
                                 'motor_temp_m1': [],
                                 'motor_temp_m2': [],
                                 'odometer_m1': [],
                                 'odometer_m2': [],
                                 'pcb_temperature_1': [],
                                 'pcb_temperature_2': [],
                                 'pcb_temperature_3': [],
                                 'pcb_temperature_4': [],
                                 'pcb_temperature_5': [],
                                 'pcb_temperature_6': [],
                                 'phase_b_current_m1': [],
                                 'phase_b_current_m2': [],
                                 'phase_c_current_m1': [],
                                 'phase_c_current_m2': [],
                                 'precharge_contactor_status': [],
                                 'precharge_state': [],
                                 'precharge_timer': [],
                                 'precharge_timer_counter': [],
                                 'receive_error_count_m1': [],
                                 'receive_error_count_m2': [],
                                 'serial_number': [],
                                 'soc_ah': [],
                                 'soc_percentage': [],
                                 'speed_setpoint': [],
                                 'transmit_error_count_m1': [],
                                 'transmit_error_count_m2': [],
                                 'tritium_id_m1': [],
                                 'tritium_id_m2': [],
                                 'vd_m1': [],
                                 'vd_m2': [],
                                 'velocity_ms_m1': [],
                                 'velocity_ms_m2': [],
                                 'velocity_rpm_m1': [],
                                 'velocity_rpm_m2': [],
                                 'vq_m1': [],
                                 'vq_m2': []}'''
            dataframe_global = dataframe_global.append(dataframe_timestamp)
            curve1.setData(dataframe_global['velocity_rpm_m1'])
            #curve2.setData(dataframe_global[])
            curve3.setData(dataframe_global['bus_voltage_m1'])
            #print(dataframe_global['velocity_rpm_m1'])
            
                
        
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
