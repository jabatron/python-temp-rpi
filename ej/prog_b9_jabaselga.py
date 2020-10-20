""" 
Detalles:

Un escáner de puertos a una ip

Requerimientos:

Crea un programa que escanee los puertos de una ip, deben haber 3 tipos de escaneo:

1.Escaneo rápido: Escaneara los puertos mas comunes según tu criterio o puedes escogerlos de esta web que te muestra los mas utilizados: Link

2.Escaneo personalizado: El usuario debe ingresar cuales puertos quiere escanear, ya sea por rango (10-20) o individual (10) o separados por coma (80, 443, 445).

3.Escaneo completo: El programa escaneara todos los puertos.

Luego el programa imprimirá en pantalla solo los puertos que esten abiertos.

El programa se puede ejecutar de dos formas:

1.Modo interactivo: El programa le pide al usuario que ingrese los datos mediante inputs

2.Argumentos: al ejecutar el programa, mediante las opciones que ingrese el usuario tomara esos datos para determinar el tipo de escaneo 
y demás datos (ej: python -p 80 -i 10.10.10.1 -escaneoB) (NOTA: estas opciones son de ejemplo)

Programas completados:


code: progb_9_tuuser.py
@aprenderpython
redes

"""
import socket
import sys 

def scan_port(ip, port):
    """ Esta funcion escanea 1 puerto. Devuelve True si esta abierto, False si no lo esta
    """

    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(0.5) 

        # returns an error indicator 
        result = s.connect_ex((ip,port)) 
        if result ==0: 
            return True
        s.close() 
    
    except: 
            print(f"El intento de escaner el puerto {port} en la ip {ip} ha dado un error") 
    
    return False


if __name__ == "__main__":

    arguments_count=len(sys.argv)
    
    print ("________________________________________________________________________________")
    print ('Ejercicio b9. Escaner de puertos.')
    print ('@jabaselga')
    print (f'{sys.argv[0]} [-i IP] [-p ports]|[-t A|B|C')
    print ("________________________________________________________________________________")

    if arguments_count > 2:
        print ('Para ejecutar el comando:')
        print (f'{sys.argv[0]} [-i IP] [-p ports] [-t A|B|c')

