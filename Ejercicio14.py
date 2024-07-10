Factorial de un número: Escribe un programa que calcule el factorial de un número introducido por el usuario.

numero_usuario = int(input("Introduce un número: ")) #Solicitamos el numero
factorial = 1 #Una variable con valor 1
for i in range(1, numero_usuario + 1): #Recorremos en un rango de 1 a el numero ingresado por el usuario
    factorial *= i #Multiplicamos el factorial por el numero ingresado
print("El factorial de", numero_usuario, "es", factorial)
