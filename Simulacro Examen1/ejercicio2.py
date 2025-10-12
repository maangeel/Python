#programa que pida una frase y 3 números reales. Quite espacios iniciales y finales y en minúsculas. Suma, media 2 decimales y producto. Mensaje que indique si la suma es mayor que el producto o no.

frase = input("Introduce una frase: ")
num1 = float(input("Introduce un número real: "))
num2 = float(input("Introduce otro número real: "))
num3 = float(input("Introduce otro número real: "))

frase = frase.strip() #quita espacios iniciales y finales
frase = frase.lower() #minúsculas

suma = num1 + num2 + num3
media = round(suma/3,2) #hace la media y redondea a dos decimales
producto = num1 * num2 * num3

print(f"Frase en minúsculas: {frase}")
print(f"La suma es: {suma}")
print(f"La media es: {media}")
print(f"El producto es: {producto}")


if suma > producto:
    print("¿La suma es mayor que el producto?",True)
else:
    print("¿La suma es mayor que el producto?",False)