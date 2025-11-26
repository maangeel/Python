#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while

valor = int(input("Introduce el valor que quieres multiplicar: "))
tabla = 1
while tabla<11:
    print(valor*tabla)
    tabla+=1