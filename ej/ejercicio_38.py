
""" 

Crea un programa que imprima las tablas de multiplicar, del 1 hasta el numero introducido por el usuario, ej:

1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
1 x 11 = 11
1 x 12 = 12

Nota: La tabla de cada numero termina en la multiplicacion del numero 12


jose angel - @jabaselga
- 20200914 primera versión


LIBRERIAS 
"""


# leo de la terminal hasta que introducen un número entero
num = False
while not num:
    try:
        tablas = int (input ('¿Hasta que tabla quieres imprimir? '))
        num = True
    except:
        print ('Hay que repetir, no has escrito un número entero!!')

# imprimo todas las tablas
for i in range (1, tablas + 1):
    print ('Imprimiendo tabla del {}'. format(i))
    # del 1 hasta el 12
    for j in range (1, 13):
        # hago formato en los string para que queden alineados
        print ('{} x {:>2} = {:>3} '. format (i, j, i*j))
