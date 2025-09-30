#21. Programa que calcula una ecuación de segundo grado. Controla
#que el valor de la raíz cuadrada no de un valor negativo
import math

a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de c: "))

#comprobar si la ecuación se puede hacer o no
ec1 = b**2-(4*a*c)
x1 = (-b+(math.pi(b**2+(4*a*c))))/(2*a)
x2 = (-b+(math.pi(b**2-(4*a*c))))/(2*a)

if ec1 < 0:
    print("La raíz no puede ser un valor negativo.")

else:
