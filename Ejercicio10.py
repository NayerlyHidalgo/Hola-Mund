num = int(input("Ingrese un numero")) #Solicitamos el numero que se desea saber si es primo


for n in range(2, int(num ** 0.5) + 1):  #recorrer en un rango de explicado ( 2, entero("elnumero que ingrese el usuario multiplicado por 0.5" mas 1)
    if num % n == 0: #Si el numero es divisible para "n"
        print("No es primo") #Imprime que no es primo

print("Es primo")
