# Ejercicio 1
print("Ejercicio 1")
print("-------------------------------")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)
print("-------------------------------")
print("Ejercicio 1 Terminado")
print("-------------------------------")
# Ejercicio 2
print("Ejercicio 2")
print("-------------------------------")
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)
print("-------------------------------")
print("Ejercicio 2 Terminado")
print("-------------------------------")
# Ejercicio 3
print("Ejercicio 3")
print("-------------------------------")
solo_nombres = list(precios_frutas.keys())
print(solo_nombres)
print("-------------------------------")
print("Ejercicio 3 Terminado")
print("-------------------------------")
# Ejercicio 4
print("Ejercicio 4")
print("-------------------------------")
diccionario = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    while not nombre.isalpha():
        print("El nombre debe contener solo letras")
        nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    telefono = input(f"Ingrese el telefono del contacto {i + 1}: ")
    while not telefono.isdigit() or len(telefono) != 8:
        print("El telefono debe contener solo numeros y ser de 8 digitos")
        telefono = input(f"Ingrese el telefono del contacto {i + 1}: ")
    diccionario[nombre] = telefono
verificar = input("Ingrese el nombre del contacto a verificar: ")
while not verificar.isalpha():
    print("El nombre debe contener solo letras")
    verificar = input("Ingrese el nombre del contacto a verificar: ")
if verificar in diccionario:
    print(f"El contacto {verificar} se encuentra registrado con el telefono {diccionario[verificar]}")
else:
    print(f"El contacto {verificar} no se encuentra registrado")
print("-------------------------------")
print("Ejercicio 4 Terminado")
print("-------------------------------")
# Ejercicio 5
print("Ejercicio 5")
print("-------------------------------")
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
cantidad_de_cada_palabra = {}
for palabra in palabras_unicas:
    cantidad_de_cada_palabra[palabra] = palabras.count(palabra)
print(cantidad_de_cada_palabra)
print("-------------------------------")
print("Ejercicio 5 Terminado")
print("-------------------------------")
# Ejercicio 6
print("Ejercicio 6")
print("-------------------------------")
alumnos = {}
for numero_alumno in range(3):
    nombre = input(f"Ingrese el nombre del alumno {numero_alumno + 1}: ")
    while not nombre.isalpha():
        print("El nombre debe contener solo letras")
        nombre = input(f"Ingrese el nombre del alumno {numero_alumno + 1}: ")
    notas = []
    for numero_nota in range(3):
        nota = input(f"Ingrese la nota {numero_nota + 1} del alumno {nombre}: ")
        while not nota.isdigit() or int(nota) > 10 or int(nota) < 0:
            print("La nota debe ser un numero entre 0 y 10")
            nota = input(f"Ingrese la nota {numero_nota + 1} del alumno {nombre}: ")
        notas.append(int(nota))
    alumnos[nombre] = tuple(notas)
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio del alumno {alumno} es {promedio}")
print(alumnos)
print("-------------------------------")
print("Ejercicio 6 Terminado")
print("-------------------------------")
# Ejercicio 7
print("Ejercicio 7")
print("-------------------------------")
asistencias = ["Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Sofía", "Miguel", "Pilar", "Fernando", "Lucía", "Juan"]
print(asistencias)
veces_que_asistio = {}
for alumno in asistencias:
    veces_que_asistio[alumno] = asistencias.count(alumno)
asistencias = set(asistencias)
for alumno in asistencias:
    print(f"El alumno {alumno} asistio {veces_que_asistio[alumno]} veces")
print(asistencias)
print("-------------------------------")
print("Ejercicio 7 Terminado")
print("-------------------------------")
# Ejercicio 8
print("Ejercicio 8")
print("-------------------------------")
productos = {
    "Arroz": 15,
    "Fideos": 20,
    "Leche": 8,
    "Huevos": 12,
    "Aceite": 10,
    "Harina": 6
}
print(f"Menu de productos: {productos}")
print("""1. Consultar stock de un producto
2. Agregar stock de un producto
3. Agregar un nuevo producto (si no existe)""")
opcion = input("Ingrese una opcion del menu (1, 2 o 3): ")
while opcion != "1" and opcion != "2" and opcion != "3":
    print("La opcion debe ser 1, 2 o 3")
    opcion = input("Ingrese una opcion del menu (1, 2 o 3): ")
