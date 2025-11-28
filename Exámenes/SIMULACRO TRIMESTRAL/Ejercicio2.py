#bucle 7 repeticiones de input

list = [] #lista de variables

#declaración de variables
positivosSuma = 0
negativosSuma = 0
mayorCien = 0

for i in range(7):
    x = int(input("Introduce un valor entero: "))
    list.append(x)#añade el valor a la lista

for j in list:
    int(j) #j pasa a integer
    if j>0:
        positivosSuma+=j #suma el valor si es positivo
    else:
        negativosSuma+=j #suma el valor si es negativo
    if j>100:
        mayorCien+=1 #si es mayor a 100

print(f"Suma positivos: {positivosSuma}")
print(f"Suma negativos: {negativosSuma}")
print(f"Mayores de 100: {mayorCien}")