""" 
Crear un programa que escanee la red local y muestre en pantalla las ips de los dispositivos conectados.


Opcional:

Mostrar informacion extra de los dispositivos conectados

josé ángel baselga
- 24082020 

LIBRERIAS ADICIONALES
pip install getmac

"""

import socket
import os
import platform
from getmac import get_mac_address

myIP = socket.gethostbyname(socket.gethostname())
myIP_split = myIP.split('.')

ip_network = myIP_split[0] + '.' + myIP_split[1] + '.' + myIP_split[2] + '.'
SO = platform.system()

print ("jose angel - @jabaselga")
print ("Mi Sistema Operativo: {}".format (SO))
print ("Mi ip: {}".format(myIP))
print ('Escaneando la red {}0/24 ...'.format(ip_network))

if (SO == "Windows"):
   cmd_ping = "ping -n 1 "
elif (SO == "Linux"):
   cmd_ping = "ping -c 1 "
else :
   cmd_ping = "ping -c 1 "

result = {}
for host_ip in range(1, 255, 1):
    addr = ip_network + str(host_ip)
    cmd = cmd_ping + addr
    response = os.popen(cmd)
   
    status = '.'
    result [addr] = 0
    for line in response.readlines():
        if (line.count("TTL")):
            status = '!'
            result [addr] = 1
    
    print (status, end='')

print ('')
print ('Lista de IPs activas')
for host_ip in range(1, 255, 1):
    addr = ip_network + str(host_ip)
    if result[addr] == 1:
        try: 
            name = socket.gethostbyaddr(addr)
        except:
            pass
        print ("host IP: {},  hostname: {}, con mac: {}".format(addr, name [0], get_mac_address(ip=addr)))   
