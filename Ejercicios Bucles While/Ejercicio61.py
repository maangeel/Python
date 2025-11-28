#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.

valor = int(input("Introduce el valor que quieres multiplicar: "))
tabla = 0
while tabla<10 and not (valor*tabla)>=40:#bucle con incremento
    tabla+=1
    print(valor*tabla)
print("Fin de programa")