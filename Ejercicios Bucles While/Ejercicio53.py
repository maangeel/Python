#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While

respuesta = "s" #inicializando variable respuesta será s/n
rep = 1 #variable repeticiones
resultTotal = 0 #variable que almacena el resultado final

while respuesta == "s":
    num1 = int(input("Introduce un valor entero: "))
    num2 = int(input("Introduce otro valor entero: "))
    result = num1+num2
    print(f"El resultado de la suma es: {result}.")
    respuesta = input("Deseas repetir la operación s/n: ")
    rep+=1 #añade una repetición
    resultTotal+=result #suma el resultado al total

print("Resumen:") #salida de datos
print(f"La suma total es: {resultTotal} y el número de repeticiones es: {rep}.")