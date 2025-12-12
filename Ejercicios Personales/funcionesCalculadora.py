opcion = 0
resultado = 0
continuar = ""
continueProgram = 1
#función introducir un valor
def introValor(inputMessage):
    while True:
        try:
            return float(input(inputMessage))
        except ValueError:
            print("El valor introducido es incorrecto")

#función interfaz del menú
def menu():
    print("\n--- Calculadora ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

#continuar programa
def continuarPrograma(mensage):
    while True:
        try:
            continuar = input(mensage)
            if continuar.lower() == "s":
                main()
            elif continuar.lower() == "n":
                continueProgram=0
                print("Finalizando")
                break
        except ValueError:
            print("Error")
            break

#función suma
def suma(a,b):
    return a+b

#función resta
def resta(a,b):
    return a-b

#función multiplicación
def multi(a,b):
    return a*b

#función división
def divi(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Syntax Error")
    
def main():
    while True:
        menu() #muestra menú
        opcion = input("Introduce una opción: ")

        if opcion == "5": #opción salir
            continueProgram=0 #evita que el programa siga
            break
        elif opcion not in ("1","2","3","4"):
            print("Opción no válida")
            continue #vuelve al bucle
        else:
            continueProgram=1 #permite seguir el programa
            break #pasa a las operaciones

    if continueProgram==1:
        #inputs
        num1 = introValor("Introduce un valor: ")
        num2 = introValor("Introduce otro valor: ")

        try: #opciones comprobación de error y suma
            if opcion == "1":
                resultado = suma(num1,num2)
                print(resultado)
            if opcion == "2":
                resultado = resta(num1,num2)
                print(resultado)
            if opcion == "3":
                resultado = multi(num1,num2)
                print(resultado)
            if opcion == "4":
                resultado = divi(num1,num2)
                print(resultado)
        except ValueError as e:
            print(f"Syntax Error, {e}")
        continuarPrograma("¿Quieres continuar el programa? s/n: ")
            

#inicio del programa
if continueProgram==1: #sirve para iniciar
    continuarPrograma("¿Quieres iniciar el programa? s/n: ")