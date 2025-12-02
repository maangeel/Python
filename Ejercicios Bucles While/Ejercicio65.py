#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.


val = int(input("Introduce un valor: ")) #input

#variables
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
sumaTotal = 0
mayor = val
menor = val

while val != -99:
    if val%2==0:
        pares+=1 #comprueba pares
    elif val==0:
        ceros+=1 #comprueba ceros
    else:
        impares+=1 #comprueba impares
    if val>0:
        positivos+=1 #comprueba positivos
    if val<0:
        negativos+=1 #comprueba negativos
    sumaTotal+=val#suma total
    if val>mayor:
        mayor=val
    if val<menor:
        menor=val
    val = int(input("Introduce un valor: "))
if val>mayor: #comprobación tras salir del bucle
    mayor=val
if val<menor:
    menor=val
    
print("RESUMEN")
#los prints solo aparecerán si el valor es mayor que 0
if pares>0:
    print(f"El número de pares es {pares}")
if impares>0:
    print(f"El número de impares es {impares}")
if positivos>0:
    print(f"El número de positivos es {positivos}")
if negativos>0:
    print(f"El número de negativos es {negativos}")
if ceros>0:
    print(f"El número de ceros es {ceros}")
print(f"El mayor valor es: {mayor}")
print(f"El menor valor es: {menor}")
print(f"El total es {sumaTotal}")