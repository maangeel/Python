#25. Repite el programa número 23 pero en esta ocasión utilizando
#operadores lógicos.

#inputs
nota = float(input("Introduce tu nota: "))

if nota >= 8.5 and nota <= 10:
    print(f"Tu nota es un {nota}, has sacado un excelente.")
elif nota >= 6.5 and nota < 8.5:
    print(f"Tu nota es un {nota}, has sacado un notable.")
elif nota >= 5 and nota < 6.5:
    print(f"Tu nota es un {nota}, has sacado un satosfactorio.")
elif nota < 5:
    print(f"Tu nota es un {nota}, has sacado un insuficiente.")
else:
    print("La nota que has introducido no está entre 0 y 10.")