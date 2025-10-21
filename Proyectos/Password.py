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

#condiciones para garantizar que la contraseña sea correcta

if password.len >= 6 and password.len <= 8:

else:
    print("ERROR")
    print("La longitud del password no es el indicado.")
    print("Cerrando programa...")