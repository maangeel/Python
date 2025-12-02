#56. Realiza un programa que gestione un establecimiento de venta de bocadillos... con listas que se mueva
#por los índices.

print("MENÚ")
print("1. Bocadillo de calamares - 9€")
print("2. Bocadillo de chistorria - 4.5€")
print("3. Bikini de jamón - 2.5€")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5€")
print("2. Patatas gruesas - 1.75€")
print("3. Patatas rústicas - 2€")
print("BEBIDAS")
print("1. Coca cola - 2€")
print("2. Acuarius - 1.5€")
print("3. Agua - 1€")

total = 0 #suma de precios
totalIva = 0 #añadiendo IVA 10%
totalDisc = 0 #descuento del 5% si es 20-30€ y 15% si es > 30€
principal = 0
acompa = 0
bebida = 0
otroPedido = "s" #s/n
numPedidos = 0 #almacena número de pedidos

#inputs
while otroPedido == "s":
    numPedidos+=1
    principalSN = input("¿Quieres pedir un plato principal? s/n: ")
    if principalSN in "sS":
        principal = int(input("Introduce el número de tu plato principal: "))
    acompa = int(input("Introduce el número de tu acompañamiento: "))
    bebida = int(input("Introduce el número de tu bebida: "))
    if principal == 1:
        total+=9
    if principal == 2:
        total+=4.5
    if principal == 3:
        total+=2.5
    if acompa == 1:
        total+=1.5
    if acompa == 2:
        total+=1.75
    if acompa == 3:
        total+=2
    if bebida == 1:
        total+=2
    if bebida == 2:
        total+=1.5
    if bebida == 3:
        total+=1
    otroPedido = input("¿Quieres realizar otro pedido? s/n: ")
    while not otroPedido == "s" and not otroPedido == "n":
        otroPedido = input("¿Quieres realizar otro pedido? s/n: ")

totalIva = total*1.1
if totalIva > 30:
    totalDisc=totalIva*0.85
    print(f"Número de pedidos: {numPedidos}")
    print(f"Total a pagar: {round(total,2)}€")
    print(f"Total + IVA: {round(totalIva,2)}€")
    print(f"Total con descuento del 15%: {round(totalDisc,2)}€")
elif totalIva <= 30 and totalIva >= 20:
    totalDisc=totalIva*0.95
    print(f"Número de pedidos: {numPedidos}")
    print(f"Total a pagar: {round(total,2)}€")
    print(f"Total + IVA: {round(totalIva,2)}€")
    print(f"Total con descuento del 5%: {round(totalDisc,2)}€")
else:
    totalDisc=totalIva
    print(f"Número de pedidos: {numPedidos}")
    print(f"Total a pagar: {round(total,2)}€")
    print(f"Total + IVA: {round(totalIva,2)}€")