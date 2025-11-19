#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural... Con While

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

print("Fin del programa...")