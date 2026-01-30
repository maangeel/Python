#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 

import random

lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
randomWord = random.choice(lista) #escoge una palabra al azar
randomList = list(randomWord) #convierte a lista la palabra
wordSorted = sorted(randomList) #sortea ls palabra sin modificarla

intentos = 1
adivina = ""

print(wordSorted)

while not adivina==randomWord and intentos<=3:
    adivina = input("Introduce palabra correcta: ")
    if not adivina==randomWord:
        print("No has acertado")
    intentos+=1
else:
    if adivina==randomWord:
        print("Acertaste")
    else:
        print("No has acertado ninguno de los intentos")