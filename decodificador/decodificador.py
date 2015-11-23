import struct
import codecs


class VariablesCan(object):

    def __init__(self):

        self.dicc_vacio = {
                'largo': 0,
                'tipo': None
        }

        self.dicc_modelo = self.modelo_de_datos

        self.opciones_unpack = {
            'uint32': '!I',
            'uint8': '!B',
            'uint16': '!H',
            'float32': '!f',
            'int8': '!b',
            'int32': '!i',
            'int16': '!i',
            'data_u32': '!L',
            'data_32': '!l',
        }

    def return_data(self, key, ident):
        return self.dicc_vacio[key][ident]['tipo'], self.dicc_vacio[key][ident]['largo']

    def identificadores(self, key):
        return self.dicc_modelo[key].keys()

    @property
    def modelo_de_datos(self):
        dicc_vacio = {}
        for llave, elemento in self.crear_dicc_variables.iteritems():
            identificadores = [ident[0] for ident in elemento]
            dicc_vacio[llave] = dict.fromkeys(identificadores)
            for index, identificador in enumerate(identificadores):
                dicc_vacio[llave][identificador] = self.dicc_vacio
                dicc_vacio[llave][identificador]['largo'] = elemento[index][1]
                dicc_vacio[llave][identificador]['tipo'] = elemento[index][2]
        return dicc_vacio

    def conversion_data(self, data, tipo):
        try:
            option = self.opciones_unpack[tipo]
            return struct.unpack(option,  codecs.decode(data, 'hex'))[0]
        except KeyError:
            return 'aun no evaluado'

    @property
    def crear_dicc_variables(self):
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
        return dicc_variables
