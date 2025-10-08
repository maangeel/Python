#intento de ver si una variable es decimal o no

#método1
var = 3.4
var = str(var)

if "." in var:
    print("Es decimal")
total=var+4
print(total)


#metodo2
var = 3.4
if not var==var//1:
    print("Es decimal")
else:
    print("Es entero")

