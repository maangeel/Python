#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

#input palabra secreta
secret = input("Introduce la palabra secreta: ")

for i in range(len(secret)):
    letra=input("Introduce una letra: ")
    if letra in secret:
        for j in range(len(secret)): #recorre del 0 a la longitud de la palabra secreta
            if letra in secret[j]: #si la letra está en la posición 0,1,2,3...
                print(f"La letra se encuentra en la posición {j+1}") #muestra en qué posición está
            
    else:
        print("La letra no existe: ")