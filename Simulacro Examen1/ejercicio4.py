#menú de tarifas

#menú visual
print("Opción | Tarifa           | Precio €/kWh | Descuento")
print("1      | Tarifa Nocturna  | 0.158        | 5%")
print("2      | Tarifa Plana     | 0.192        | 0%")
print("3      | Tarifa Solar     | 0.143        | 8%")
print("4      | Tarifa Ecológica | 0.170        | 10%")

opcion = int(input("Introduce el número de la opción: "))
kWh = int(input("Introduce los kWh: "))

if not opcion < 1 and not opcion > 4: #está entre el 1 y el 4
    if opcion == 1:
        precio = round((0.158 * kWh),2)
        precioDiscount = round((precio - precio*0.05),2)
        print(f"El total a pagar es: {precio} €")
        print(f"Con el descuento aplicado queda en: {precioDiscount} €")
    
    elif opcion == 2:
        precio = round((0.192 * kWh),2)
        print(f"El total a pagar es: {precio} €")

    elif opcion == 3:
        precio = round((0.143 * kWh),2)
        precioDiscount = round((precio - precio*0.08),2)
        print(f"El total a pagar es: {precio} €")
        print(f"Con el descuento aplicado queda en: {precioDiscount} €")
    else:
        precio = round((0.170 * kWh),2)
        precioDiscount = round((precio - precio*0.1),2)
        print(f"El total a pagar es: {precio} €")
        print(f"Con el descuento aplicado queda en: {precioDiscount} €")
else:
    print("ERROR, asegúrate de haber introducido correctamente la opción.")