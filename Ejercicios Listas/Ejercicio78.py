#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir

lista1 = ['a','b','D','x','r','X','3','h','w','2','i']

#variable bucle
continuar = "s"

while continuar in "Ss" and not continuar in "Nn":
    valorEliminar = input("Introduce el valor que deseas eliminar: ")
    if valorEliminar.isdigit(): #comprueba si es numérico
        if valorEliminar in lista1:
            lista1.remove(valorEliminar) #elimina el valor de la lista
            print(lista1)
        else:
            print("El valor introducido no está en la lista")
    else:
        print("Introduce valor numérico")
    
    continuar = input("Deseas introducir otro valor s/n: ")
