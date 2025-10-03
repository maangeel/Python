#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda.
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su
#índice.

frase = "A quién madruga Dios ayuda"
palabras = ["madruga", "Dios", "dios"] #lista de palabras

for n in palabras: #las palabras se almacenan temporalmente en una variable llamada n hasta que se acabe el bucle
    indice = frase.find(n) #indice va a ser igual al valor de la posición de la palabra n
    if indice != -1: #el indice es -1 cuando la palabra no aparece en la frase
        print(f"La palabra está en la frase y está en el índice {indice}.")
    else:
        print(f"La palabra no está en la frase.")