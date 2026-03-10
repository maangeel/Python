passwords = input("Ingrese contraseñas separadas por guiones: ")

passwordsList = [password for password in passwords.split("-")] #crea lista de contraseñas separadas

#CATEGORÍAS: Segura, débil, inválida
segura = []
debil = []
invalida = []

#clasificación de contraseñas
for password in passwordsList:
    if any(char.invalid for char in password):
        not password.replace("-", "").replace("_", "").isalnum()
        invalida.append(password)
    elif len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        debil.append(password)
    elif len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        segura.append(password)