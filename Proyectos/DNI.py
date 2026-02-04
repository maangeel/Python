lista_intentos = [] #intentos de DNI
repetir = "s" #comprueba repetición
dniLetterValue = 0 #valor numérico de la letra
lista_Letras = "T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E" #recoge las letras
lista_Letras = lista_Letras.split(",") #letras en lista
DNI_Completo = "" #DNI final
DNI_Correcto = [] #almacena los DNI correctos
DNI_Incorrecto = [] #almacena los DNI incorrectos
dniNumber = 0 #número de DNI

while repetir.lower() == "s":

    #-----REPETICIÓN-----
    if lista_intentos: #comprueba si ya se ha introducido algún dni
        repetir = input("¿Quieres introducir otro DNI? s/n: ")
    if repetir.lower() == "n":
        continue #vuelve al bucle y comprueba de nuevo la condición
    
    #-----INPUTS-----
    #COMPROBADOR-NUMÉRICO
    while True:
        try:
            dniNumber = int(input("Introduce tu DNI: "))
            break
        except ValueError:
            print("El valor no es numérico")
            lista_intentos.append(1) #DNI no numérico
            DNI_Incorrecto.append(DNI_Completo) #añade a lista de incorrectos
            continue #repite el bucle

    #-----COMPROBADOR-LONGITUD-----
    if len(str(dniNumber)) != 8:
        print("El valor no tiene la longitud correcta")
        lista_intentos.append(0) #DNI longitud incorrecta
        DNI_Incorrecto.append(DNI_Completo) #añade a lista de incorrectos
        continue

    #-----CÁLCULO-DE-LA-LETRA-----
    dniLetterValue = dniNumber%23
    if dniLetterValue>=0 and dniLetterValue<=22:
        DNI_Completo = dniNumber+"-"+lista_Letras[dniLetterValue] #completa el DNI con la letra
        lista_intentos.append(3) #DNI correcto
        DNI_Correcto.append(DNI_Completo) #añade a lista de correctos
    else:
        print("El DNI no existe")
        lista_intentos.append(2) #DNI inexistente
        DNI_Incorrecto.append(DNI_Completo) #añade a lista de incorrectos
        continue

#------------------------------------MENÚ-SELECCIÓN------------------------------------

print("\nRESULTADOS")
print("ESCOGE UNA OPCIÓN")

print("\n1. Listar DNI correcto ordenado de menor a mayor")
print("2. Listar DNI incorrecto ordenado de menor a mayor")
print("3. Número total de errores producidos")
print("4. Número total de DNI correctos")
print("5. Porcentaje de intentos con error y sin error")
print("6. Salir s/n")

opcionesMenu = 0

#-----ESCOGER-OPCIÓN-----
while True:
    try:
        opcionesMenu = int(input("Introduce la opción: "))
        if not opcionesMenu>=1 or not opcionesMenu<=6:
            print("ERROR; Introduzca una opción posible")
            continue
        else:
            break
    except ValueError:
        print("ERROR; Introduzca una opción posible")

#-----CÓDIGO-DE-OPCIONES-----
if opcionesMenu == 1: #CORRECTOS ORDENAR MENOR A MAYOR
    DNI_Correcto.sort()
    print(DNI_Correcto)

if opcionesMenu == 2: #INCORRECTOS ORDENAR MENOR A MAYOR
    DNI_Incorrecto.sort()
    print(DNI_Incorrecto)

if opcionesMenu == 3: #TOTAL ERRORES
    print(len(DNI_Incorrecto))

if opcionesMenu == 4: #TOTAL CORRECTOS
    print(len(DNI_Correcto))

if opcionesMenu == 5: #PORCENTAJE ERRORES
    print("El número de intentos es:",len(lista_intentos))
    percCorrectos = len(DNI_Correcto)/len(lista_intentos)*100 #porcentaje correctos
    perIncorrectos = len(DNI_Incorrecto)/len(lista_intentos)*100 #porcentaje incorrectos
    
    #PORCENTAJE ERROR DE LONGITUD
    repeticionesLong = lista_intentos.count(0)
    percLongitud = repeticionesLong/lista_intentos*100

    #PORCENTAJE ERROR DE DÍGITOS
    repeticionesDigit = lista_intentos.count(1)
    percDigit = repeticionesDigit/lista_intentos*100

    #PORCENTAJE DNI INEXISTENTES
    repeticionesInex = lista_intentos.count(2)
    percInex = repeticionesInex/lista_intentos*100

    #PRINTS
    print("El '%' de DNI correctos es:",percCorrectos)
    print("El '%' de DNI incorrectos es:",perIncorrectos)
    print("El '%' de DNI con error de longitud es:",percLongitud)
    print("El '%' de DNI con error de dígitos es:",percDigit)
    print("El '%' de DNI que no existen es:",percInex)