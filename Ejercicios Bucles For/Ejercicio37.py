#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

rep = input("Introduce el número de notas que deseas introducir: ")

if rep.isdigit: #comprueba si el valor es entero
    rep = int(rep)
    for i in range(rep): #hace tantas repeticiones como el usuario pida
        nota = float(input("Introduce tu nota sobre 10: "))

        if nota>=5 and nota<=10:
            print("Asignatura aprobada")
        elif nota<5 and nota>=0:
            print("Asignatura suspendida")
        else: #en caso de no estar entre 0 y 10 salta error
            print("Error")

else: #en caso de no ser entero printea error
    print("Error")