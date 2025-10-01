#21. Programa que calcula una ecuación de segundo grado. Controla
#que el valor de la raíz cuadrada no de un valor negativo
import math

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

#comprobar si la ecuación se puede hacer o no
ec1 = (b**2-(4*a*c))


if ec1 < 0:
    print("La raíz no puede ser un valor negativo.")

else:
    raiz = math.sqrt(ec1)
    x1 = (-b+raiz)/(2*a)
    x2 = (-b-raiz)/(2*a)
    print(f"El valor de x1 es de: {x1}")
    print(f"El valor de x2 es de: {x2}")