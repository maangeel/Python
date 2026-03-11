valores = input("Ingresa los valores separados por guiones: ").split("-")

valores = [int(x) for x in valores] #Convierte los valores a enteros

valMax = max(valores)
valMin = min(valores)

media = round(sum(map(float, valores)) / len(valores), 4) #Vuelve a float los valores y calcula la media

nuevaLista = [int(x) for x in valores if int(x) > media] #Crea nueva lista con valores mayores a la media


#PRINTS
print(f"Máximo: {valMax}")
print(f"Mínimo: {valMin}")
print(f"Promedio: {media}")
print(f"Nueva lista: {nuevaLista}")