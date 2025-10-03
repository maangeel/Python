#34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se
#ejecute correctamente.

#inicializo valores a cada variable
var_numero=6734
var_suma=0

numeroStr = str(var_numero) #convierto a string

#obtengo su longitud
var_longitud=len(numeroStr) #mide la longitud del string

#sumo cada digito a partir del índice de cada posición
for i in range(var_longitud):
    var_suma += int(numeroStr[i])
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
if var_suma % 2 == 0:
    print (f"el valor de {var_suma} es par.")
else:
    print (f"el valor de {var_suma} es impar.")