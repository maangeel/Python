#15. Utiliza el valor Pi de la librería math para calcular el área y
#volumen de un cilindro, introduciendo por teclado el valor de radio
#y altura. Resultado con 2 decimales.

import math

#inputs
r = float(input("Introduce el valor del radio: "))
h = float(input("Introduce el valor de la altura: "))

#cálculos
aBase = math.pi * r**2
v = aBase * h

aBase = round(aBase,2)
v = round(v,2)

print(f"El área del cilindro es: {aBase}")
print(f"El volumen del cilindro es: {v}")