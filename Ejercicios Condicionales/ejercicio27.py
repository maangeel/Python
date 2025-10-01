#27. Mejora el programa anterior para controlar que el valor introducido
#es una letra y en caso de introducir un número, aparezca un aviso
#por pantalla.

letra = input("Introduce una letra: ")
if letra.isdigit(): #comprueba si es un dígito
    print("El valor introducido es un número.")
if letra.isalpha(): #comrpueba si es una letra
    if letra.isupper(): #comprueba si es mayúsculas
        print("La letra es mayúscula.")
    if not letra.isupper():
        print("La letra es minúscula.")
if not letra.isdigit() and not letra.isalpha():
    print("Mayúscula¿?")