num = int(input())

suma = 0
posibilidades = 0
guardado = 0
guardado2 = 0

secuenceNum = 1,2,3,4,6,8,11,13,16,18,26,28,36,38,47

secuencia = ""

for i in range(num-1):
    for j in range(num-1):
        if i in secuenceNum and j in secuenceNum:
            suma=j+i
            if suma == num:
                posibilidades+=1
                guardado = j
                guardado2 = i
                secuencia = str(i),"+",str(j)
    if i == guardado and j==guardado2:
        break
        

if num == 1 or num == 2:
    print(f"{num} is in sequence (starter)")

elif posibilidades == 1:
    print(f"{num} is in sequence: {secuencia}")

else:
    print(f"{num} is not in sequence")