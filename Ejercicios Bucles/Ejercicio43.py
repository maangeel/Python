#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra

word = input("Introduce una palabra: ")

for i in range(len(word)):
    print(f"En la posición {i} está la {word[i]}")