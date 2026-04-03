# Ejercicio 1— “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total

nombre_cliente = input("Cliente: ")

while not nombre_cliente.isalpha() or nombre_cliente == "":
    print("Nombre invalido. Ingrese su nombre nuevamente.")
    nombre_cliente = input("Cliente: ")

cant_productos = input("Cantidad de productos: ")

while not cant_productos.isdigit() or int(cant_productos) <= 0:
    print("Valor invalido. Ingrese la cantidad nuevamente.")
    cant_productos = input("Cantidad de productos: ")

cant_productos = int(cant_productos)

total_sin_descuentos = 0
descuento_suma = 0

for i in range(1, cant_productos + 1):
    precio_producto = input(f"Producto {i} - Precio: ")
    while not (precio_producto).isdigit() or int(precio_producto) <= 0:
        print("Precio invalido. Ingrese únicamente digitos enteros.")
        precio_producto = input(f"Producto {i} - Precio: ")

    precio_producto = float(precio_producto)
    total_sin_descuentos += precio_producto
    
    descuento = input("Descuento (S/N):").lower().strip()
    while descuento not in ("s", "n"):
        print("Valor invalido. Ingrese solo S o N.")
        descuento = input("Descuento (S/N):").lower().strip()


    if descuento == "s":
        precio_descuento = precio_producto * 0.10
        descuento_suma += precio_descuento
    
total_con_descuentos = total_sin_descuentos - descuento_suma
promedio_por_producto = total_sin_descuentos / cant_productos

print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos}")
print(f"Ahorro: ${descuento_suma}")
print(f"Promedio por producto ${promedio_por_producto:.2f}")


    
    

        

    


