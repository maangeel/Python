#variables
sumPos = 0 #suma de positivos
sumNeg = 0 #suma de negativos

for i in range(6): #bucle 6 repeticiones
    valor = int(input("Introduce un valor: "))
    if valor >= 0:
        sumPos+=valor #suma el valor
    else:
        sumNeg+=valor

print(f"Suma de números positivos: {sumPos}")
print(f"Suma de números negativos: {sumNeg}")