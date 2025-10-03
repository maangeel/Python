#33. Programa un código que permita contar el número de vocales de la siguiente frase: No
#hay mal que dure cien años.

frase = "No hay mal que dure cien años"
vocales = ["a", "e", "i", "o", "u"]

for vocals in vocales:
    numVocals = frase.count(vocals)
    print(f"La vocal {vocals} aparece {numVocals} veces.")