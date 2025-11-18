#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10

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
            print("Has introducido una nota equivocada")

else: #en caso de no ser entero printea error
    print("Error")