#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida)...

import random

partidasNum = int(input("Introduce el número de partidas: "))
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)

palabra = random.choice(lista) #escoge un valor al azar

puntosTotalesList = []
puntosTotalesSuma = 0

intentos = 0
puntuacionMax = 8
puntuacion = 0

mediaPartidas = 0

#code de todas las partidas
for i in partidasNum: #repeticion partidas
    adivina = input("Introduce la palabra secreta: ")
    while adivina != partidasNum: #bucle de una partida
        print("SIGUE JUGANDO")
        intentos+=1 #cuenta intentos
        adivina = input("Introduce la palabra secreta: ")
    else:
        print("ACERTASTE")
    puntuacion = puntuacionMax-intentos
    puntosTotalesList.append(puntuacion)

puntosTotalesSuma = sum(puntosTotalesList)
mediaPartidas = partidasNum*4
