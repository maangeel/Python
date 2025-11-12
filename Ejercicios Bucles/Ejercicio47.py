#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida

#inputs
a = int(input("Introduce el primer valor del intervalo: "))
b = int(input("Introduce el segundo valor del intervalo: "))

if a < b:
    for i in range(a, b + 1): #en ascendente
        print(i, end="-")
elif a > b:
    for j in range(a, b - 1, -1): #en descendiente
        print(j, end="-")
else:
    print(a) #si a y b son iguales