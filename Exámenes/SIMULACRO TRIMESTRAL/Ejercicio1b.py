#input de dos números
inicio = int(input("Introduce un valor entero para inicio: "))
final = int(input("Introduce otro valor entero para final: "))

increment = int(input("Introduce el incremento: ")) #incremento valores
valores = ""

for i in range(inicio,final,increment): #recorre valores
    if not i%4==0:
        if i%6==0:
            valores = valores + "*" + str(i) + "*" ","
        else:
            valores = valores + str(i) + ","

print(valores[:-1])