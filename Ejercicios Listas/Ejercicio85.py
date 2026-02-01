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

#cálculo de medias
mediaIng = sum(ingles)/len(ingles)
mediaCaste = sum(caste)/len(caste)
mediaCata = sum(cata)/len(cata)

#cálculo de medianas
ingles_orden = sorted(ingles)
caste_orden = sorted(caste)
cata_orden = sorted(cata)

def calcular_mediana(lista): #función que calcula mediana
    n = len(lista)
    mitad = n // 2
    if n % 2 == 0:  #longitud par
        return (lista[mitad - 1] + lista[mitad]) / 2
    else:  #impar
        return lista[mitad]

medianaIng = calcular_mediana(ingles_orden)
medianaCaste = calcular_mediana(caste_orden)
medianaCata = calcular_mediana(cata_orden)

#prints
print("\nInglés:",ingles)
print("Castellano:",caste)
print("Catalán:",cata)

print("\nRESUMEN")

print("La media en inglés es:", round(mediaIng, 1))
print("La media en castellano es:", round(mediaCaste, 1))
print("La media en catalán es:", round(mediaCata, 1))

print("La mediana en inglés es:", medianaIng)
print("La mediana en castellano es:", medianaCaste)
print("La mediana en catalán es:", medianaCata)