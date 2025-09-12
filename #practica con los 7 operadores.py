#practica con los 7 operadores
#calculadora

print("Hay 7 operadores en python: suma, resta, multiplicacion, division, division exacta, modulo y potencia")
operador = input("Escoge un tipo de Operación: ")

if (operador=="suma"):
    print("Has seleccionado suma.")
    valor1 = float(input("A continuación escoge el primer valor: "))
    valor2 = float(input("Escoge un segundo valor: "))
    resultado = valor1+valor2
    print(f"La suma de {valor1} + {valor2} da: {resultado}")

elif (operador=="resta"):
    print("Has seleccionado resta.")
    valor1 = float(input("A continuación escoge el primer valor: "))
    valor2 = float(input("Escoge un segundo valor: "))
    resultado = valor1-valor2
    print(f"La resta de {valor1} - {valor2} da: {resultado}")

elif (operador=="multiplicacion"):
    print("Has seleccionado multiplicación.")
    valor1 = float(input("A continuación escoge el primer valor: "))
    valor2 = float(input("Escoge un segundo valor: "))
    resultado = valor1*valor2
    print(f"La multiplicación de {valor1} * {valor2} da: {resultado}")

elif (operador=="division"):
    print("Has seleccionado división.")
    valor1 = float(input("A continuación escoge el primer valor: "))
    valor2 = float(input("Escoge un segundo valor: "))
    resultado = valor1/valor2
    print(f"La división de {valor1} / {valor2} da: {resultado}")

elif (operador=="division exacta"):
    print("Has seleccionado división exacta.")
    valor1 = float(input("A continuación escoge el primer valor: "))
    valor2 = float(input("Escoge un segundo valor: "))
    resultado = valor1//valor2
    print(f"La división exacta de {valor1} / {valor2} da: {resultado}")

elif (operador=="modulo"):
    print("Has seleccionado módulo.")
    valor1 = float(input("A continuación escoge el primer valor: "))
    valor2 = float(input("Escoge un segundo valor: "))
    resultado = valor1-valor2
    print(f"El módulo de {valor1} / {valor2} da: {resultado}")

elif (operador=="potencia"):
    print("Has seleccionado potencia.")
    valor1 = float(input("A continuación escoge el primer valor: "))
    valor2 = float(input("Escoge un segundo valor: "))
    resultado = valor1%valor2
    print(f"{valor1} elevado a {valor2} da: {resultado}")

else:
    print("No has escrito correctamente el operador.")
    print("Asegúrate de escribirlo sin acentos ni mayúsculas.")