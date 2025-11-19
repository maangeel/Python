#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

numOperaciones = 1 #variable que controla número de operaciones
resultTotal = 0 #variable que almacena el resultado final

num1 = int(input("Introduce un valor entero: ")) #primera suma
num2 = int(input("Introduce otro valor entero: "))
result = num1+num2
resultTotal+=result
#primer print
print(f"El resultado de la suma es: {result}.")
print(f"El total acumulado es: {resultTotal} y llevas {numOperaciones} operación.")

while resultTotal < 50: 
    num1 = int(input("Introduce un valor entero: "))
    num2 = int(input("Introduce otro valor entero: "))
    result = num1+num2
    numOperaciones+=1 #añade una repetición
    resultTotal+=result #suma el resultado al total
    print(f"El resultado de la suma es: {result}.")
    print(f"El total acumulado es: {resultTotal} y llevas {numOperaciones} operaciones.")

while resultTotal%2 == 0: #una vez el valor es mayor a 50 hasta que no sea impar no interrumpe el programa
    num1 = int(input("Introduce un valor entero: "))
    num2 = int(input("Introduce otro valor entero: "))
    result = num1+num2
    numOperaciones+=1 #añade una repetición
    resultTotal+=result #suma el resultado al total
    print(f"El resultado de la suma es: {result}.")
    print(f"El total acumulado es: {resultTotal} y llevas {numOperaciones} operaciones.")

print("Fin del programa...")