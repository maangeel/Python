#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.


lista1 = ["casa","mesa","sal","sol","agua"]
lista2 = ["casa","luz","tres","tren","sol","pan"]
repetidas=[]
noRepetidas=[]

for i in lista2:
    if i in lista1:
        repetidas.append(i)
    else:
        noRepetidas.append(i)

for j in lista1:
    if j in lista2 and j not in repetidas:
        repetidas.append(j)
    elif j not in lista2 and j not in noRepetidas:
        noRepetidas.append(j)


print("Están repetidas:",repetidas)
print("No están repetidas:",noRepetidas)