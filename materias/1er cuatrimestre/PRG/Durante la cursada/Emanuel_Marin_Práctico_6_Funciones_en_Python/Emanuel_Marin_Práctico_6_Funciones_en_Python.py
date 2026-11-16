# Ejercicio 1
print("----------------------------------------------------")
print("Ejercicio 1")
print("----------------------------------------------------")
def imprimir_hola_mundo():
    """Imprime Hola Mundo."""
    print("Hola Mundo!")

imprimir_hola_mundo()
print("----------------------------------------------------")
print("Ejercicio 1 Terminado")
print("----------------------------------------------------")
# Ejercicio 2
print("----------------------------------------------------")
print("Ejercicio 2")
print("----------------------------------------------------")
def saludar_usuario(nombre):
    """Saluda al usuario."""
    saludo = f"Hola {nombre}!"
    return saludo
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)
print("----------------------------------------------------")
print("Ejercicio 2 Terminado")
print("----------------------------------------------------")
# Ejercicio 3
print("----------------------------------------------------")
print("Ejercicio 3")
print("----------------------------------------------------")
def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime la información personal del usuario."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
while edad.isdigit() == False:
    print("Error: La edad debe ser un número entero.")
    edad = input("Ingrese su edad: ")
edad = int(edad)
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
print("----------------------------------------------------")
print("Ejercicio 3 Terminado")
print("----------------------------------------------------")
# Ejercicio 4
print("----------------------------------------------------")
print("Ejercicio 4")
print("----------------------------------------------------")
def calcular_area_circulo(radio):
    """Calcula el área del círculo."""
    area = 3.14 * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    """Calcula el perímetro del círculo."""
    perimetro = 3.14 * 2 * radio
    return perimetro

radio = input("Ingrese el radio del círculo: ")
while radio.isdigit() == False:
    print("Error: El radio debe ser un número entero positivo.")
    radio = input("Ingrese el radio del círculo: ")
radio = int(radio)
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo con radio {radio} es {area} y su perímetro es {perimetro}")
print("----------------------------------------------------")
print("Ejercicio 4 Terminado")
print("----------------------------------------------------")
# Ejercicio 5
print("----------------------------------------------------")
print("Ejercicio 5")
print("----------------------------------------------------")
def segundos_a_horas(segundos):
    """Convierte segundos a horas."""
    horas = segundos / 3600
    return horas

segundos = input("Ingrese la cantidad de segundos: ")
while segundos.isdigit() == False:
    print("Error: La cantidad de segundos debe ser un número entero positivo.")
    segundos = input("Ingrese la cantidad de segundos: ")
segundos = int(segundos)
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas")
print("----------------------------------------------------")
print("Ejercicio 5 Terminado")
print("----------------------------------------------------")
# Ejercicio 6
print("----------------------------------------------------")
print("Ejercicio 6")
print("----------------------------------------------------")
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar (del 1 al 10) del número entero ingresado """
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = input("Ingrese un número entero: ")
while numero.startswith("-") and not numero[1:].isdigit() or not numero.startswith("-") and not numero.isdigit():
    print("Error: Ingrese un número entero.")
    numero = input("Ingrese un número entero: ")
numero = int(numero)
tabla_multiplicar(numero)
print("----------------------------------------------------")
print("Ejercicio 6 Terminado")
print("----------------------------------------------------")
# Ejercicio 7
print("----------------------------------------------------")
print("Ejercicio 7")
print("----------------------------------------------------")
def operaciones_basicas(a, b):
    """Realiza las operaciones basicas. 
    Suma, resta, multiplicación, división"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = "No se puede dividir por 0"
    else:
        division = a / b
    return suma, resta, multiplicacion, division

a = input("Ingrese el primer número entero: ")
while a.startswith("-") and not a[1:].isdigit() or not a.startswith("-") and not a.isdigit():
    print("Error: Ingrese un número entero.")
    a = input("Ingrese el primer número entero: ")
