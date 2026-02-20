#JUEGO DEL AHORCADO

import random

lista_palabrasecreta = ["python", "programacion", "ahorcado", "juego", "desarrollo", "computadora", "teclado", "raton", "monitor", "tecnologia"]
palabra_secreta = ""
lista_partida = []
lista_ahorcado = []
letras_ahorcado = ["A", "H", "O", "R", "C", "A", "D", "O"]
intentos = 0


#Función para randomizar la palabra secreta
def randomizar_palabra(listaPalabras):
    palabra_secreta = random.choice(listaPalabras)
    lista_partida = ["_"] * len(palabra_secreta)
    print(",".join(lista_partida))
    intentos = 0
    lista_palabrasecreta.remove(palabra_secreta)
    return palabra_secreta, lista_partida, intentos, lista_palabrasecreta


#añadir letras a la partida
def agregar_letra(letra):
    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)): #recorre la palabra para comprobar la letra
            if palabra_secreta[i] == letra:
                lista_partida[i] = letra #sustituye el guion bajo por la letra correcta
    else:
        global intentos
        lista_ahorcado.append(letras_ahorcado[intentos]) #añade una letra a AHORCADO
        intentos += 1
    print(",".join(lista_partida))
    print(" ".join(lista_ahorcado)) #imprime la palabra ahorcado
    return lista_partida, lista_ahorcado


def partida(lista_partida, lista_ahorcado): #función para jugar la partida
    while lista_ahorcado != letras_ahorcado:
        lista_partida, lista_ahorcado = agregar_letra(input("Ingresa una letra: ").lower())
    if "_" not in lista_partida:
        print("¡Felicidades! Has ganado. La palabra era:", palabra_secreta)
    else:
        print("¡Has perdido! La palabra era:", palabra_secreta)
    print(",".join(lista_partida))


#PARTIDA
palabra_secreta, lista_partida, intentos, lista_palabrasecreta = randomizar_palabra(lista_palabrasecreta)
lista_partida, lista_ahorcado = agregar_letra(input("Ingresa una letra: ").lower())
partida(lista_partida, lista_ahorcado)