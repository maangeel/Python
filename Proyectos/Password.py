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

totalError = 0
error1 = False #inicialización variables 
error2 = False #inicialización variables
error3 = False #inicialización variables
error4 = False #inicialización variables
error5 = False #inicialización variables
error6 = False #inicialización variables
error7 = False #inicialización variables
error8 = False #inicialización variables

correct = 1 #variable para comprobar que la contraseña es correcta
#condiciones para garantizar que la contraseña sea correcta

if len(password) >= 6 and len(password) <= 8:
    if int(password[0]) >= 1 and int(password[0]) <= 5: #verifica primera pos
        correct += correct
    else:
        error1 = True


    if password[1].islower: #segunda pos
        correct += correct
    else:
        error2 = True


    if password[2].isupper: #tercera pos
        correct += correct
    else:
        error3 =True


    if password[3] in "*" or password[3] in "*" or password[3] in "*": #cuarta pos
        correct += correct
    else:
        error4 = True


    if password[4].islower:
        correct += correct
    else:
        error5 = True


    if int(password[5]) >= 6 and int(password[5]) <= 9:
        correct += correct
    else:
        error6 = True


    if password[6] in "&" or password[6] in "/" or password[3] in "#":
        correct += correct
    else:
        error7 = True
        

    if int(password[7]) <= 5:
        correct += correct
    else:
        error8 = True


else:
    print(f"ERROR, el PASSWORD tiene una longitud de {len(password)} caracteres y no cumple los requisitos")

#condiciones para comprobar el número de errores
if 