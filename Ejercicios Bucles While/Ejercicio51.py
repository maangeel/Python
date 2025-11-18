#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While

rep = int(input("Introduce el número de repeticiones: "))
i = 0
while i!=rep: #repetición hasta que i valga intent
    print("Buenos días")
    i+=1