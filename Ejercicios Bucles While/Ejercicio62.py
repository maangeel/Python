#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

#variables
pares = ""
impares = ""

val1 = int(input("Introduce el primer valor del rango: "))
val2 = int(input("Introduce el segundo valor del rango: "))
if val1<val2: #comprueba que valor es mayor
    for i in range(val1,val2):
        if i%2==0:
            pares=pares+str(i)+"-" #concatena
        else:
            impares=impares+str(i)+"-"
else:
    for i in range(val2,val1):
        if i%2==0:
            pares=pares+str(i)+"-"
        else:
            impares=impares+str(i)+"-"
print("Los números pares son",pares[:-1])
print("Los números impares son",impares[:-1])