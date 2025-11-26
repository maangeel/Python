#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
randomNum = random.randint(0,1000) #número entre 0 y 1000
num = int(input("Introduce un número entre 0 y 1000: "))
intentos=1

while num!=randomNum: #si no acierta
    if num>randomNum: #si es mayor
        print("El número que has introducido es mayor")
        intentos+=1 #suma intentos
        num = int(input("Introduce un número entre 0 y 1000: "))
    else: #si es menor
        print("El número que has introducido es menor")
        intentos+=1 #suma intentos
        num = int(input("Introduce un número entre 0 y 1000: "))
else:
    print(f"Acertaste, has realizado {intentos} intentos.")