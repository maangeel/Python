#24. Corrige los errores del siguiente código y comprueba que se
#ejecuta correctamente.

var1=float(input("Introduce el peso: ")) #variable no puede comenzar por num
var2=float(input("Introduce la altura: ")) #declarar float
var_imc = var1 / var2**2 #la variable var_imc no está definida
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es:",var_imc) #errores print
if var_imc>25: #: de if
    print("Hay sobrepeso") #tabular
else:
    print("Estás dentro de los parámetros normales") #tabular
