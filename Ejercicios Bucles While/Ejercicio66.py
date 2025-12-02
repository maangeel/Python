#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 

import time #libreriía de tiempo
import random

uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0
randomNum = 0

tiempo = time.time() #comienza a contar tiempo

while tiempo<3: #hasta 3 segundos
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

print("RESUMEN")
print("Uno:",uno) #prints
print("Dos:",dos)
print("Tres:",tres)
print("Cuatro:",cuatro)
print("Cinco:",cinco)
print("Seis:",seis)