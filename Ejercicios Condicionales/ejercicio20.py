#20. A partir del ejercicio anterior, forzar que el usuario solo
#pueda introducir por teclados números entre 0 y 10

#inputs
var1 = float(input("Introduce un valor: "))
var2 = float(input("Introduce otro valor: "))

if var1 > 0 and var1 < 10 and var2 > 0 and var2 < 10: #están entre 1 y 10
    if var1 < var2: #si var1 es mayor a var2
        print(f"El número {var2} es mayor que el número {var1}.")

    elif var1 > var2: #si var1 es menor a var2
        print(f"El número {var1} es mayor que el número {var2}.")

    else: #si son iguales
        print("Ambos números son iguales.")
else: #si no cumple la condición de estar entre 0 y 10
    print("Uno o los dos números están fuera de los límites establecidos.")