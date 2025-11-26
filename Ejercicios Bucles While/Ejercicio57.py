#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random

randNum = int(input("Introduce un valor entre 1 y 5: "))

while not randNum>=1 or not randNum<=5: #controla que el valor sea entre 1-5
    print("Valor no apto")
    randNum = int(input("Introduce un valor entre 1 y 5: "))

randomNumber = random.randint(1,5) #genera número del 1-5

while randNum!=randomNumber:
    print("Número no acertado")
    randNum = int(input("Introduce un valor entre 1 y 5: "))

else:
    print("Número acertado")