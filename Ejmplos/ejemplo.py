__author__ = 'Seba'
import socket
import struct
import binascii
import time
multicast_group = '239.255.60.60'
server_addres = ('', 4876)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_addres)
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

filtro_temperatura = b'601'
filtro_volt = b'602'
while True:
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

            print temperatura_pcb
            temperatura_pcb = int(temperatura_pcb[2:4] + temperatura_pcb[0:2], 16)
            temperatura_celda = int(temperatura_celda[2:4] + temperatura_celda[0:2], 16)

            print 'TEMPERATURA PCB'
            print temperatura_pcb/10.0
            print '\n'

            print 'TEMPERATURA CELDA'
            print temperatura_celda/10.0

        elif identificador == filtro_volt:
            print 'voltaje'

    except KeyboardInterrupt:
        sock.close()
