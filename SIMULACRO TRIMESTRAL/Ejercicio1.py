#input de dos números
inicio = int(input("Introduce un valor entero para inicio: "))
final = int(input("Introduce otro valor entero para final: "))

increment = int(input("Introduce el incremento: ")) #incremento valores

for i in range(inicio,final,increment): #recorre valores
    if i==inicio:
        if not i%4==0:
            if i%6==0:
                print(f"*{i}*",end="")
            else:
                print(i,end="")
    else:
        if not i%4==0:
            if i%6==0:
                print(f",*{i}*",end="")
            else:
                print(f",{i}",end="")
