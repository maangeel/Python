#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de lengua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos

#listas
nombres = []
ingles = []
caste = []
cata = []

#variables
mediaIng = 0
mediaCaste = 0
mediaCata = 0
medianaIng = 0
medianaCaste = 0
medianaCata = 0
repetir = "s"

while repetir.upper() == "S":
    nombre = input("Introduce estudiante: ")
    nombres.append(nombre) #añade a la lista

    nota = float(input("Nota Inglés: "))
    ingles.append(nota)

    nota = float(input("Nota Castellano: "))
    caste.append(nota)

    nota = float(input("Nota Catalán: "))
    cata.append(nota)

    repetir = input("Deseas introducir otro alumno s/n: ")

print("Inglés:",ingles)
print("Castellano:",caste)
print("Catalán:",cata)

#cálculo de medias
for i in ingles:
    sumaIng += i
    mediaIng = sumaIng/len(ingles)

for j in caste:
    sumaCaste += j
    mediaCaste = sumaCaste/len(caste)

for x in cata:
    sumaCata += x
    mediaCata = sumaCata/len(cata)

#cálculo de medianas


print(f"\n La media en inglés es:")