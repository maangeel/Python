productosCompleto = input("Ingrese los productos: ").split("-")

# Inicializar listas
lista_productos = []
lista_precios = []
lista_stock = []

valorTotalInventario = 0

# Separar los datos en las listas correspondientes
for prod in productosCompleto:
    nombres, precios, stocks = prod.split(":") #asginación de variables a valores de la lista
    try:
        lista_productos.append(nombres)
        lista_precios.append(int(precios))
        lista_stock.append(int(stocks))
    except ValueError:
        print(f"Error al convertir precio o stock para el producto '{nombres}'. Verifique los datos ingresados.")
        print("Reinicie el programa e ingrese los datos correctamente.")

productoMasCaro = max(lista_precios)
indiceProductoMasCaro = lista_precios.index(productoMasCaro) #sirve para obtener el índice del producto más caro
productoNoStock = [lista_productos[j] for j in range(len(lista_stock)) if lista_stock[j] == 0]

for i in range(len(lista_productos)):
    valorTotalInventario += lista_precios[i] * lista_stock[i]
    print(f"Producto: {lista_productos[i]}, Precio: {lista_precios[i]}, Stock: {lista_stock[i]}")
print(f"Valor total del inventario: {valorTotalInventario}")
print(f"Producto más caro: {lista_productos[indiceProductoMasCaro]}, Precio: {productoMasCaro}")
print(f"Productos sin stock: {', '.join(productoNoStock) if productoNoStock else 'Ninguno'}")

lista_productos = [x for x in lista_productos if x not in productoNoStock] #cambia la lista para guardar los productos on stock
lista_precios = [lista_precios[i] for i in range(len(lista_stock)) if lista_stock[i] > 0] #cambia la lista para guardar los precios de los productos on stock
lista_stock = [lista_stock[i] for i in range(len(lista_stock)) if lista_stock[i] > 0] #cambia la lista para guardar los stock de los productos on stock

#resumen
print("\nResumen de productos con stock:")
for z in range(len(lista_productos)):
    print(f"Producto: {lista_productos[z]}, Precio: {lista_precios[z]}, Stock: {lista_stock[z]}")