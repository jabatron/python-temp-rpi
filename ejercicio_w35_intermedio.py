""" 
Crear un programa que escanee la red local y muestre en pantalla las ips de los dispositivos conectados.


Opcional:

Mostrar informacion extra de los dispositivos conectados

josé ángel baselga
- 24082020 versión inicial
- 28082020 añadir comentarios. arreglar el print

LIBRERIAS ADICIONALES
pip install getmac

---------------ejemplo de resultado------------------

jose angel - @jabaselga
Mi Sistema Operativo: Windows
Mi ip: 192.168.8.122
Escaneando la red 192.168.8.0/24 ...
.......................................................
.......................................................
......!...................!............................
..................................!....................
.!...............................!
Lista de IPs activas
host IP: 192.168.8.117,  hostname: Chromecast.lan, con mac: a4:77:33:11:11:11
host IP: 192.168.8.137,  hostname: DESKTOP-42MKJ9F.lan, con mac: 8a:90:95:22:22:22
host IP: 192.168.8.200,  hostname: Google-Nest-Mini.lan, con mac: c4:ad:34:33:33:33
host IP: 192.168.8.222,  hostname: rpi, con mac: b8:27:eb:44:44:44
host IP: 192.168.8.254,  hostname: ims.vodafone.es, con mac: ac:3b:77:55:55:55


"""

import socket
import os
import platform
import time
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
hora_comienzo = time.time()
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
    print (status, end='', flush=True)

print ('')

hora_fin = time.time()

# Impresión de los resultados
print ('Lista de IPs activas')
print ('Duración del escaneo: {} seg'.format(hora.fin - hora_comienzo))
# Recorro el array de resultados imprimiendolos y de paso
# comprobando si tiene "hostname" e imprimiendo la MAC
for host_ip in range(1, 255, 1):
    addr = ip_network + str(host_ip)
    if result[addr] == 1:
        try: 
            name = socket.gethostbyaddr(addr)
        except:
            name = 'No se ha encontrado'
        print ("host IP: {},  hostname: {}, con mac: {}".format(addr, name [0], get_mac_address(ip=addr)))   