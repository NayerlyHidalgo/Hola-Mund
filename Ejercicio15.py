Escribe un programa que calcule el índice de masa corporal (IMC) a partir del peso y la altura introducidos por el usuario

peso_usuario = float(input("Introduce tu peso en kg: ")) #Solicitamos el peso en numero flotante
altura_usuario = float(input("Introduce tu altura en m: ")) #Solicitamos la altura en numero flotante
imc_usuario = peso_usuario / (altura_usuario ** 2)  #Calculamos el IMC con la formula peso dividio para altura multiplicada por 2
print("Tu IMC es", round(imc_usuario, 2)) #Imprime el IMC redondeado a dos decimales

