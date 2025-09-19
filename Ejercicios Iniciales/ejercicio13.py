#13. Realiza un programa que, a partir introducir el lado de un cubo,
#presente por pantalla el área y para calcular el volumen utiliza
#el operador de exponente.

#inputs
lado = float(input("Introduce el lado del cubo: "))

#cálculos
area = lado ** 2
vol = lado **3

print(f"El área es de: {area}.")
print(f"El volumen es de: {vol}.")