#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.

lista1 = []
rep = int(input("Introduce el número de palabras: "))

for i in range(rep):
    palabra = input(f"Introduce la {i+1}ª palabra: ")
    lista1.append(palabra)

lista2 = lista1.copy() #duplica lista
lista2.reverse() #invierte el orden

print(f"Lista1 contiene: {lista1}")
print(f"Lista2: {lista2}")