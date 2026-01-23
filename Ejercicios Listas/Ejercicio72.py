#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista

listaLetras = []

repetir = "s"

while repetir in "sS":
    letra = input("Introduce una letra: ")
    if letra in "áàä":
        letra="a"
    if letra in "èéë":
        letra="e"
    if letra in "íìï":
        letra="i"
    if letra in "óòö":
        letra="o"
    if letra in "úùü":
        letra="u"
    while True:
        try: #comprueba si es númerico o no
            int(letra)
            letra = input("Introduce una letra: ")
        except ValueError:
            break
    if letra not in listaLetras:
        listaLetras.append(letra)
    repetir = input("Repetir s/n: ")
    if repetir not in "SsnN":
        repetir = input("Repetir s/n: ")
    
print(listaLetras)