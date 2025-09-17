#2. Programa que introduzca por teclado tres tipos de variables 
#y se muestren por pantalla
#en el siguiente orden: número entero, texto y número decimal.

#entrada de número int
varInt = int(input("Introduce un valor entero: "))

#entrada de texto
varStr = input("Introduce una letra: ")

#entrada de decimal
varFloat = float(input("Introduce un valor decimal: "))

#muestra por consola las variables
print("El valor entero introducido es", varInt)
print(f"La letra introducida es: {varStr}")
print(f"El número decimal introducido es: {varFloat}")