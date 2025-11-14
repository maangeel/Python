#verión 2 del password. Con bucles for. Requisitos: tener 3 letras, 3 números y 2 símbolos. 3 entradas de password

print("INSTRUCCIONES")
print("1. La longitud del password tiene que tener 8 caracteres")
print("2. Debe contener 3 letras, 3 números y 2 símbolos")


letras = 0
num = 0
simbol = 0

#3 inputs almacenados en una lista
password=[input("Introduce password 1: "),input("Introduce password 2: "),input("Introduce password 3: ")]

for i in password: #asigna a i cada password
    if len(i) == 8:
        for j in range(8):
            if password[j].isalpha():
                letras += 1
            elif password[j].isdigit():
                num += 1
            else:
                simbol += 1
    else:
        print("Longitud incorrecta")