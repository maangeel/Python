#10. Introduce por teclado dos números y muestre por pantalla la
#siguiente información: cociente, resto y si el dividendo es par o impar.

#inputs
var1 = float(input("Introduce el primer valor: "))
var2 = float(input("Introduce el segundo valor: "))

#cociente
cociente = var1 / var2
print(f"El cociente es: {cociente}")

#resto
resto = var1 % var2
print(f"El resto es: {resto}.")

#dividendo par o impar
parImpar = var1 % 2
if (parImpar == 1):
    print("El dividendo es impar.")
else:
    print("El dividendo es par.")