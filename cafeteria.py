def calcular_total(precio,cantidad):
    return precio*cantidad

print("=================================")
print("SISTEMA PEDIDOS CAFETERÍA EL MONO")
print("=================================")

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

valor = calcular_total(precio,cantidad)
print()
print("Pedido registrado")
print("producto", producto)
print("Precio: $", precio)
print("Valor Subtotal: $", valor)
print("El producto tiene un descuento del 10%")
descuento = valor *0.9
print("Valor total: $", descuento)