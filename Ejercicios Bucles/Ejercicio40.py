#40. Crea un programa que cuente todos los números pares hasta el número 50

#inicialización de variables
pares = 0
impares = 0

for i in range(1,51):
    if i%2==0:
        pares +=1
    else:
        impares+=1

print(f"El total de pares es: {pares}")
print(f"El total de impares es: {impares}")