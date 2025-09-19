#8. programa que pida un número de horas y
#muestre por pantalla los minutos y segundos

#inputs
horas = int(input("Introduce un número de horas en formato entero: "))

#conversiones
minutos = horas * 60
segundos = horas * 3600
print(f"{horas} horas equivalen a {minutos} minutos o en segundos serían {segundos} segundos.")