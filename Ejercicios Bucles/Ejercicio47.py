#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida

#inputs
a = int(input("Introduce el primer valor del intervalo: "))
b = int(input("Introduce el segundo valor del intervalo: "))

if a < b:
    for i in range(a, b + 1): #en ascendente
        if i!=b: #se encarga de comprobar el último valor para evitar que aparezca un guión al final
            print(i, end="-") 
        else:
            print(i) #el último valor aparece sin guión final
elif a > b:
    for j in range(a, b - 1, -1): #en descendiente
        if j!=b: #se encarga de comprobar el último valor para evitar que aparezca un guión al final
            print(j, end="-")
        else:
            print(j)
else:
    print(a) #si a y b son iguales