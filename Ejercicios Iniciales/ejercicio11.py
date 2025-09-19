#11. Realiza un programa que introduciendo el valor del lado
#de un cuadrado nos devuelva por pantalla en el área y el perímetro.

#input
lado = float(input("Introduce la medida de un lado de cuadrado: "))

#cálculos
per = lado * 4
area = lado ** 2

#prints
print(f"El perímetro del cuadrado es de: {per}.")
print(f"El área del cuadrado es de {area}.")