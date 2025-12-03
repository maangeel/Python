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

#precios
principal = [9,4.5,2.5]
acompa = [1.5,1.75,2]
bebida = [2,1.5,1]

numPlato = 0
otroPedido = "s" #s/n
numPedidos = 0 #almacena número de pedidos

#inputs
while otroPedido == "s":
    numPedidos+=1
    
    #plato principal
    principalSN = input("¿Quieres pedir un plato principal? s/n: ")
    while not principalSN in "sSnN":
        print("ERROR")
        principalSN = input("¿Quieres pedir un plato principal? s/n: ")
    if principalSN in "sS":
        numPlato = int(input("Introduce el número de tu plato principal: "))
        while not numPlato<=3 or not numPlato>=1:
            print("ERROR")
            numPlato = int(input("Introduce el número de tu plato principal: "))
        total+=principal[numPlato-1]
    
    #acompañamiento
    acompaSN = input("¿Quieres pedir un acompañamiento? s/n: ")
    while not acompaSN in "sSnN":
        print("ERROR")
        acompaSN = input("¿Quieres pedir un acompañamiento? s/n: ")
    if acompaSN in "sS":
        numPlato = int(input("Introduce el número de tu acompañamiento: "))
        while not numPlato<=3 or not numPlato>=1:
            print("ERROR")
            numPlato = int(input("Introduce el número de tu acompañamiento: "))
        total+=acompa[numPlato-1]

    #bebida
    bebidaSN = input("¿Quieres pedir una bebida? s/n: ")
    while not bebidaSN in "sSnN":
        print("ERROR")
        bebidaSN = input("¿Quieres pedir una bebida? s/n: ")
    if bebidaSN in "sS":
        numPlato = int(input("Introduce el número de tu bebida: "))
        while not numPlato<=3 or not numPlato>=1:
            print("ERROR")
            numPlato = int(input("Introduce el número de tu bebida: "))
        total+=bebida[numPlato-1]

    #otro pedido
    otroPedido = input("¿Quieres realizar otro pedido? s/n: ")
    while not otroPedido in "sSnN":
        print("ERROR")
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