#26. Realiza un programa que, al introducir una letra por teclado,
#aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s
#que establezcan True o False a la condición.

#inputs
letra = input("Introduce una letra: ")

if letra.isalpha():
    if letra.isupper():
        print("La letra es mayúscula")
    if not letra.isupper():
        print("La letra es minúscula")
else:
    print("Mayúscula¿?")