a = int(a)
b = input("Ingrese el segundo número entero: ")
while b.startswith("-") and not b[1:].isdigit() or not b.startswith("-") and not b.isdigit():
    print("Error: Ingrese un número entero.")
    b = input("Ingrese el segundo número entero: ")
b = int(b)
tupla = operaciones_basicas(a, b)
print(f"La suma de {a} y {b} es {tupla[0]}")
print(f"La resta de {a} y {b} es {tupla[1]}")
print(f"La multiplicación de {a} y {b} es {tupla[2]}")
if tupla[3] == "No se puede dividir por 0":
    print(f"La división de {a} y {b} es {tupla[3]}")
else:
    print(f"La división de {a} y {b} es {tupla[3]:.2f}")
print("----------------------------------------------------")
print("Ejercicio 7 Terminado")
print("----------------------------------------------------")
# Ejercicio 8
print("----------------------------------------------------")
print("Ejercicio 8")
print("----------------------------------------------------")
def calcular_imc(peso, altura):
    """Calcula el IMC. Ingrese su peso en kg y su altura en metros, respectivamente.
    \n Ejemplo: 70.0 1.70
    \n Use "." para ingresar los numeros, tal como en el ejemplo."""
    imc = peso / (altura ** 2)
    return imc

peso = input("Ingrese su peso en kg: ")

while not peso.replace(".", "").isdigit() or peso.count(".") > 1 or float(peso) <= 0:
    print("Error: El peso debe ser un número positivo.")
    peso = input("Ingrese su peso en kg: ")

peso = float(peso)
altura = input("Ingrese su altura en metros: ")

while not altura.replace(".", "").isdigit() or altura.count(".") > 1 or float(altura) <= 0:
    print("Error: La altura debe ser un número positivo.")
    altura = input("Ingrese su altura en metros: ")

altura = float(altura)
imc = calcular_imc(peso, altura)
print(f"Su IMC es {imc:.2f}")
print("----------------------------------------------------")
print("Ejercicio 8 Terminado")
print("----------------------------------------------------")
# Ejercicio 9
print("----------------------------------------------------")
print("Ejercicio 9")
print("----------------------------------------------------")
def celsius_a_fahrenheit(celsius):
    """Convierte de grados Celsius a Fahrenheit."""
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

celsius = input("Ingrese los grados Celsius: ")

while celsius.startswith("-") and not celsius[1:].isdigit() or not celsius.startswith("-") and not celsius.isdigit():
    print("Error: Los grados Celsius deben ser un número entero.")
    celsius = input("Ingrese los grados Celsius: ")

celsius = int(celsius)
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit")
print("----------------------------------------------------")
print("Ejercicio 9 Terminado")
print("----------------------------------------------------")
# Ejercicio 10
print("----------------------------------------------------")
print("Ejercicio 10")
print("----------------------------------------------------")
def calcular_promedio(a, b, c):
    """Calcula el promedio de tres números enteros"""
    promedio = (a + b + c) / 3
    return promedio

a = input("Ingrese el primer número entero: ")
while a.startswith("-") and not a[1:].isdigit() or not a.startswith("-") and not a.isdigit():
    print("Error: Ingrese un número entero.")
    a = input("Ingrese el primer número entero: ")
a = int(a)
b = input("Ingrese el segundo número entero: ")
while b.startswith("-") and not b[1:].isdigit() or not b.startswith("-") and not b.isdigit():
    print("Error: Ingrese un número entero.")
    b = input("Ingrese el segundo número entero: ")
b = int(b)
c = input("Ingrese el tercer número entero: ")
while c.startswith("-") and not c[1:].isdigit() or not c.startswith("-") and not c.isdigit():
    print("Error: Ingrese un número entero.")
    c = input("Ingrese el tercer número entero: ")
c = int(c)
promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es {promedio}")
print("----------------------------------------------------")
print("Ejercicio 10 Terminado")
input("Presione enter para salir.")