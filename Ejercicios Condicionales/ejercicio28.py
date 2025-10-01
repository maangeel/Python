#28. Mejora el programa anterior para controlar también la introducción
#de símbolos. Utiliza elif.

letra = input("Introduce una letra: ")
if letra.isdigit(): #comprueba si es un dígito
    print("El valor introducido es un número.")
elif letra.isalpha(): #comrpueba si es una letra
    if letra.isupper(): #comprueba si es mayúsculas
        print("La letra es mayúscula.")
    else:
        print("La letra es minúscula.")
else:
    print("Mayúscula¿?")