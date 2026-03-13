#lista con cartas del 7 y medio
listaCartas = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12]

#valor de las cartas
valoresCartas = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,0.5,0.5,0.5,0.5]

#función para obtener una carta y su valor
def obtenerCarta():
    respuesta = input("¿Quieres una carta? (s/n): ")
    if respuesta == "s":
        import random
        numeroCarta = random.randint(0,39)
        return listaCartas[numeroCarta], valoresCartas[numeroCarta]
    while respuesta != "s" and respuesta != "n":
        print("Por favor, ingresa 's' o 'n'.")
        respuesta = input("¿Quieres una carta? (s/n): ")
        
    else:
        return 0,0

print("Bienvenido al juego de 7 y Medio")

while obtenerCarta() != (0,0):
    carta, valor = obtenerCarta()
    print(f"Has obtenido la carta {carta} con valor {valor}")