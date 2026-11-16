# Limpia el nombre y lo compara con los registros existentes antes de aceptarlo.
def validar_nombre_herramienta(inventario, nombre):
    """Valida que el nombre no esté vacío ni se encuentre repetido."""
    nombre = nombre.strip()

    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    for herramienta_registrada in inventario:
        if herramienta_registrada['herramienta'].lower() == nombre.lower():
            raise ValueError("Ya existe una herramienta con ese nombre.")

    return nombre


# Repite la carga de cada dato hasta recibir valores válidos.
def cargar_herramientas(inventario):
    """Carga en el inventario una cantidad inicial de herramientas."""
    while True:
        try:
            cantidad_herramientas = int(
                input("¿Cuántas herramientas desea cargar?: ")
            )

            if cantidad_herramientas <= 0:
                raise ValueError(
                    "La cantidad de herramientas debe ser mayor que cero."
                )

        except ValueError as error:
            print(f"Error: {error}")
            print("Intente nuevamente.")
            continue

        break

    for numero in range(cantidad_herramientas):
        print(f"Herramienta {numero + 1} de {cantidad_herramientas}")

        while True:
            try:
                nombre = input("Nombre de la herramienta: ")
                nombre = validar_nombre_herramienta(inventario, nombre)

            except ValueError as error:
                print(f"Error: {error}")
                continue

            break

        while True:
            try:
                cantidad = int(input("Stock inicial: "))

                if cantidad < 0:
                    raise ValueError(
                        "El stock inicial no puede ser negativo."
                    )

            except ValueError as error:
                print(f"Error: {error}")
                print("Ingrese nuevamente el stock.")
                continue

            break

        inventario.append({
            'herramienta': nombre,
            'cantidad': cantidad
        })

        print(f"Herramienta '{nombre}' cargada correctamente.")

    print("Carga de herramientas finalizada.")


# Informa si no hay registros o recorre el inventario para mostrarlos.
def mostrar_inventario(inventario):
    """Muestra todas las herramientas y sus existencias actuales."""
    if len(inventario) == 0:
        print("El inventario está vacío.")
        print("Utilice la opción 1 para cargar varias herramientas o la opción 5 para agregar una herramienta.")
    else:
        print("--- INVENTARIO COMPLETO ---")

        for herramienta in inventario:
            print(
                f"Herramienta: {herramienta['herramienta']} | "
                f"Stock: {herramienta['cantidad']}"
            )


# Comprueba primero que haya datos y luego busca la herramienta por su nombre.
def consultar_stock(inventario):
    """Busca una herramienta y muestra la cantidad disponible."""
    if len(inventario) == 0:
        print("El inventario está vacío.")
        print("Utilice la opción 1 para cargar varias herramientas o la opción 5 para agregar una herramienta.")
        return

    nombre = input("Ingrese el nombre de la herramienta: ").strip()

    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre.lower():
            print(
                f"Stock de {herramienta['herramienta']}: "
                f"{herramienta['cantidad']} unidades."
            )
            return

    print(f"No se encontró la herramienta '{nombre}'.")


# Usa una bandera para avisar cuando ninguna herramienta tiene stock cero.
def mostrar_herramientas_agotadas(inventario):
    """Muestra las herramientas que no tienen existencias."""
    if len(inventario) == 0:
        print("El inventario está vacío.")
        print("Utilice la opción 1 para cargar varias herramientas o la opción 5 para agregar una herramienta.")
    else:
        hay_agotadas = False

        print("--- HERRAMIENTAS AGOTADAS ---")

        for herramienta in inventario:
            if herramienta['cantidad'] == 0:
                print(f"Herramienta: {herramienta['herramienta']}")
                hay_agotadas = True

        if not hay_agotadas:
            print("No hay herramientas agotadas.")


# Valida los datos ingresados antes de incorporar el nuevo registro.
def agregar_herramienta(inventario):
    """Agrega al inventario una herramienta nueva."""
    nombre = input("Nombre de la nueva herramienta: ")
    nombre = validar_nombre_herramienta(inventario, nombre)

    cantidad = int(input("Stock inicial: "))

    if cantidad < 0:
        raise ValueError("El stock inicial no puede ser negativo.")

    inventario.append({
        'herramienta': nombre,
        'cantidad': cantidad
    })

    print(f"Herramienta '{nombre}' agregada correctamente.")


# Busca la herramienta y aplica el movimiento solo después de validarlo.
def actualizar_existencias(inventario):
    """Actualiza las existencias mediante una venta o un ingreso."""
    if len(inventario) == 0:
        print("El inventario está vacío.")
        print("Utilice la opción 1 para cargar varias herramientas o la opción 5 para agregar una herramienta.")
        return

    nombre = input("Nombre de la herramienta: ").strip()

    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre.lower():
            break
    else:
        print(f"No se encontró la herramienta '{nombre}'.")
        return

    movimiento = input("Tipo de movimiento (venta/ingreso): ").strip().lower()

    if movimiento != "venta" and movimiento != "ingreso":
        print("Tipo de movimiento inválido. Ingrese venta o ingreso.")
        return

    cantidad = int(input("Cantidad de unidades: "))

    if cantidad <= 0:
        raise ValueError("La cantidad de unidades debe ser mayor que cero.")

    if movimiento == "venta":
        if cantidad > herramienta['cantidad']:
            raise ValueError(
                "No hay stock suficiente para realizar la venta."
            )

        herramienta['cantidad'] = herramienta['cantidad'] - cantidad

        print("Venta registrada correctamente.")

    else:
        herramienta['cantidad'] = herramienta['cantidad'] + cantidad

        print("Ingreso de mercadería registrado correctamente.")

    print(
        f"Stock actualizado de {herramienta['herramienta']}: "
        f"{herramienta['cantidad']} unidades."
    )


# Mantiene el menú activo hasta que el usuario elige la opción de salida.
def programa_principal():
    """Gestiona el menú principal del sistema de inventario."""
    inventario = []
    salir = False

    while not salir:
        print("========== SISTEMA DE INVENTARIO ==========")
        print("1. Cargar herramientas con existencias iniciales")
        print("2. Mostrar inventario")
        print("3. Consultar stock")
        print("4. Mostrar herramientas agotadas")
        print("5. Agregar una herramienta")
        print("6. Actualizar existencias")
        print("7. Salir")
        print("============================================")

        try:
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                raise ValueError(
                    "La opción del menú debe ser un número entero."
                )

            if opcion < 1 or opcion > 7:
                raise ValueError(
                    "La opción debe estar comprendida entre 1 y 7."
                )

            if opcion == 1:
                cargar_herramientas(inventario)

            elif opcion == 2:
                mostrar_inventario(inventario)

            elif opcion == 3:
                consultar_stock(inventario)

            elif opcion == 4:
                mostrar_herramientas_agotadas(inventario)

            elif opcion == 5:
                agregar_herramienta(inventario)

            elif opcion == 6:
                actualizar_existencias(inventario)

            elif opcion == 7:
                salir = True
                print("Programa finalizado.")

        except ValueError as error:
            print(f"Error: {error}")


programa_principal()
