#JUEGO DEL AHORCADO

import random
import time

textPartida = open("DatosPartida.txt", "a+")

lista_palabrasecreta = ["python", "programacion", "ahorcado", "juego", "desarrollo", "computadora", "teclado", "raton", "monitor", "tecnologia"]
palabra_secreta = ""
lista_partida = []
lista_ahorcado = []
letras_ahorcado = ["A", "H", "O", "R", "C", "A", "D", "O"]
intentos = 0
lista_aciertos = []
lista_errores = []


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
    global lista_aciertos
    global lista_errores
    if len(letra) != 1 or not letra.isalpha() or letra in lista_aciertos or letra in lista_errores: #en caso de ingresar un valor no válido
        print("Por favor, ingresa una letra válida.")
        return lista_partida, lista_ahorcado

    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)): #recorre la palabra para comprobar la letra
            if palabra_secreta[i] == letra:
                lista_partida[i] = letra #sustituye el guion bajo por la letra correcta
        lista_aciertos.append(letra) #añade la letra a la lista de aciertos
    else:
        global intentos
        lista_errores.append(letra)
        lista_ahorcado.append(letras_ahorcado[intentos]) #añade una letra a AHORCADO
        intentos += 1
    print(",".join(lista_partida))
    print(" ".join(lista_ahorcado)) #imprime la palabra ahorcado
    return lista_partida, lista_ahorcado


def partida(lista_partida, lista_ahorcado): #función para jugar la partida
    tiempo_inicio = time.time() #comienza a contar tiempo
    while lista_ahorcado != letras_ahorcado and "_" in lista_partida:
        lista_partida, lista_ahorcado = agregar_letra(input("Ingresa una letra: ").lower())
    if "_" not in lista_partida:
        tiempo_fin = time.time() #finaliza el contador
        tiempo_total_min = round((tiempo_fin - tiempo_inicio)//60)
        tiempo_total_sec = round((tiempo_fin - tiempo_inicio)%60, 2)
        print("¡Felicidades! Has ganado. La palabra era:", palabra_secreta)
    else:
        print("¡Has perdido! La palabra era:", palabra_secreta)
        tiempo_fin = time.time() #finaliza el contador
        tiempo_total_min = round((tiempo_fin - tiempo_inicio)//60)
        tiempo_total_sec = round((tiempo_fin - tiempo_inicio)%60, 2)
    return tiempo_total_min, tiempo_total_sec


continuar = "s"

while continuar == "s":

    #AGREGAR PALABRAS
    addWords = input("¿Quieres agregar una palabra al juego? (s/n): ").lower()
    if addWords == "s":
        nueva_palabra = input("Ingresa la nueva palabra: ").lower()
        if nueva_palabra not in lista_palabrasecreta:
            lista_palabrasecreta.append(nueva_palabra)
            print("Palabra agregada correctamente.")
        else:
            print("La palabra ya existe en la lista.")

    #PARTIDA
    palabra_secreta, lista_partida, intentos, lista_palabrasecreta = randomizar_palabra(lista_palabrasecreta)
    tiempo_total_min, tiempo_total_sec = partida(lista_partida, lista_ahorcado)
    print(f"Tiempo total de la partida: {tiempo_total_min} minutos y {tiempo_total_sec} segundos")
    continuar = input("¿Quieres jugar otra partida? (s/n): ").lower()
    textPartida.write(f"Fecha de partida: {time.strftime('%Y-%m-%d')}\n")
    textPartida.write(f"Hora de partida: {time.strftime('%H:%M')}\n")
    textPartida.write(f"Aciertos: {len(lista_aciertos)}\n")
    textPartida.write(f"Errores: {len(lista_errores)}\n")

else:
    print("¡Gracias por jugar! ¡Hasta la próxima!")
    print(f"Tus aciertos fueron: {', '.join(lista_aciertos)}")
    print(f"Tus errores fueron: {', '.join(lista_errores)}")