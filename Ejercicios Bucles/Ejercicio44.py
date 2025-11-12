#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’

for i in range(0,100,3): #recorre 0 a 100 de 3 en 3
    if i != 99: #así se evita poner coma al final de la serie.
        print(i,end=", ") #imprime i y manda que se siga el print en la misma línea
    else:
        print(i)