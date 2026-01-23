#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor

rep = int(input("Introduce el número de repeticiones: "))
listaValores = []

for i in range(rep): #bucle repeticiones
    valor = int(input("Introduce un valor: "))
    listaValores.append(valor)

listaValores.sort() #ordena de menor a mayor

print(listaValores)