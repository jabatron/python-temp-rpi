""" 
Crear un programa que escanee la red local y muestre en pantalla las ips de los dispositivos conectados.


Opcional:

Mostrar informacion extra de los dispositivos conectados

josé ángel baselga
- 24082020 versión inicial
- 28082020 añadir comentarios. arreglar el print
- 29082020 mejoras ip/interfaces

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


LIBRERIAS ADICIONALES
pip install getmac
pip install psutil

"""



import socket
import os
import platform
import time
import psutil
import ipaddress
from getmac import get_mac_address

# Necesitamos saber cual es nuestra ip
myIP = socket.gethostbyname(socket.gethostname())

# Necesitamos saber cual es la parte de red, asi que "troceamos la IP" para quedarnos con 
# la parte de red A.B.C.D -> A.B.C.
A, B, C, D = myIP.split('.')
ip_network = A + '.' + B + '.' + C + '.'

# Averiguamos en que Sistema operativo estamos para luego ejecutar los "pings"
SO = platform.system()

print ("jose angel - @jabaselga")
print ("Mi Sistema Operativo: {}".format (SO))
print ("Mi ip: {}".format(myIP))
print ('Escaneando la red {}0/24 ...'.format(ip_network))

# Dependiendo del SO el ping es de una manera u otra
# lanzamos 1 unico ping para que sea más rápido

if (SO == "Windows"):
    ip_so = 1
    cmd_ping = "ping -n 1 "
elif (SO == "Linux"):
    ip_so = 0
    cmd_ping = "ping -c 1 "
else :
    ip_so = 0
    cmd_ping = "ping -c 1 "
ip_ip = 1
ip_mk = 2
# Variables ip_XX -> nos van a permitir acceder a los datos de tarjeta de red, ip, y mask


# Sacamos la información de la red, tarjetas, ips, mascaras, etc
info_red = psutil.net_if_addrs()


# ips -> va a contener el listado de todas las IPs validas, para luego escanear las redes
ips = []
for i in a:
    # Vamos a componer toda la información de cada red en "net[]"
    net = []
    
    # accedemos a cada elemento "i", según el sigtema operativo y sacamos la IP
    # y acontinuación convertimos esa caddena en un objeto de la clase ipaddress
    IP_str = a[i][ip_so][ip_ip]
    IP_class = ipaddress.ip_address(IP_str)

    # una vez que tenemos un objeto de la clase IP, nos quedamos con las IPv4, que no sean PIPA ni loopback
    if (IP_class.version == 4) and (not IP_class.is_link_local) and (not IP_class.is_loopback) :
        # vamos a preparar una lista net [ip, mascara, bitmask, cdir] para cada una de las ips validas
        net.append(a[i][ip_so][ip_ip])                              # añadimos la ip
        net.append(a[i][ip_so][ip_mk])                              # añadimos la mascara    
        ip_prefix_str = '0.0.0.0/'+ a[i][ip_so][ip_mk]              
        ip_prefix = ipaddress.IPv4Network(ip_prefix_str).prefixlen  # buscar longitud de la mascara
        net.append(ip_prefix)                                       # añadimos logitud de la mascara
        
        IP2= net[0] + '/' + str(net[1])
        cdir = ipaddress.ip_network (IP2, strict=False)
        net.append(cdir)                                            # añadimos CDIR

        ips.append(net)


# print (ips [0][3])
# genero la lista de todos los host que pertenecen a una red
hosts = list (ipaddress.ip_network(ips[0][3]).hosts())
# print (hosts)

print (ips)





# En result vamos a guardar las IPs, y si han dado positivo o no en el escaneo
result = {}
# Guardo la hora para poner la duracción del escaneo
hora_comienzo = time.time()

inicio = 1
fin = 255
paso = 1

# Hacemos un bucle desde 1 hasta 254 y para cada item lanzamos el ping y guardamos el resultado
for host_ip in range(inicio, fin, paso):
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
            # Si ha respondido al ping conmutamos el estado
            # y lo guardamos en el array de resultados
            status = '!'
            result [addr] = 1
    # vamos imprimiendo el avance del escaneo
    print (status, end='', flush=True)

print ('')

# Guardo la hora fin de escaneo 
hora_fin = time.time()

# Impresión de los resultados
print ('Lista de IPs activas')
print ('Duración del escaneo: {} seg'.format(round (hora_fin - hora_comienzo)))
# Recorro el array de resultados imprimiendolos y de paso
# comprobando si tiene "hostname" e imprimiendo la MAC
for host_ip in range(inicio, fin, paso):
    addr = ip_network + str(host_ip)
    if result[addr] == 1:
        try: 
            name = socket.gethostbyaddr(addr)
        except Exception:
            name =['NoName']
        print ("host IP: {},  hostname: {}, con mac: {}".format(addr, name [0], get_mac_address(ip=addr)))   