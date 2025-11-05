#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

rep = input("Introduce el número de notas que deseas introducir: ")

if rep.isdigit: #comprueba si el valor es entero
    rep = int(rep)



else: #en caso de no serlo printea error
    print("Error")