#6. A partir del programa 5. Haz que se muestre por pantalla
#también la frase en el orden inverso en que se han introducido las palabras.

#entrada input
palabra1 = input("Introduce una palabra: ")
palabra2 = input("Introduce otra palabra: ")
palabra3 = input("Introduce otra palabra: ")
palabra4 = input("Introduce otra palabra: ")
palabra5 = input("Introduce otra palabra: ")

#print
print(palabra5,palabra4,palabra3,palabra2,palabra1)
print(f"{palabra5}{palabra4}{palabra3}{palabra2}{palabra1}")
print(f"{palabra5}, {palabra4}, {palabra3}, {palabra2}, {palabra1}.")