Tabla de multiplicar: Escribe un programa que muestre la tabla de multiplicar de un
#número introducido por el usuario.

numero = int(input("Ingrese un numero")) #Solicitamos el numero que se desea multiplicar

for tabla in range(1,11): #Recorremos con for un rango de 1 a 11 para saber la 10 tablas del numero ingresado que se guardan en "tabla"
      mul = numero * tabla #multiplicamos cada uno de los numeros (10) que estan en tabla por el numero ingresado(numero)
      print(mul)
