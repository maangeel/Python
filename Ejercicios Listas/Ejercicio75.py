#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos

#creación de la lista

lista1 = ['a','b','D','x','r','X','3','h','w','2','i']

#CANTIDAD TOTAL DE VALORES
totalValores = len(lista1)

#CANTIDAD DE NÚMEROS
totalNum = sum(1 for parte in lista1 if parte.isdigit())

#CANTIDAD DE LETRAS
totalLetras = sum(1 for parte in lista1 if parte.isalpha())

#CANTIDAD DE MAYÚSCULAS
totalMayus = sum(1 for parte in lista1 if parte.isupper())

#SUMA DE LOS VALORES NUMÉRICOS
sumaNum = sum(int(parte) for parte in lista1 if parte.isdigit())

print("Número de valores:",totalValores)
print("Cantidad de números:",totalNum)
print("Cantidad de letras:",totalLetras)
print("Número de mayúsculas:",totalMayus)
print("Suma total de números:",sumaNum)