import string

passwords = input("Ingrese contraseñas separadas por guiones: ")

passwordsList = [password for password in passwords.split("-")] #crea lista de contraseñas separadas

#CATEGORÍAS: Segura, débil, inválida
segura = []
debil = []
invalida = []

caracterValidos = string.ascii_letters + string.digits + string.punctuation

#clasificación de contraseñas
for password in passwordsList:
    if any(char not in caracterValidos for char in password): #inválida
        invalida.append(password)
    elif len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password): #débil
        debil.append(password)
    elif len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password): #segura
        segura.append(password)

print("Contraseñas seguras:", ", ".join(segura))
print("Contraseñas débiles:", ", ".join(debil))
print("Contraseñas inválidas:", ", ".join(invalida))
print("Contraseña más larga:", max(passwordsList, key=len))