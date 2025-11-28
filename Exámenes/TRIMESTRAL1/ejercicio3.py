#variables
resultado = 0

#inputs
numCifras = int(input("Introduce el número de cifras: "))
numFinal = input("Introduce un número respetando el nº de cifras: ")

if len(numFinal)!=numCifras: #mensaje de error
    print("Error, no coincide con el número de cifras")
else:
    for i in numFinal: #recorre el número y suma cada cifra
        resultado+=int(i)
    print(f"Resultado: {resultado}")