# Ejercicio 1
print("Ejercicio 1")
with open("productos.txt", "w") as archivo:
    archivo.write("pan,2200.00,15\nlentejas,3000.00,25\narroz,3500.00,26\n")
    print(f"Archivo productos.txt creado con éxito")
print("---------------------------------")
print("Ejercicio 1 terminado")
print("---------------------------------")
# Ejercicio 2
print("Ejercicio 2")
print("---------------------------------")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(
            f"Producto: {datos[0]} | "
            f"Precio: ${datos[1]} | "
            f"Cantidad: {datos[2]}"
        )
print("Ejercicio 2 terminado")
print("---------------------------------")
# Ejercicio 3
print("Ejercicio 3")
print("---------------------------------")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(
            f"Producto: {datos[0]} | "
            f"Precio: ${datos[1]} | "
            f"Cantidad: {datos[2]}"
        )
with open("productos.txt", "a") as archivo:
    print("Formato de productos.txt: producto,precio,cantidad")
    nuevo = input("Ingrese el nuevo producto: ")
    lista = nuevo.split(",")
    valido = False
    validoA = False
    validoB = False
    validoC = False
    count = 0
    if len(lista) != 3:
        pass
    else:
        for i in lista:
            count += 1
            if count == 1 and i.isalpha():
                validoA = True
            elif count == 2:
                try:
                    precio = float(i)

                    if precio >= 0:
                        validoB = True
                    else:
                        print("El precio no puede ser negativo.")

                except ValueError:
                    print("El precio debe ser decimal.")
            elif count == 3 and i.isnumeric():
                validoC = True
            if validoA == True and validoB == True and validoC == True:
                valido = True
    while valido == False:
        print("Formato de productos.txt: producto,precio,cantidad")
        nuevo = input("Ingrese el nuevo producto: ")
        lista = nuevo.split(",")
        count = 0
        validoA = False
        validoB = False
        validoC = False
        if len(lista) != 3:
            print("Formato de productos.txt: producto,precio,cantidad")
        else:
            for i in lista:
                count += 1
                if count == 1 and i.isalpha():
                    validoA = True
                elif count == 2:
                    try:
                        precio = float(i)

                        if precio >= 0:
                            validoB = True
                        else:
                            print("El precio no puede ser negativo.")

                    except ValueError:
                        print("El precio debe ser decimal.")
                elif count == 3 and i.isnumeric():
                    validoC = True
                if validoA == True and validoB == True and validoC == True:
                    valido = True
    archivo.write(f"{nuevo}\n")
print("Archivo productos.txt actualizado con éxito")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(
            f"Producto: {datos[0]} | "
            f"Precio: ${datos[1]} | "
            f"Cantidad: {datos[2]}"
        )
print("---------------------------------")
print("Ejercicio 3 terminado")
print("---------------------------------")
# Ejercicio 4
print("Ejercicio 4")
print("---------------------------------")
productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)
print(productos)
print("---------------------------------")
print("Ejercicio 4 terminado")
print("---------------------------------")
# Ejercicio 5
print("Ejercicio 5")
print("---------------------------------")
encontrado = False
nombre = input("Ingrese el nombre del producto a buscar: ")
while not nombre.isalpha():
    print("Ingrese un nombre válido.")
    nombre = input("Ingrese el nombre del producto a buscar: ")
for linea in productos:
    if linea["nombre"] == nombre:
        print(f"Producto encontrado: {linea}")
        encontrado = True
if not encontrado:
    print("Producto no encontrado.")
print("---------------------------------")
print("Ejercicio 5 terminado")
print("---------------------------------")
print("Ejercicio 6")
print("---------------------------------")
# Ejercicio 6
# Se vuelve a guardar la lista en el archivo para demostrar la persistencia
# de los datos, aunque el producto ya fue guardado en el ejercicio 3.
with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(
            f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("Archivo productos.txt actualizado con éxito")
print("---------------------------------")
print("Ejercicio 6 terminado")
print("---------------------------------")
input("Presione enter para salir...")
