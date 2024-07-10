Calculadora básica: Escribe un programa que realice operaciones básicas (suma, resta, multiplicación y división) entre dos números introducidos por el usuario.

numero1 = int(input(" Ingrese numero ")) #Solicitamos los dos valores al usuario y los convertimos en enteros
numero2 = int(input(" Ingrese numero "))

print("Menu: 1.-Suma 2.-Resta 3.-Division 4.-Multiplicacion")
op = input("Eliga la operacion") #Creamos un menu para elegir la operacion que deseemos

if op == "1": #Dependiendo de la opcion sumara, restara, dividara o multiplicara los dos valores que solicitamos
   suma = (numero1 + numero2)
   print("Suma")
   print(suma)
elif op == "2":
   resta = (numero1 - numero2)
   print("Resta")
   print(resta)
elif op == "3":
   division = (numero1 / numero2)
   print("Division")
   print(division)
elif op == "4":
   multiplicacion = (numero1 * numero2)
   print("Multiplicacion")
   print(multiplicacion)
