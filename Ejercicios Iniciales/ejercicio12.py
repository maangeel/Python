#12. Realiza un programa que, introduciendo en los valores de lado,
#base menor, base mayor y altura de un trapecio isósceles,
#nos devuelva por pantalla en el área y el perímetro.

#inputs
B = float(input("Introduce la base mayor: "))
b = float(input("Introduce la base menor: "))
h = float(input("Introduce la altura: "))

#cálculos
area = h*(B+b)/2
print(f"El area es de: {area}.")

lado = ((B-b) ** 2 + h ** 2)**0.5
per = lado * 2 + b + B
print(f"El perímetro es de: {per}.")