#for i in range(1,10,3): #asigna a i un valor que comienza en 1 y acaba en 10. El tercer valor suma al primero y es opcional
#    print(i)
#for i in range(1,999):
#    print(i)
#for i in "banana":
#    print(i)
#for i in range(10): #tmb sirve para hacer repeticiones
#    print("Repito")
#n=0
#while n < 10: #bucle con una condición
#    print("klk")
#    n += 1

#while True: #bucle infinito
#    print("Hola")

totalV = 0 #para la suma de vocales
sumaNum = 0 #para la suma de num
password = "a7e4jk"

for i in password:
    if i.lower() in "aeiou":
        totalV += 1
    if i.isdigit():
        sumaNum = int(sumaNum)
        sumaNum += int(i)

print(f"Hay {totalV} vocales y la suma total es {sumaNum}.")