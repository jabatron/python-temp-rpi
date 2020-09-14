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
- 20200914 via web

Ejemplo de uso, en el navegador poner:

http://localhost:8080/tablas/6

LIBRERIAS 
pip install bottle
"""

from bottle import route, run, template

@route('/tablas/<name>')
def index(name):

    if name.isnumeric():
        tablas = int(name) + 1
        pagina = '<b>Escribir tablas hasta la del {{name}}</b>! <br>'

        for i in range (1, tablas):
            pagina = pagina + '<b>Imprimiendo tabla del {}</b><br>'. format(i)
            # del 1 hasta el 12
            for j in range (1, 13):
                pagina = pagina + ('{} x {} = {} <br>'. format (i, j, i*j))
    else:
        pagina = '<b>El dato {{name}} no es un número</b>! <br>'
 

    return template(pagina, name=name)

print ('Escribe en el navegador ')
print ('')
print ('http://localhost:8080/tablas/<num>')
print ('<num> -> numero de tablas a imprimir')
print ('')

run(host='localhost', port=8080)