if opcion == "1":
    producto = input("Ingrese el nombre del producto: ")
    while producto not in productos:
        print("El producto no se encuentra registrado")
        producto = input("Ingrese el nombre del producto: ")
    print(f"El stock del producto {producto} es {productos[producto]}")
elif opcion == "2":
    producto = input("Ingrese el nombre del producto: ")
    while producto not in productos:
        print("El producto no se encuentra registrado")
        producto = input("Ingrese el nombre del producto: ")
    cantidad = input("Ingrese la cantidad de a agregar: ")
    while not cantidad.isdigit():
        print("La cantidad debe ser un numero")
        cantidad = input("Ingrese la cantidad a agregar: ")
    productos[producto] += int(cantidad)
    print(f"El stock del producto {producto} es {productos[producto]}")
else:
    producto = input("Ingrese el nombre del producto: ")
    while producto in productos:
        print("El producto ya se encuentra registrado")
        producto = input("Ingrese el nombre del producto: ")
    cantidad = input("Ingrese la cantidad de a agregar: ")
    while not cantidad.isdigit():
        print("La cantidad debe ser un numero")
        cantidad = input("Ingrese la cantidad a agregar: ")
    productos[producto] = int(cantidad)
    print(f"El stock del producto {producto} es {productos[producto]}")
print(f"Menu de productos: {productos}")
print("-------------------------------")
print("Ejercicio 8 Terminado")
print("-------------------------------")
# Ejercicio 9
print("Ejercicio 9")
print("-------------------------------")
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Cita médica",
    ("Miércoles", "18:00"): "Entrevista de trabajo",
    ("Jueves", "09:00"): "Cumpleaños de Juan",
    ("Viernes", "12:00"): "Salida temprana"
}
print("Seleccione un dia de la semana y hora para ver su actividad")
dia = input("Ingrese el dia de la semana (Lunes, Martes, Miércoles, Jueves o Viernes): ")
while dia not in ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes"):
    print("El dia debe ser Lunes, Martes, Miércoles, Jueves o Viernes")
    dia = input("Ingrese el dia de la semana (Lunes, Martes, Miércoles, Jueves o Viernes): ")
hora = input("Ingrese la hora (10:00, 14:00, 18:00, 09:00 o 12:00): ")
while hora not in ("10:00", "14:00", "18:00", "09:00", "12:00"):
    print("La hora debe ser 10:00, 14:00, 18:00, 09:00 o 12:00")
    hora = input("Ingrese la hora (10:00, 14:00, 18:00, 09:00 o 12:00): ")
while (dia, hora) not in agenda:
    print("No hay una actividad agendada para ese dia y hora")
    dia = input("Ingrese el dia de la semana (Lunes, Martes, Miércoles, Jueves o Viernes): ")
    while dia not in ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes"):
        print("El dia debe ser Lunes, Martes, Miércoles, Jueves o Viernes")
        dia = input("Ingrese el dia de la semana (Lunes, Martes, Miércoles, Jueves o Viernes): ")
    hora = input("Ingrese la hora (10:00, 14:00, 18:00, 09:00 o 12:00): ")
    while hora not in ("10:00", "14:00", "18:00", "09:00", "12:00"):
        print("La hora debe ser 10:00, 14:00, 18:00, 09:00 o 12:00")
        hora = input("Ingrese la hora (10:00, 14:00, 18:00, 09:00 o 12:00): ")
print(f"El evento de {dia} a las {hora} es {agenda[(dia, hora)]}")
print("-------------------------------")
print("Ejercicio 9 Terminado")
print("-------------------------------")
# Ejercicio 10
print("Ejercicio 10")
print("-------------------------------")
diccionario_original = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "España": "Madrid",
    "Francia": "París",
    "México": "Ciudad de México"
}
print(diccionario_original)
diccionario_al_reves = {}
for pais, ciudad in diccionario_original.items():
    diccionario_al_reves[ciudad] = pais
print(diccionario_al_reves)
print("Ejercicio 10 Terminado")
print("-------------------------------")
input("Presione enter para salir...")