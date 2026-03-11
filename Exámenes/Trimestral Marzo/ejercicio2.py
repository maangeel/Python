#input cadena de texto
cadena = input("Introduce una cadena de texto: ").split(" ")

print(cadena)

palabraEscogida = input("Introduce la palabra que quieres buscar: ")

#contar palabras
print(f'La palabra "{palabraEscogida}" aparece {cadena.count(palabraEscogida)} veces')

#unir la lista
listaUnida = ", ".join(cadena)
print(listaUnida)