""" 
Requerimientos:

Crea un programa que lea una ip y determine su clase según su rango, la información que debe mostrar debe ser la siguiente:

°Clase de ip (clase a, b o c)
°Cuantos host pueden haber en esa subred 

Ej: en una clase c pueden haber 254 host por cada red, por lo tanto imprimiría 254 por la red actual)

Ejemplo de la salida del programa: 

"Tu ip es 192.168.0.1 es de clase C y pueden haber 254 host en tu red actual"

code:prog_b7_tuuser.py


v0.1 20201005 estructura básica del programa

Datos para elegir el tipo de IP

Class        Networks                     mask          CDIR       leading bits
A       0.0.0.0   - 127.255.255.255     255.0.0.0         /8        0
B       128.0.0.0 - 191.255.255.255     255.255.0.0       /16       10
C       192.0.0.0 - 223.255.255.255     255.255.0.0       /24       110
D       224.0.0.0 - 239.255.255.255         not defined             1110        Multicast
E       240.0.0.0 - 247.255.255.255         not defined             1111        Reserved

información procedente de:
https://en.wikipedia.org/wiki/Classful_network


LIBRERIAS ADICIONALES


"""
import ipaddress

def pedir_ip ():
    print ('Ejercicio b7. Mostrar clase y número de host.')
    print ('Notación clásica: 192.168.4.2')
    print ('Notción CDIR: 192.168.4.2/23 o 192.168.5.2/255.255.240.0')
    ip_s = input  ("Introduce una IP en notación clásica o CDIR: ")

    return ip_s


def es_ip (ip_s):
    """  

    """
    # tipo de ip 0-> notación clásica, 1-> CDIR
    ip = None
    network = None
    clase = None
    tipo = None
    dir_ok = False

    
    try:
        ip = ipaddress.IPv4Address(ip_s)
        print ('IP valida')
        dir_ok = True
        tipo = 1
    except:
        dir_ok = False

    if not dir_ok:
        try:
            network = ipaddress.IPv4Network(ip_s, strict=False)
            ip, _ = ip_s.split('/')
            dir_ok = True
            tipo = 2
        except:
            dir_ok = False

        
    if tipo == 1:
        
        a, b, c, d = ip_s.split('.')
        a, b, c, d = int(a), int (b), int (c), int (d)

        if a < 128:
            clase = "A"
            full_ip = ip_s +'/8'
        elif a < 192:
            clase = 'B'
            full_ip = ip_s +'/16'
        elif a < 224:
            clase = 'C'
            full_ip = ip_s +'/24'
        elif a < 240:
            clase = 'D'
            full_ip = None
        elif a < 248:
            clase = 'S'
            full_ip = None
        
        try:
            network = ipaddress.IPv4Network(full_ip, strict=False)
        except:
            network = None
            

    return (ip, network, clase, tipo)

def imprimir (data):

    prefijo = data[1].prefixlen
    print (f"Dirección ip: {data[0]}")
    if data[2]:
        print (f'Es una red de clase {data[2]}.')
    else:
        print ('Has introducido la red en formato CDIR.')
        if prefijo == 24:
            print ('Que por la máscara de red podría ser de clase C')
        elif prefijo == 16:
            print ('Que por la máscara de red podría ser de clase B')
        elif prefijo == 8:
            print ('Que por la máscara de red podría ser de clase A')

    if data[1]:
        print (f'La máscara de red es: {str(data[1].netmask)}')
        hosts = (2**(32-prefijo))-2 # 1 por broadcast y otro por dirección de red
        print (f'En la que puede haber {hosts} hosts')
    else:
        print ('Es una red reservada, por tanto el numero de hosts es "not defined"')

def main_chequear_IP ():
    """ 

    """

    data = (None, None, None, None)
        
    while data[0] == None:
        ip = pedir_ip ()
        data = es_ip (ip)
      
  
    imprimir (data)
    


if __name__ == "__main__":
    main_chequear_IP()
    