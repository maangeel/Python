#programa menú de gasolinera

#diseño del menú
print("*********GASOLINERA**********")
print("*1. | Sin plomo 95  | 1.765€*")
print("*2. | Sin plomo 98  | 1.913€*")
print("*3. | Gasóleo A     | 1.746€*")
print("*4. | Gasóleo A+    | 1.839€*")
print("*****************************")

#inputs
tipo = int(input("Escoja el tipo de combustible: "))

litros = float(input("Introduzca el número de litros a repostar: "))

#condicionales según la opción escogida
if tipo == 1:
    total = round((litros * 1.765),2) #los round aparecido son para redondear el resultado a 2 decimales
    print(f"El total a pagar es: {total}€")
elif tipo == 2:
    total = round((litros * 1.913),2)
    discount = round((total - total * 0.1),2)
    print(f"El total a pagar es {total}€ y con el descuento queda en {discount}€.")
elif tipo == 3:
    total = round((litros * 1.746),2)
    print(f"El total a pagar es: {total}€")
elif tipo == 4:
    total = round((litros * 1.839),2)
    discount = round((total - total * 0.12),2)
    print(f"El total a pagar es {total}€ y con el descuento queda en {discount}€.")
else:
    print("Error, elija una opción entre el 1 y el 4.") #salida de error en caso de no escoger una de las opciones