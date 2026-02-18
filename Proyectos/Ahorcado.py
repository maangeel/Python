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
    global palabra_secreta
    global lista_partida
    palabra_secreta = random.choice(lista_palabrasecreta)
    lista_partida = ["_"] * len(palabra_secreta)
    print(",".join(lista_partida)) #join para quitar lista y mostrar solo la palabra con comas
    global intentos
    intentos = 0
    lista_palabrasecreta.remove(palabra_secreta)

#añadir letras a la partida
def agregar_letra(letra):
    global lista_partida
    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)): #recorre la palabra secreta para encontrar la letra y sustituirla en la lista partida
            if palabra_secreta[i] == letra:
                lista_partida[i] = letra
    else:
        global intentos
        lista_ahorcado.append(letras_ahorcado[intentos]) #sustituye la letra por la letra del ahorcado correspondiente al número de intentos
        intentos += 1
    print(",".join(lista_partida))

def partida(): #función para jugar la partida
    while lista_ahorcado != letras_ahorcado:
        agregar_letra(input("Ingresa una letra: ").lower())
    if "_" not in lista_partida:
        print("¡Felicidades! Has ganado. La palabra era:", palabra_secreta)
    else:
        print("¡Has perdido! La palabra era:", palabra_secreta)
    print(",".join(lista_partida))


#PARTIDA
randomizar_palabra()
partida()