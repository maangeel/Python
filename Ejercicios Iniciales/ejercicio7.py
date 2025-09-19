#7. programa que calcule dos operandos con los 7 operadores vistos en clase.
# ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

#inputs
var1 = float(input("Introduce un valor: "))
var2 = float(input("Introduce otro valor: "))

#suma
suma = var1 + var2
print(f"El resultado de la suma de {var1} + {var2} es {suma}.")

#resta
resta = var1 - var2
print(f"El resultado de la resta de {var1} + {var2} es {resta}.")

#multiplicación
multi = var1 * var2
print(f"El resultado de la multiplicación de {var1} * {var2} es {multi}.")

#división
divi = var1 / var2
divi = round(divi, 2) #redondear 2 decimales
print(f"El resultado de la división de {var1} / {var2} es {divi}.")

#división exacta
diviExact = var1 // var2
print(f"El resultado de la división exacta de {var1} / {var2} es {diviExact}.")

#potencia
pote = var1 ** var2
print(f"El resultado de la potencia de {var1} elevado a {var2} es {pote}.")

#módulo
modu = var1 % var2
print(f"El resto de dividir {var1} / {var2} da {modu}.")