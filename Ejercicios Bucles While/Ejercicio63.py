#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.

import random
repetidor = 0
randomNum = 0
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

while repetidor != 100:
    randomNum = random.randint(1,6) #tira dado
    if randomNum == 1:
        uno+=1
    if randomNum == 2:
        dos+=1
    if randomNum == 3:
        tres+=1
    if randomNum == 4:
        cuatro+=1
    if randomNum == 5:
        cinco+=1
    if randomNum == 6:
        seis+=1
    repetidor+=1 #variable que controla el bucle

print("Uno:",uno) #prints
print("Dos:",dos)
print("Tres:",tres)
print("Cuatro:",cuatro)
print("Cinco:",cinco)
print("Seis:",seis)