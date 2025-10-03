#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para
#no distinguir entre mayúsculas y minúsculas

frase = "A quién madruga Dios ayuda"
palabras = ["madruga", "Dios", "dios"] #lista de palabras

frasMinus = frase.lower() #convertimos la frase a minúsculas

for n in palabras:
    indice = frasMinus.find(n.lower()) #convertimos las palabras de la lista en minúsculas también
    if indice != -1:
        print(f"La palabra está en la frase y está en el índice {indice}.")
    else:
        print(f"La palabra no está en la frase.")