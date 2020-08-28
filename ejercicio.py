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

# Necesitamos saber cual es nuestra ip
myIP = socket.gethostbyname(socket.gethostname())

# Necesitamos saber cual es la parte de red, asi que "troceamos la IP" para quedarnos con 
# la parte de red A.B.C.D -> A.B.C.
myIP_split = myIP.split('.')
ip_network = myIP_split[0] + '.' + myIP_split[1] + '.' + myIP_split[2] + '.'

# Averiguamos en que Sistema operativo estamos para luego ejecutar los "pings"
SO = platform.system()

print ("jose angel - @jabaselga")
print ("Mi Sistema Operativo: {}".format (SO))
print ("Mi ip: {}".format(myIP))
print ('Escaneando la red {}0/24 ...'.format(ip_network))

# Dependiendo del SO el ping es de una manera u otra
# lanzamos 1 unico ping para que sea más rápido
if (SO == "Windows"):
   cmd_ping = "ping -n 1 "
elif (SO == "Linux"):
   cmd_ping = "ping -c 1 "
else :
   cmd_ping = "ping -c 1 "

# En result vamos a guardar las IPs, y si han dado positivo o no en el escaneo
result = {}
# Hacemos un bucle desde 1 hasta 254 y para pada item lanzamos el ping y guardamos el resultado
for host_ip in range(1, 255, 1):
    addr = ip_network + str(host_ip)
    cmd = cmd_ping + addr
    response = os.popen(cmd)
   
    # para ir mostrando el avance del programa
    # . -> la IP no responde a ping
    # ! -> la IP responde a ping
    # por defecto no responde
    status = '.'
    result [addr] = 0
    for line in response.readlines():
        if (line.count("TTL")):
            # Si ha respondido al ping contutamos el estado
            # y lo guardamos en el array de resultados
            status = '!'
            result [addr] = 1
    # vamos imprimiendo el avance del escaneo
    print (status, end='')

print ('')

# Impresión de los resultados
print ('Lista de IPs activas')
# Recorreo el array de resultados imprimiendolos y de paso
# comprobando si tiene "hostname" e imprimiendo la MAC
for host_ip in range(1, 255, 1):
    addr = ip_network + str(host_ip)
    if result[addr] == 1:
        try: 
            name = socket.gethostbyaddr(addr)
        except:
            pass
        print ("host IP: {},  hostname: {}, con mac: {}".format(addr, name [0], get_mac_address(ip=addr)))   