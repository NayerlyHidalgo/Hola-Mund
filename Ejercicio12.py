Contar vocales: Escribe un programa que cuente el número de vocales en una
#cadena introducida por el usuario.

cadena = input("Introduce una cadena: ") #Solicitamos la cadena
vocales = "aeiouAEIOUáéíóùÁÉÍÓÚ" #Con una variable llamada "vocales" comparamos todo tipo de vocal que tenga escrita la cadena
contador = 0 #Un contador en cero para que cada bocal encontrada sumara uno
for vocal in cadena: #recorremos la cadena ingresasa "cadena" y la guardamos en "vocal"
    if vocal in vocales:
        contador += 1
print("La cadena tiene", contador, "vocales")
