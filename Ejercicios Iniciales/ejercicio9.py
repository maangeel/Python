#9. programa que pida los segundos y muestre por pantalla
#y en la misma frase los minutos y las horas.

#input
segundos = int(input("Introduce un número de segundos en formato entero: "))

#conversión
minutos = segundos / 60
minutos = round(minutos, 2)
horas = segundos / 3600
horas = round(horas, 2)

print(f"{segundos} segundos equivalen a {minutos} minutos o en horas serían {horas} horas.")