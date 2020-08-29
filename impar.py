## Programa para calucular si un numero solicitado es impar o par.
##
## keito99@protonmail.com
## 29/08/2020
##
##
num=int(input ("Introduce un numero:"))
## Determino si es impar/par con el resto de una división
res=num%2
#print ("Resultado {}",res)
if (res!=0):
	print ("El numero",num,"no es par")
else:
	print ("El numero",num,"es par")
