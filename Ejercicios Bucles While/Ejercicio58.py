#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random

intent=1

randNum = int(input("Introduce un valor entre 1 y 5: "))

while not randNum>=1 or not randNum<=5:
    print("Valor no apto")
    randNum = int(input("Introduce un valor entre 1 y 5: "))

randomNumber = random.randint(1,5) #random número

while randNum!=randomNumber and intent<3: #3 intentos para acertar
    print("Número no acertado")
    randNum = int(input("Introduce un valor entre 1 y 5: "))
    intent+=1

if randNum==randomNumber: #salir del bucle comprueba por última vez
    print("Número acertado")
else:
    print("Número no acertado")