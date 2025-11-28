#variables
valor = 100

numero = int(input("Introduce un número: "))
if numero%2==0:
    valor/=2
else:
    valor+=numero
if numero%3==0:
    valor-=5
print(valor)

while (numero>=0) and (valor>=50) and (valor<=150): #si no se incumplen las condiciones el bucle continúa
    numero = int(input("Introduce un número: "))
    if numero%2==0:
        valor/=2
    else:
        valor+=numero
    if numero%3==0:
        valor-=5
    print(valor)