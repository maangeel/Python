#programa que calcula área de un triángulo equilátero.

import math #librería de mates

#inputs
a = float(input("Introduce el valor de un lado del triángulo: "))

#cálculo
area = round(((math.sqrt(3)/4)*(a**2)),2) #redondeo del cálculo

#salida
print(f"El área del triángulo es de {area}.")