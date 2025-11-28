var_total = 50 #variable inicial
valIntro = 1
#bucle, finaliza al incumplir condiciones
while not var_total>60 and not valIntro == 0:
    valIntro = int(input("Introduce un valor: ")) #repite el input
    if valIntro%2==0: #comprueba si es par o impar
        var_total+=valIntro
    else:
        var_total-=valIntro
    if var_total<=60:
        print(var_total)
print("Fin del programa") #mensaje final