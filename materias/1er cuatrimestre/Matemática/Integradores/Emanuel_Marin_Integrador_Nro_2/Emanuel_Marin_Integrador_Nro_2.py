print("==================================================")
print("--- DISEÑO DE DIAGRAMA DE VENN DE 3 CONJUNTOS ---")
print("==================================================")

def pedir_entero_no_negativo(mensaje):
    """Solicita un número entero no negativo y repite la entrada si es inválida."""
    while True:
        try:
            valor_ingresado = int(input(mensaje))
            if valor_ingresado >= 0:
                return valor_ingresado
            print("Ingrese un número entero positivo (mayor o igual que 0).")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero positivo.")

# Solicitar los datos del universo y los tres conjuntos.
descripcion_universo = input("Ingrese la descripción del universo (U): ")
cantidad_universo = pedir_entero_no_negativo("Cantidad total de elementos de U: ")

nombre_conjunto_a = input("Nombre del conjunto A: ")
cantidad_conjunto_a = pedir_entero_no_negativo(f"Cantidad total de elementos en {nombre_conjunto_a}: ")

nombre_conjunto_b = input("Nombre del conjunto B: ")
cantidad_conjunto_b = pedir_entero_no_negativo(f"Cantidad total de elementos en {nombre_conjunto_b}: ")

nombre_conjunto_c = input("Nombre del conjunto C: ")
cantidad_conjunto_c = pedir_entero_no_negativo(f"Cantidad total de elementos en {nombre_conjunto_c}: ")

print("--- Ingrese las intersecciones (totales, incluida la triple) ---")

cantidad_interseccion_ab = pedir_entero_no_negativo(f"Elementos en {nombre_conjunto_a} y {nombre_conjunto_b}: ")
cantidad_interseccion_ac = pedir_entero_no_negativo(f"Elementos en {nombre_conjunto_a} y {nombre_conjunto_c}: ")
cantidad_interseccion_bc = pedir_entero_no_negativo(f"Elementos en {nombre_conjunto_b} y {nombre_conjunto_c}: ")
cantidad_interseccion_abc = pedir_entero_no_negativo("Elementos que pertenecen a los TRES conjuntos: ")

# Validar que las cantidades ingresadas sean matemáticamente coherentes.
if cantidad_conjunto_a > cantidad_universo or cantidad_conjunto_b > cantidad_universo or cantidad_conjunto_c > cantidad_universo:
    print("ERROR MATEMÁTICO: Ningún conjunto puede tener más elementos que el universo.")

elif (cantidad_interseccion_ab > cantidad_conjunto_a or cantidad_interseccion_ab > cantidad_conjunto_b or
      cantidad_interseccion_ac > cantidad_conjunto_a or cantidad_interseccion_ac > cantidad_conjunto_c or
      cantidad_interseccion_bc > cantidad_conjunto_b or cantidad_interseccion_bc > cantidad_conjunto_c):
    print("ERROR MATEMÁTICO: Una intersección doble no puede superar a los conjuntos que la forman.")

elif cantidad_interseccion_abc > cantidad_interseccion_ab or cantidad_interseccion_abc > cantidad_interseccion_ac or cantidad_interseccion_abc > cantidad_interseccion_bc:
    print("ERROR MATEMÁTICO: La intersección triple no puede ser mayor que las intersecciones dobles.")

else:
    # Cálculo de las regiones.
    elementos_interseccion_abc = cantidad_interseccion_abc

    elementos_solo_ab = cantidad_interseccion_ab - elementos_interseccion_abc
    elementos_solo_ac = cantidad_interseccion_ac - elementos_interseccion_abc
    elementos_solo_bc = cantidad_interseccion_bc - elementos_interseccion_abc

    elementos_solo_a = cantidad_conjunto_a - elementos_solo_ab - elementos_solo_ac - elementos_interseccion_abc
    elementos_solo_b = cantidad_conjunto_b - elementos_solo_ab - elementos_solo_bc - elementos_interseccion_abc
    elementos_solo_c = cantidad_conjunto_c - elementos_solo_ac - elementos_solo_bc - elementos_interseccion_abc

    cantidad_total_dentro_conjuntos = (elementos_solo_a + elementos_solo_b + elementos_solo_c +
                                       elementos_solo_ab + elementos_solo_ac + elementos_solo_bc +
                                       elementos_interseccion_abc)

    elementos_fuera_de_todos_los_conjuntos = cantidad_universo - cantidad_total_dentro_conjuntos

    if (elementos_solo_a < 0 or elementos_solo_b < 0 or elementos_solo_c < 0 or
            elementos_solo_ab < 0 or elementos_solo_ac < 0 or elementos_solo_bc < 0):
        print("ERROR MATEMÁTICO: Los datos de los conjuntos o de las intersecciones dobles son inconsistentes (generan regiones negativas).")

    elif elementos_fuera_de_todos_los_conjuntos < 0:
        print(f"ERROR MATEMÁTICO: La suma de las regiones ({cantidad_total_dentro_conjuntos}) supera el total del universo ({cantidad_universo}).")

    else:
        # Mostrar los resultados de las ocho regiones del diagrama.
        print("==================================================")
        print(f"RESULTADOS PARA EL UNIVERSO: {descripcion_universo}")
        print("==================================================")
        print(f"1. Pertenecen exclusivamente a {nombre_conjunto_a}: {elementos_solo_a}")
        print(f"2. Pertenecen exclusivamente a {nombre_conjunto_b}: {elementos_solo_b}")
        print(f"3. Pertenecen exclusivamente a {nombre_conjunto_c}: {elementos_solo_c}")
        print(f"4. Pertenecen exclusivamente a {nombre_conjunto_a} y {nombre_conjunto_b}: {elementos_solo_ab}")
        print(f"5. Pertenecen exclusivamente a {nombre_conjunto_a} y {nombre_conjunto_c}: {elementos_solo_ac}")
        print(f"6. Pertenecen exclusivamente a {nombre_conjunto_b} y {nombre_conjunto_c}: {elementos_solo_bc}")
        print(f"7. Pertenecen a los tres conjuntos simultáneamente: {elementos_interseccion_abc}")
        print(f"8. No pertenecen a ninguno de los tres conjuntos: {elementos_fuera_de_todos_los_conjuntos}")
        print("==================================================")
        print(f"Comprobación final: la suma de las 8 regiones es {cantidad_total_dentro_conjuntos + elementos_fuera_de_todos_los_conjuntos}, que debe ser igual al total del universo, que es {cantidad_universo}.")
        print("==================================================")
input("Presione Enter para salir...")
