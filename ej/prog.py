import argparse
import ipaddress
import re

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

parser = argparse.ArgumentParser(description='Espectacular escaner de puertos', epilog='@jabaselga')
group = parser.add_mutually_exclusive_group()
group.add_argument("-p", "--ports", nargs='?', help="Ports to scan",type=check_ports)
group.add_argument("-f", "--full", help="Scan all port range (0-65535)", action='store_true')
group.add_argument("-s", "--sort", help="Scan more interesting ports (22, 80, 443, ...)", action='store_true')
parser.add_argument("-i", "--ip", metavar='A.B.C.D', help="IP to port scan", type=check_ip)
args = parser.parse_args()

print (f'{args.ports}')
print (f'{args.full}')
print (f'{args.sort}')
print (f'{args.ip}')


port_to_scan = sorted(list(set(eval_port(args.ports))))
print (port_to_scan)

