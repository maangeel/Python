valores = input("Introduce una lista de números separados por guiones: ").split("-")

valoresNumericos = [x for x in valores if not x.isalpha()]

listaNoNumeros = []
listaNumeros = []

#clasificar en numéricos y no numéricos
for valor in valoresNumericos:
    try:
        listaNumeros.append(int(valor)) #intenta convertir a int
    except ValueError:
        listaNumeros.append(float(valor)) #intenta convertir a float

listaNoNumeros = [valor for valor in valores if valor.isalpha()]

#suma números
sumaNum = sum(listaNumeros)

#conversión a mayúsculas y orden alfabético
listaNoNumerosMayus = sorted([valor.upper() for valor in listaNoNumeros])

#eliminar duplicados
listaNoNumerosNoDuplicados = list(set(listaNoNumerosMayus))
listaNumerosNoDuplicados = sorted(list(set(listaNumeros)))

sumaTotalNoDuplicados = sum(listaNumerosNoDuplicados)


#prints
print("\nValores numéricos antes de eliminar duplicados:", listaNumeros)
print("\nSuma total antes de eliminar duplicados:", sumaNum)
print("\nValores numéricos después de eliminar duplicados:", listaNumerosNoDuplicados)
print("\nSuma total después de eliminar duplicados:", sumaTotalNoDuplicados)
print("\nValores no numéricos antes de eliminar duplicados:", listaNoNumeros)
print("\nValores no numéricos después de eliminar duplicados:", listaNoNumerosNoDuplicados)