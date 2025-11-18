#41. Imprime el siguiente patrón utilizando for:

for i in range(5, 0, -1): #recorre los valores de 5 a 0
    for j in range(i, 0, -1): #comienza a contar desde el valor de i y resta 1
        print(j, end="") #end sirve para no hacer el salto de línea en el print
    print("") #deja un hueco en blanco