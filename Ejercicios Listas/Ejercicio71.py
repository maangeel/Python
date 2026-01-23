#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.

listaLetras = []

repetir = "s"

while repetir in "sS":
    letra = input("Introduce una letra: ")
    while True:
        try: #comprueba si es númerico o no
            int(letra)
            letra = input("Introduce una letra: ")
        except ValueError:
            break
    if letra not in listaLetras:
        listaLetras.append(letra)
    repetir = input("Repetir s/n: ")
    
print(listaLetras)