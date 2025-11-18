#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.

rep = int(input("Introduce la cantidad de números que deseas introducir: "))

#inicialización de las variables
posTotal = 0
negTotal = 0
ceroTotal = 0

for i in range(rep): #bucle para repetir la entrada de datos y comprobar si es +, - o 0
    n = float(input("Introduce un número: "))
    if n>0:
        posTotal += 1
    elif n<0:
        negTotal += 1
    else:
        ceroTotal += 1

print(f"La cantidad de números positivos es: {posTotal}")
print(f"La cantidad de números negativos es: {negTotal}")
print(f"La cantidad de números ceros es: {ceroTotal}")