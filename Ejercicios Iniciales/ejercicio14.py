#14. Realiza un programa que a partir de introducir el diámetro de un
#círculo calcule el área y perímetro. Importa la librería math y utiliza
#el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math

#inputs
diam = float(input("Introduce el valor del diámetro: "))

#cálculo radio
r = diam/2

#cálculo área
a = math.pi*r**2
a = round(a,1)

#cálculo perímetro
p = math.pi * diam
p = round(p,1)

print(f"El perímetro del circulo es: {p}")
print(f"El área del círculo es: {a}")