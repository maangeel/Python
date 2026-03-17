#EN LA FASE 2 se han añadido los siguientes cambios:
    #mecánica de puntos


import random

#lista con cartas del 7 y medio
listaCartas = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12]

#valor de las cartas
valoresCartas = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]

totalValores = 0

#función para obtener una carta y su valor
def obtenerCarta():
    respuesta = input("\n¿Quieres una carta? (s/n): ")
    if respuesta == "s" and len(listaCartas) > 0:
        numeroCarta = random.randint(0,len(listaCartas)-1)
        valorCarta = valoresCartas[numeroCarta] #asignar el valor de la carta
        signoCarta = listaCartas[numeroCarta] #asignar el signo (1,2,3,4...Rey, sota) de la carta

        #eliminar la carta de la lista para que no se repita
        listaCartas.pop(numeroCarta-1)
        valoresCartas.pop(numeroCarta-1)
        return signoCarta, valorCarta, listaCartas, valoresCartas
    while respuesta != "s" and respuesta != "n":
        print("Por favor, ingresa 's' o 'n'.")
        respuesta = input("\n¿Quieres una carta? (s/n): ")
        
    else:
        return 0,0, listaCartas, valoresCartas
    
def partida(respuesta):

    global totalValores
    global listaCartas
    global valoresCartas

    totalValores = 0
    listaCartas = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12]
    valoresCartas = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]

    if respuesta != "s":
        print("¡Hasta luego!")
        return
    if respuesta == "s":
        print("Bienvenido al juego de 7 y Medio")

        #obtener la primera carta
        carta, valor, listaCartas, valoresCartas = obtenerCarta()
        print(f"Has obtenido la carta {carta} con valor {valor}")
        totalValores += valor
        print(f"Tu total actual es: {totalValores}")

        #resto de cartas
        while carta != 0 and valor != 0 and totalValores < 7.5:
            carta, valor, listaCartas, valoresCartas = obtenerCarta() #se actualizan los valores y listas
            print(f"Has obtenido la carta {carta} con valor {valor}")
            totalValores += valor
            print(f"Tu total actual es: {totalValores}")

        else:
            if totalValores > 7.5:
                print("Has perdido la partida")
            elif totalValores == 7.5:
                print("Enhorabuena, has ganado la partida")
            elif totalValores >=6 and totalValores <= 7:
                print(f"Has sido un poco conservador")
            else:
                print("Quizás tendrías que haber arriesgado un poco, ¿No?")


start = input("¿Quieres jugar al 7 y Medio? (s/n): ")
partida(start)

while start == "s":
    start = input("\n¿Quieres jugar otra partida? (s/n): ")
    partida(start)