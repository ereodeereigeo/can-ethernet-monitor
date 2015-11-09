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

filtro_wavescultor = b'401'

while True:
    try:
        data, address = sock.recvfrom(124)
        hexdata = binascii.hexlify(data)
        print hexdata
        identificador = hexdata[37:40]
        if identificador == filtro_wavescultor:
            print hexdata
            '''
            if len(hexdata) == 60:
                temperatura = hexdata[-16:-8]
                temperatura = temperatura[6:8] + temperatura[4:6] + temperatura[2:4] + temperatura[0:2]
                print struct.unpack('!f', temperatura.decode('hex'))[0]
            '''

    except KeyboardInterrupt:
        sock.close()
