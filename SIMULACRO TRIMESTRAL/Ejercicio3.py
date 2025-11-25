#declaración de variables
producto = 1
pares = 0

#input
cifraNumber = int(input("Introduce la cantidad de cifras: "))
val1 = input("Introduce el número: ")

if len(val1) == cifraNumber:
    for i in val1:
        producto*=int(i)
        if int(i)%2==0:
            pares+=1
    print(f"Producto de cifras: {producto}")
    print(f"Cifras pares {pares}")
else:
    print("Longitud incorrecta")