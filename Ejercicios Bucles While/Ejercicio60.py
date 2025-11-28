#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while

valor = int(input("Introduce el valor que quieres multiplicar: "))
tabla = 0
while tabla<10:#bucle con incremento
    tabla+=1
    print(valor*tabla)