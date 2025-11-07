#42. Imprima el siguiente patrón con el ciclo for:

for i in range(0,5):
    for j in range(i):
        print("*", end="")
    print("")
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print("")