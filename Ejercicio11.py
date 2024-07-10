Invertir una cadena: Escribe un programa que invierta una cadena introducida por
#el usuario.


cadena = input("Introduce una cadena") #Solicitamos la cadena que necesitamos invertir
cadenai = cadena[ ::-1] #Definimos que nuestra cadena ira del final hacia el inicio con los subindices [ ::-1]
print("La cadena invertida es", cadenai)
