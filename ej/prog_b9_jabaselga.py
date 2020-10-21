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
import argparse
import ipaddress
import re
from datetime import datetime 

def check_ip(string):
    try:
        ipaddress.IPv4Address(string)
    except:
        msg = f'{string} no es una IP.'
        raise argparse.ArgumentTypeError(msg)
    
    return string

def check_ports(string):
    pattern=re.compile(r'(((([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))-(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))),|(\d{1,5}),)*((\d{1,5}-\d{1,5})|(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))\Z)+')
    port_re=pattern.fullmatch(string)
    
    if port_re:
        lp=eval_port(port_re.string)
        if lp:
            return port_re.string
        else:
            msg = f'{string} error al escribir los puertos.'
            raise argparse.ArgumentTypeError(msg)

    else:
        msg = f'{string} error al escribir los puertos.'
        raise argparse.ArgumentTypeError(msg)

def check_ports_manual(string):
    pattern=re.compile(r'(((([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))-(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))),|(\d{1,5}),)*((\d{1,5}-\d{1,5})|(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))\Z)+')
    port_re=pattern.fullmatch(string)
    
    if port_re:
        lp=eval_port(port_re.string)
        if lp:
            return sorted(list(set(eval_port(port_re.string))))
    
    return False


def eval_port(ports_s):
    ports=list(ports_s.split(','))

    lp=[]
    for p in ports:
        if p.isdigit():
            lp.append(int(p))
        else:
            a, b = map(int, p.split('-'))
      
            if a>b:
                return False
            else:
                for j in range(a,b+1):
                    lp.append(int(j))
    return lp

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
    print ('usage: prog_b9_jabaselga.py [-h] [-p [PORTS] | -f | -q] [-i A.B.C.D]')
    print ("________________________________________________________________________________")

    parser = argparse.ArgumentParser(description='Espectacular escaner de puertos', epilog='@jabaselga')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--ports", nargs='?', help="Ports to scan",type=check_ports)
    group.add_argument("-f", "--full", help="Scan all port range (0-65535)", action='store_true')
    group.add_argument("-q", "--quit", help="Scan more interesting ports (22, 80, 443, ...)", action='store_true')
    parser.add_argument("-i", "--ip", metavar='A.B.C.D', help="IP to port scan", type=check_ip)
    parser.add_argument("-v", "--verbose", help="Extra information")
    args = parser.parse_args()

    if args.verbose:
        print (f'Puertos: {args.ports}')
        print (f'Escano total: {args.full}')
        print (f'Escaneo rápido: {args.quit}')
        print (f'Sobre esta ip: {args.ip}')


    ip=''
    if not args.ip:
        nok=True
        while nok:
            ip=input('Introduce la IP a escanear: ')
            try:
                ipaddress.IPv4Address(ip)
                nok = False
            except:
                print ('Has escrito una IP no válida. Intenta de nuevo.')
    else:
        ip=args.ip
    
    ports=[]
    
    if args.quit:
        ports = [22, 23, 80, 443]
    elif args.full:
        ports=list(range(65535))
    else:
        if not args.ports:
            nok=True
            while not ports:
                ports=input('Introduce los puertos a escanear: ')
                ports = check_ports_manual(ports)
                if not ports:
                    print ('No has escrito correctamente los puertos [x,x-y,...].  Intenta de nuevo.')
        else:
            ports = sorted(list(set(eval_port(args.ports))))
        
    if args.verbose:
        print (ports)

    print("-" * 50) 
    print("Scanning Target: " + ip) 
    print("Scanning started at:" + str(datetime.now())) 
    print("-" * 50) 

    try: 
        for port in ports:
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            socket.setdefaulttimeout(0.01) 
            
            # returns an error indicator 
            result = s.connect_ex((ip,port)) 
            if result ==0: 
                print(f"Port {port} is open") 
            s.close() 
            
    except KeyboardInterrupt: 
            print("\n Exitting Program !!!!") 
            sys.exit() 
    except socket.gaierror: 
            print("\n Hostname Could Not Be Resolved !!!!") 
            sys.exit() 
    except socket.error: 
            print("\n Server not responding !!!!") 
            sys.exit() 

