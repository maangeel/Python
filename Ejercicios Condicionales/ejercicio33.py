#33. Programa un código que permita contar el número de vocales de la siguiente frase: No
#hay mal que dure cien años.

frase = "No hay mal que dure cien años"
vocales = ["a", "á", "à", "e", "é", "è","i", "í", "ì", "o", "ó", "ò", "u", "ú", "ù"]

for vocals in vocales:
    numVocals = frase.count(vocals)
    print(f"La vocal {vocals} aparece {numVocals} veces.")