lista = input().split()

peaks = 0

for i in range(len(lista)-2):

    if int(lista[i+1])>int(lista[i]) and int(lista[i+1])>int(lista[i+2]):
        peaks+=1

if peaks == 0:
    print("There are no peaks!")
else:
    print(peaks)