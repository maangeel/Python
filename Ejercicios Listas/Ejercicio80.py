#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.

num = input("Introduce un número: ")

if num.count(".")==1: #comprueba que no haya varios puntos
    partes = num.split(".") #hace dos listas separando decimal de entero
    if partes[0].isdigit() and partes[1].isdigit(): #comprueba que sea todo numérico
        print("Es un número con decimales")
    else:
        print("No es un número con decimales")
else:
    print("No es un número con decimales")
