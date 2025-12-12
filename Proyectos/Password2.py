#verión 2 del password. Con bucles for. Requisitos: tener 3 letras, 3 números y 2 símbolos. 3 entradas de password

print("INSTRUCCIONES")
print("1. La longitud del password tiene que tener 8 caracteres")
print("2. Debe contener 3 letras, 3 números y 2 símbolos")

#inicialización de variables
correctPassword = 0
incorrectPassword = 0

letras = 0  
num = 0
simbol = 0

#3 inputs almacenados en una lista
password=[input("Introduce password 1: "),input("Introduce password 2: "),input("Introduce password 3: ")]

for i in password: #asigna a i cada password
    letras = 0 #reseteo variables
    num = 0
    simbol = 0
    if len(i) == 8: #comprueba la longitud
        for j in range(8):
            if i[j].isalpha(): #caracter string
                letras += 1
            elif i[j].isdigit(): #caracter numérico
                num += 1
            else: #resto de carácteres
                simbol += 1
    else: #en caso de longitud incorrecta
        print("Longitud incorrecta")
    if letras == 3 and num == 3 and simbol == 2: #comprueba requisitos
        correctPassword+=1
        print(f'El Password "{i}" cumple con los requisitos.')
    else:
        incorrectPassword+=1
        print(f'El Password "{i}" no cumple con los requisitos.')

#salida de datos
print(f"Has introducido {correctPassword} Passwords correctas y {incorrectPassword} Password incorrectas.")