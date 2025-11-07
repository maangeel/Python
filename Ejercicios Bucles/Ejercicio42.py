#42. Imprima el siguiente patrón con el ciclo for:

#primer bloque
for i in range(0,5):#le asigna a i el recorrido del 1 al 5
    for j in range(i): #hace tantas repeticiones como valor de i
        print("*", end="") #imprime un asterisco y no salta a la siguiente línea
    print("")

#segundo bloque
for i in range(5,0,-1): #hace lo mismo a la inversa
    for j in range(i):
        print("*", end="")
    print("")