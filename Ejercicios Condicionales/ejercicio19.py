#19. Programa que introduzca dos números y devuelva cuál de los dos
#es mayor, menor o son iguales

#inputs
var1 = float(input("Introduce un valor: "))
var2 = float(input("Introduce otro valor: "))

#si var1 es mayor a var2
if var1 < var2:
    print(f"El número {var2} es mayor que el número {var1}.")

elif var1 > var2:
    print(f"El número {var1} es mayor que el número {var2}.")

else:
    print("Ambos números son iguales.")