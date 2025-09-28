#15. Utiliza el valor Pi de la librería math para calcular el área y
#volumen de un cilindro, introduciendo por teclado el valor de radio
#y altura. Resultado con 2 decimales.

import math

#inputs
r = float(input("Introduce el valor del radio: "))
h = float(input("Introduce el valor de la altura: "))

#cálculos
aBase = math.pi * r**2
aLateral = 2 * math.pi * r * h
aTotal = 2 * aBase + aLateral
v = aBase * h

aTotal = round(aTotal,2)
v = round(v,2)

print(f"El área del cilindro es: {aTotal}")
print(f"El volumen del cilindro es: {v}")