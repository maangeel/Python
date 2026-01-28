#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra

import random

lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)

palabra = random.choice(lista) #escoge un valor al azar

adivina = input("Introduce la palabra secreta: ")

while adivina != palabra:
    print("SIGUE JUGANDO")
    adivina = input("Introduce la palabra secreta: ")

else:
    print("ACERTASTE")