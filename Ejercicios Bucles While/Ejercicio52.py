#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While

res = "s" #inicializando variable respuesta será s/n

while res == "s":
    num1 = int(input("Introduce un valor entero: "))
    num2 = int(input("Introduce otro valor entero: "))
    result = num1+num2
    print(f"El resultado de la suma es: {result}.")
    res = input("Deseas repetir la operación s/n: ")

print("Cerrando...")