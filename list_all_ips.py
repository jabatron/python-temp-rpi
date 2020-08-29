import psutil
import platform
import ipaddress

SO = platform.system()

if (SO == "Windows"):
    ip_so = 1
else: # (SO == "Linux")
    ip_so = 0
ip_ip = 1
ip_mk = 2

a = psutil.net_if_addrs()

ips = []
for i in a:
    net = []
    
    IP_str = a[i][ip_so][ip_ip]
    IP_class = ipaddress.ip_address(IP_str)

    if (IP_class.version == 4) and (not IP_class.is_link_local) and (not IP_class.is_loopback) :
        net.append(a[i][ip_so][ip_ip]) 
        net.append(a[i][ip_so][ip_mk])  
        ip_prefix_str = '0.0.0.0/'+ a[i][ip_so][ip_mk]
        ip_prefix = ipaddress.IPv4Network(ip_prefix_str).prefixlen
        net.append(ip_prefix)
        
        IP2= net[0] + '/' + str(net[1])
        cdir = ipaddress.ip_network (IP2, strict=False)
        net.append(cdir)

        ips.append(net)

print (ips [0][3])
hosts = list (ipaddress.ip_network(ips[0][3]).hosts())
print (hosts)

print (ips)

print (str(hosts[25]))