#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir

lista1 = ['a','b','D','x','r','X','3','h','w','2','i']

valorEliminar = input("Introduce el valor que deseas eliminar: ")

#variable bucle
continuar = "s"

while continuar in "Ss" and not continuar in "Nn":
    if valorEliminar.isdigit():
        if valorEliminar in lista1:
