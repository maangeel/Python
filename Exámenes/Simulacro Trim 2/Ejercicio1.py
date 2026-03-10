#entrada de datos
nums = input("Ingrese una lista de números separados por comas: ")

#conversión a lista de enteros
numerosInt = [int(num) for num in nums.split(",")]

# Eliminar el valor mayor y menor de la lista
if len(numerosInt) > 1:
    max_val = max(numerosInt)
    min_val = min(numerosInt)
    numerosInt.remove(max_val)
    numerosInt.remove(min_val)

print(nums)
print(numerosInt)

media = round(sum(numerosInt) / len(numerosInt), 2)

#clasiificación del rendimiento
match media:
    case media if media < 5:
        print("Rendimiento bajo.")
    case media if media > 10:
        print("Rendimiento alto.")
    case _:
        print("Rendimiento medio.")