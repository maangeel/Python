#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no

lista1 = ["casa","mesa","sal","sol","agua"]
lista2 = ["casa","luz","tres","tren","sol","pan"]
repetidas=[]
noRepetidas=[]

#comprueba palabras repetidas a lista2
for i in lista2:
    if i in lista1:
        repetidas.append(i)
    else:
        noRepetidas.append(i)


print("Están repetidas:",repetidas)
print("No están repetidas:",noRepetidas)