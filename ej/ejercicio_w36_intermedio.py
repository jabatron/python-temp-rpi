"""

Proyecto Intermedio:

Crear un programa que detecte la hora actual del dispositivo, y 
en base a eso determine si es de día, tarde o noche, Luego debe pedirle 
al usuario que ingrese su nombre y saludar al usuario con la informacion 
ya obtenida, por ejemplo:

"Buenas tardes stary"

Opcional:

Dependiendo si es de dia, tarde o noche, el programa tiene que luego del 
saludo decirle una frase escogida aleatoriamente, por ejemplo:

"Buenas noches stary, ya es hora de dormir", 
"Buenas noches stary, hasta mañana"

nota:investigar cuando es de dia, tarde o noche para realizar este programa
code:#proyIn002


RESTRICCIONES:

MAÑANA -> de 6:00 a 14:59
TARDE -> de 15:00 a 20:59
NOCHE -> de 21:00 a 5:00

jose angel - @jabaselga
v0.1 020920 estructura del programa


"""
from datetime import time, datetime

# frases -> [[mañana], [tarde], [noche]]
frases = [  ["Que pases un buen día", "Que te sea leve", "Divierte"],                                           # frases mañana
            ["Que duermas bien la siesta", "Sal a pasear", "No estes mucho rato en el bar"],                    # frases tarde
            ["Pronto a dormir", "No te quedes mucho rato viendo la TV", "Que sueñes con los angelitos"]         # frases noche
        ]

manana = time (hour=6, minute=0, second=0)      # a partir de esta hora es mañana
tarde = time (hour=14, minute=0, second=0)      # a partir de esta hora es tarde
noche = time (hour=21, minute=0, second=0)      # a partir de esta hora es noche

# Sacamos la hora actual del sistema
hora = datetime.now().time()

if (hora >= manana) and (hora < tarde):
    estado = 0                                  #
elif (hora >= tarde) and (hora < noche):
    estado = 1
else:
    estado = 2

print (type(hora))
print (hora)

print (type(noche))
print (noche)
