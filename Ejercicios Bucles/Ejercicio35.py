#35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre

name = input("Introduce tu nombre: ")
num = int(input("Introduce el número de repeticiones: "))

for i in range(num): #bucle que hace tantas repeticiones como la variable num diga
    print(name)