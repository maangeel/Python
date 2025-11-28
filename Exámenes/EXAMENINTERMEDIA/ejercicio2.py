#mejora del código anterior añadiendo división y redondeo

var1 = float(input("Introduce el primer número: ")) #entrada de datos
var2 = float(input("Introduce el segundo número: ")) #entrada de datos

suma = var1 + var2 #suma de ambos números
div = round((suma / 3),3) #división de la suma entre 3 y redondeo a 3 decimales

print(f"El resultado de sumar {var1} y {var2} es:", suma) #salida de datos con uso de {} y comas
print(f"El resultado de dividir {suma} entre 3 es:", div) #salida de datos 2