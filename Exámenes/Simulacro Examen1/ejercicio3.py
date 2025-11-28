#programa calcule volumen de un cilindro pidiendo radio y altura. Formato en mayus o minus segun lo que pida el user.
import math

radio = float(input("Introduce el radio: "))
altura = float(input("Introduce la altura: "))
formato = input("¿Quieres la salida en mayúsculas o minúsculas? ")

formato = formato.lower() #paso a minusculas para evitar bugs

printText = "El volumen del cilindro es:" #el texto del print en variable

vol = math.pi * radio**2 * altura
vol = round(vol,3) #redondeo

if formato == "mayusculas" or formato == "mayúsculas":
    print(printText.upper(),vol) #pasa el print a mayus
elif formato == "minusculas" or formato == "minúsculas":
    print(printText.lower(),vol) #pasa el print a minus
else:
    print("ERROR, asegúrate de haber escrito correctamente el formato.")