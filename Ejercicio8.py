Cuenta atrás: Escribe un programa que cuente hacia atrás desde 10 hasta 0.

conteo = [] #creamos una lista vacia
for i in range(10,0,-1): # Con "for" recorremos en un rango de 10 a 0 determinado con "range" que se guarda en "i"
       conteo.append(i) #Con "append" con el nombre de la variable al inicio añadimos los valores de "i" que son los numeros del 10 al 0

print(conteo)
