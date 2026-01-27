#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

#creación de la lista

lista1 = ['a','b','D','x','r','X','3','h','w','2','i']

#CREACIÓN LISTA NUMÉRICA
numeros = []
#CREACIÓN LISTA LETRAS
letras = []

for i in lista1: #clasificación de caracteres
    if i.isalpha():
        letras.append(i)
    else:
        numeros.append(i)

#input ordenar
while True:
    try:
        orden = int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
        if orden == 1 or orden == 2:
            break
        else:
            print("Error")
    except ValueError:
        print("Error")

if orden == 1: #ascendente
    sortedNum = sorted(numeros)
    sortedLetra = sorted(letras, key=str.lower)

if orden == 2: #descendente
    sortedNum = sorted(numeros, reverse=True)
    sortedLetra = sorted(letras, key=str.lower, reverse=True)

print(sortedNum)
print(sortedLetra)