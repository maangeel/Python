#16. Utiliza el método sqrt de la librería math para calcular la raíz
#cuadrada de un número. El resultado de la raíz cuadrada divídelo entre
#2 de manera que se obtenga siempre un resultado entero. Haz que se
#muestre por pantalla los dos resultados de todo el proceso(raíz y división).

import math

#inputs
valor = float(input("Introduce un valor: "))

#cálculos
raiz = math.sqrt(valor)
divInt = raiz//2

print(f"El resultado de la raiz es: {raiz}")
print(f"El resultado de la divisió entera es: {divInt}")