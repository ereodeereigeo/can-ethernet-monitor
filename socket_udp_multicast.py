import socket
import struct
#import sys
import binascii
import time

multicast_group = '239.255.60.60'
server_address = ('', 4876)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
t1 = time.time()
while True:
    #print('waiting to receive message')    
    data, address = sock.recvfrom(1024)
    hexdata = binascii.hexlify(data)  
    print(hexdata)    
    #print ('received %s bytes from %s' % (len(data), address))
    if hexdata[37:40]==b'601':
        num=hexdata[46:48]+hexdata[44:46]
        print(int(num,16))
        t2=time.time()-t1        
        print(t2)
        t1=time.time()
    

    #print ('sending acknowledgement to', address)
    #sock.sendto(b'ack', address)
