#programa de la contraseña

#print con las instrucciones

print("INSTRUCCIONES")
print("1. La longitud del password tiene que tener entre 6 y 8 caracteres")
print("2. Forzar los siguientes valores según la posición indicada:")
print("      Posición 1 Un número mayor o igual a 1 y menor o igual a 5")
print("      Posición 2 Una letra minúscula")
print("      Posición 3 Una letra mayúscula")
print("      Posición 4 Un de los siguientes símbolos *, _, @")
print("      Posición 5 Una letra minúscula")
print("      Posición 6 Un número mayor or igual a 6 y menor o igual a 9")
print("      Posición 7 Uno de los siguientes símbolos &, /, #")
print("      Posición 8 Un número menor o igual a 5")

#entrada de la contraseña
password = input("Introuce el password: ")

if len(password) >= 6 and len(password) <= 8:
    isError = False
    errores = []

    if not (password[0].isdigit() and int(password[0]) >= 1 and int(password[0]) <= 5): #verifica primera pos
        errores.append("Error en el caracter 1")
        isError = True

    if not password[1].islower(): #segunda pos
        errores.append("Error en el caracter 2")
        isError = True

    if not password[2].isupper(): #tercera pos
        errores.append("Error en el caracter 3")
        isError = True

    if not password[3] in "*_@": #cuarta pos
        errores.append("Error en el caracter 4")
        isError = True

    if not (password[4].islower()):
        errores.append("Error en el caracter 5")
        isError = True

    if not (password[5].isdigit() and int(password[5]) >= 6 and int(password[5]) <= 9):
        errores.append("Error en el caracter 6")
        isError = True

    if len(password) == 7:
        if not password[6] in "&#/":
            errores.append("Error en el caracter 7")
            isError = True
    if len(password) == 8:    
        if not password[7].isdigit() or not int(password[7]) <= 5:
            errores.append("Error en el caracter 8")
            isError = True
    
    if isError:
        print(errores)
    else:
        print("El formato del PASSWORD es correcto")

else:
    print(f"ERROR, el PASSWORD tiene una longitud de {len(password)} caracteres y no cumple los requisitos")