#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra.

#input palabra secreta
secret = input("Introduce la palabra secreta: ")

for i in range(len(secret)): #repite tantas veces como longitud de la palabra
    letra=input("Introduce una letra: ")
    if letra in secret: #si la letra aparece en la palabra
        print("La letra existe.")
    else:
        print("La letra no existe: ")