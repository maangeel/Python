#inputs

var_min = int(input("Introduce el primer valor del intervalo: "))
var_max = int(input("Introduce el segundo valor del intervalo: "))
var_intervalo = int(input("Introduce el valor de incremento: "))


for i in range(var_min,var_max+1,var_intervalo): #suma 1 a var_max evitar error
    if i == var_min:   
        print(var_min,end="") #printea el primer valor
    else:
        print(f",{i}",end="") #printea el resto seguido de comas