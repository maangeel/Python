#JUEGO DEL AHORCADO

import random

lista_palabrasecreta = ["python", "programacion", "ahorcado", "juego", "desarrollo", "computadora", "teclado", "raton", "monitor", "tecnologia"]
palabra_secreta = ""
lista_partida = []
lista_ahorcado = []
letras_ahorcado = ["A", "H", "O", "R", "C", "A", "D", "O"]
intentos = 0


#randomizar palabra
def randomizar_palabra():
    global palabra_secreta #variable global para usarla en otras funciones
    palabra_secreta = random.choice(lista_palabrasecreta)
    global lista_partida
    lista_partida = ["_"] * len(palabra_secreta)
    print(",".join(lista_partida)) #join para quitar lista y mostrar solo la palabra con comas
    global lista_ahorcado
    lista_ahorcado = []
    global intentos
    intentos = 0

#añadir letras a la partida
def agregar_letra(letra):
    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                lista_partida[i] = letra
    else:
        lista_ahorcado.append(letras_ahorcado[intentos])
        global intentos
        intentos += 1

