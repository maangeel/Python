#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.

#listas de variables
consonantes = ""
vocales = ""

#input
word=input("Introduce una palabra: ")

for i in word:
    if i.upper() in "AEIOU": #comprueba que la letra en mayúsculas sea vocal
        vocales += i #concatena las vocales
    else:
        consonantes += i


print(f"Las consonantes de la palabra {word.lower()} son: {consonantes.lower()}.") #convierte a minúsculas para evitar errores
print(f"Las vocales de la palabra {word.lower()} son: {vocales.lower()}.")