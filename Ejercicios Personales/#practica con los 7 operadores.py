#practica con los 7 operadores
#calculadora

#Bienvenida
print("Bienvenido a la Calculadora básica de Python")

#declaración variable continuar donde se asegura que el usuario quiera ejecutar el programa
continuar = input("Para continuar pulsa s, para finalizar pulsa n:")


#inicio de un bucle
while continuar == "s":
    print("Hay 7 operadores en python: suma, resta, multiplicacion, division, division exacta, modulo y potencia")
    operador = input("Escoge un tipo de Operación: ")

    #suma de dos valores
    if (operador=="suma"):
        print("Has seleccionado suma.")
        valor1 = float(input("A continuación escoge el primer valor: "))
        valor2 = float(input("Escoge un segundo valor: "))
        resultado = valor1+valor2
        print(f"La suma de {valor1} + {valor2} da: {resultado}")

    #resta de valores
    elif (operador=="resta"):
        print("Has seleccionado resta.")
        valor1 = float(input("A continuación escoge el primer valor: "))
        valor2 = float(input("Escoge un segundo valor: "))
        resultado = valor1-valor2
        print(f"La resta de {valor1} - {valor2} da: {resultado}")

    #multiplicación de valores
    elif (operador=="multiplicacion"):
        print("Has seleccionado multiplicación.")
        valor1 = float(input("A continuación escoge el primer valor: "))
        valor2 = float(input("Escoge un segundo valor: "))
        resultado = valor1*valor2
        print(f"La multiplicación de {valor1} * {valor2} da: {resultado}")

    #división de valores
    elif (operador=="division"):
        print("Has seleccionado división.")
        valor1 = float(input("A continuación escoge el primer valor: "))
        valor2 = float(input("Escoge un segundo valor: "))
        resultado = valor1/valor2
        print(f"La división de {valor1} / {valor2} da: {resultado}")

    #división exacta de valores
    elif (operador=="division exacta"):
        print("Has seleccionado división exacta.")
        valor1 = float(input("A continuación escoge el primer valor: "))
        valor2 = float(input("Escoge un segundo valor: "))
        resultado = valor1//valor2
        print(f"La división exacta de {valor1} / {valor2} da: {resultado}")

    #resto de una división
    elif (operador=="modulo"):
        print("Has seleccionado módulo.")
        valor1 = float(input("A continuación escoge el primer valor: "))
        valor2 = float(input("Escoge un segundo valor: "))
        resultado = valor1%valor2
        print(f"El módulo de {valor1} / {valor2} da: {resultado}")

    #operador de potencias
    elif (operador=="potencia"):
        print("Has seleccionado potencia.")
        valor1 = float(input("A continuación escoge el primer valor: "))
        valor2 = float(input("Escoge un segundo valor: "))
        resultado = valor1**valor2
        print(f"{valor1} elevado a {valor2} da: {resultado}")

    #mensaje de error en caso de no coincidir con ningun operador
    else:
        print("No has escrito correctamente el operador.")
        print("Asegúrate de escribirlo sin acentos ni mayúsculas.")
    
    #verificador de que el usuario quiere continuar o finalizar
    continuar = input("Para continuar pulsa s, para finalizar pulsa n:")

print("Cerrando programa...")

