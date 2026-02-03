lista_intentos = []
repetir = "s"
dniLetterValue = 0
lista_Letras = "T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E"
lista_Letras = lista_Letras.split(",")
DNI_Completo = ""

while repetir.lower() == "s":

    if lista_intentos: #comprueba si ya se ha introducido algún dni
        repetir = input("¿Quieres introducir otro DNI? s/n: ")
    if repetir.lower() == "n":
        continue
    #-----INPUTS-----

    #COMPROBADOR NUMÉRICO
    while True:
        try:
            dniNumber = int(input("Introduce tu DNI: "))
            break
        except ValueError:
            print("El valor no es numérico")
            lista_intentos.append(1)
            continue #repite el bucle

    #-----COMPROBADOR LONGITUD-----
    if len(str(dniNumber)) != 8:
        print("El valor no tiene la longitud correcta")
        lista_intentos.append(0)
        continue

    #-----CÁLCULO DE LA LETRA-----
    dniLetterValue = dniNumber%23
    if dniLetterValue>=0 and dniLetterValue<=22:
        DNI_Completo = dniNumber+lista_Letras[dniLetterValue]
    else:
        print("El DNI no existe")
        lista_intentos.append(2)
        continue