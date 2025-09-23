#17. Calcula el índice de masa corporal IMC de una persona, introduciendo
#por teclado el peso (en kg) y dividiendo por la estatura (en metros
#y elevado al cuadrado). Si el resultado es igual o superior a 25,
#debe aparecer un mensaje informando de sobrepeso.

#inputs
masa = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en m: "))

#cálculos
imc = masa / estatura**2
imc = round(imc,2)

if (imc >= 25):
    print(f"Si pesas {masa} kg y mides {estatura} m, tienes sobrepeso.")
    print(f"Tu IMC es {imc}.")

else:
    print(f"Si pesas {masa} kg y mides {estatura} m, tu IMC es {imc}.")