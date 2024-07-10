Par o Impar: Escribe un programa que determine si un número introducido por el usuario es par o impar.

numero1 = int(input("Ingrese un número: ")) #Pedimos al usuario el numero que quiera saber si es par o impar

if numero1 % 2 == 0: #Si el numero es divisible para 2 con residuo cero es par
   print("El numero es par")
else: #Si no cumple la condicion anterior logicamente es impar
   print("El numero es impar")
