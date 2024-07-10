Escribe un programa que determine si una cadena introducida por el usuario es un palíndromo.


cadena_usuario = input("Introduce una cadena: ")
cadena_usuario = cadena_usuario.replace(" ", "").lower()  # Eliminamos espacios y convertimos a minúsculas
if cadena_usuario == cadena_usuario[::-1]:  # Comparamos la cadena con su reversa
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")
