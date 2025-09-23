#18. Cines Paradiso celebran su décimo aniversario y por ser un día
#especial realizan importantes descuentos. A los adultos se les aplicará
#un 10% de descuento y a los menores de 18 años un 50%. Si la entrada
#cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.

minors = int(input("Introduce el número de menores que hay: "))
adults = int(input("Introduce el número de adultos que hay: "))

minorsPrice = 12*0.5*minors
adultsPrice = 12*0.9*adults
minorsPrice = round(minorsPrice,1)
adultsPrice = round(adultsPrice,1)

print(f"El precio total del cine para {minors} menor/es es: {minorsPrice}")
print(f"El precio total del cine para {adults} adulto/s es: {adultsPrice}")