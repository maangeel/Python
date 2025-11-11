#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:

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

print(f"Las consonantes de la palabra {word} son: {consonantes}.")
print(f"Las vocales de la palabra {word} son: {vocales}.")