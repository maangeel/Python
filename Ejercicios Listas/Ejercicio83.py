#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida)...

import random

partidasNum = int(input("Introduce el número de partidas: "))
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)

palabra = random.choice(lista) #escoge un valor al azar

adivina = input("Introduce la palabra secreta: ")

puntosTotalesList = []
puntosTotalesSuma = 0

intentos = 0
puntuacionMax = 8
puntuacion = 0

mediaPartidas = 0

#code de todas las partidas
for i in range(partidasNum): #repeticion partidas
    intentos = 0
    puntuacionMax = 8
    while adivina != palabra: #bucle de una partida
        print("SIGUE JUGANDO")
        intentos+=1 #cuenta intentos
        adivina = input("Introduce la palabra secreta: ")
    else:
        print("ACERTASTE")
    puntuacion = puntuacionMax-intentos
    puntosTotalesList.append(puntuacion)
    
    #empieza la siguiente partida
    if not i==partidasNum-1:
        print(lista)
        palabra = random.choice(lista)
        adivina = input("Introduce la palabra secreta: ")

puntosTotalesSuma = sum(puntosTotalesList)
mediaPartidas = partidasNum*4

#salida de datos
if puntosTotalesSuma>=mediaPartidas: #en caso de superar la media
    print(f"Puntuación: {puntosTotalesList}")
    print(f"Tu puntuació ha sido de {puntosTotalesSuma}")
    print(f"La media de las partidas realizadas es {mediaPartidas}")
    print("Tienes buena suerte")
else:
    print(f"Puntuación: {puntosTotalesList}")
    print(f"Tu puntuació ha sido de {puntosTotalesSuma}")
    print(f"La media de las partidas realizadas es {mediaPartidas}")
    print("Dedícate al parchís")