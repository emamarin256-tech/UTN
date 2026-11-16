# Ejercicio 1
# Se pide crear una función recursiva que calcule el factorial de un número entero no
# negativo y utilizarla para calcular y mostrar en pantalla el factorial de todos los números
# enteros entre 1 y el número que indique el usuario.

print("----------------------------------------------------")
print("Ejercicio 1")
print("----------------------------------------------------")

def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)
numero_limite = input("Ingrese un número entero no negativo: ")
while not numero_limite.isdigit():
    print("Error: Ingrese un número entero no negativo.")
    numero_limite = input("Ingrese un número entero no negativo: ")
numero_limite = int(numero_limite)
while numero_limite < 0:
    print("Error: Ingrese un número entero no negativo.")
    numero_limite = input("Ingrese un número entero no negativo: ")
    while not numero_limite.isdigit():
        print("Error: Ingrese un número entero no negativo.")
        numero_limite = input("Ingrese un número entero no negativo: ")
    numero_limite = int(numero_limite)
for numero in range(1, numero_limite + 1):
    print(f"El factorial de {numero} es {factorial(numero)}")
    
print("----------------------------------------------------")
print("Ejercicio 1 Terminado")
print("----------------------------------------------------")

# Ejercicio 2
# Se pide crear una función recursiva que calcule el valor de la sucesión de Fibonacci en la
# posición indicada. Posteriormente, se pide mostrar la sucesión completa hasta la posición
# que especifique el usuario.

print("----------------------------------------------------")
print("Ejercicio 2")
print("----------------------------------------------------")

def fibonacci(posicion):
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1
    return fibonacci(posicion - 1) + fibonacci(posicion - 2)
posicion_limite = input("Ingrese la posición final de la sucesión de Fibonacci: ")
while not posicion_limite.isdigit():
    print("Error: Ingrese un número entero no negativo.")
    posicion_limite = input("Ingrese un número entero no negativo: ")
posicion_limite = int(posicion_limite)
while posicion_limite < 0:
    print("Error: Ingrese un número entero no negativo.")
    posicion_limite = input("Ingrese un número entero no negativo: ")
    while not posicion_limite.isdigit():
        print("Error: Ingrese un número entero no negativo.")
        posicion_limite = input("Ingrese un número entero no negativo: ")
    posicion_limite = int(posicion_limite)
sucesion = []
for posicion in range(posicion_limite + 1):
    sucesion.append(fibonacci(posicion))
print(f"Sucesión de Fibonacci hasta la posición {posicion_limite}:")
print(sucesion)

print("----------------------------------------------------")
print("Ejercicio 2 Terminado")
print("----------------------------------------------------")

# Ejercicio 3
# Se pide crear una función recursiva que calcule la potencia de un número base elevado a
# un exponente entero no negativo, utilizando la fórmula n ^ m = n ∗ (n^(m−1))
# , con n ^ 0 = 1 como caso base. Se pide probar la función en un algoritmo general.

print("----------------------------------------------------")
print("Ejercicio 3")
print("----------------------------------------------------")
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
base = input("Ingrese la base: ")
while True:
    try:
        base = float(base)
        break
    except ValueError:
        print("Error: ingrese un número válido para la base.")
        base = input("Ingrese la base: ")
exponente = input("Ingrese un exponente entero no negativo: ")
while not exponente.isdigit():
    print("Error: Ingrese un número entero no negativo.")
    exponente = input("Ingrese un número entero no negativo: ")
exponente = int(exponente)
while exponente < 0:
    print("Error: Ingrese un número entero no negativo.")
    exponente = input("Ingrese un número entero no negativo: ")
    while not exponente.isdigit():
        print("Error: Ingrese un número entero no negativo.")
        exponente = input("Ingrese un número entero no negativo: ")
    exponente = int(exponente)
print(f"{base}^{exponente} = {potencia(base, exponente)}")

print("----------------------------------------------------")
print("Ejercicio 3 Terminado")
print("----------------------------------------------------")

# Ejercicio 4
# Se pide crear una función recursiva en Python que reciba un número entero positivo
# en base decimal y devuelva su representación en binario como una cadena de texto.
# La representación binaria de un número utiliza solamente ceros (0) y unos (1), en base 2.

print("----------------------------------------------------")
print("Ejercicio 4")
print("----------------------------------------------------")


def decimal_a_binario(numero):
    if numero < 2:
        return str(numero)
    return decimal_a_binario(numero // 2) + str(numero % 2)
print(f"10 en binario es {decimal_a_binario(10)}")

print("----------------------------------------------------")
print("Ejercicio 4 Terminado")
print("----------------------------------------------------")

# Ejercicio 5
# Se pide implementar una función recursiva llamada es_palindromo(palabra) que reciba
# una cadena de texto sin espacios ni tildes y devuelva True si es un palíndromo o
# False si no lo es.

print("----------------------------------------------------")
print("Ejercicio 5")
print("----------------------------------------------------")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
print(f"'reconocer' es palíndromo: {es_palindromo('reconocer')}")
print(f"'python' es palíndromo: {es_palindromo('python')}")

print("----------------------------------------------------")
print("Ejercicio 5 Terminado")
print("----------------------------------------------------")

# Ejercicio 6
# Se pide escribir una función recursiva llamada suma_digitos(n) que reciba un número
# entero positivo y devuelva la suma de todos sus dígitos.
print("----------------------------------------------------")
print("Ejercicio 6")
print("----------------------------------------------------")

def suma_digitos(numero):
    if numero < 10:
        return numero
    return numero % 10 + suma_digitos(numero // 10)

print(f"La suma de los dígitos de 1234 es {suma_digitos(1234)}")
print(f"La suma de los dígitos de 305 es {suma_digitos(305)}")

print("----------------------------------------------------")
print("Ejercicio 6 Terminado")
print("----------------------------------------------------")

# Ejercicio 7
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos y así sucesivamente hasta llegar a un nivel
# con un solo bloque. Se pide escribir una función recursiva contar_bloques(n) que
# devuelva el total de bloques necesarios para construir toda la pirámide.

print("----------------------------------------------------")
print("Ejercicio 7")
print("----------------------------------------------------")

def contar_bloques(n):
    if n <= 1:
        return n
    return n + contar_bloques(n - 1)

print(f"La pirámide de 4 niveles necesita {contar_bloques(4)} bloques")

print("----------------------------------------------------")
print("Ejercicio 7 Terminado")
print("----------------------------------------------------")

# Ejercicio 8
# Se pide escribir una función recursiva llamada contar_digito(numero, digito) que
# reciba un número entero positivo y un dígito entre 0 y 9, y devuelva cuántas veces
# aparece ese dígito dentro del número.

print("----------------------------------------------------")
print("Ejercicio 8")
print("----------------------------------------------------")


def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)


print(f"El dígito 2 aparece {contar_digito(122332421, 2)} veces en 122332421")
print(f"El dígito 7 aparece {contar_digito(18999923456, 7)} veces en 18999923456")

print("----------------------------------------------------")
print("Ejercicio 8 Terminado")
print("----------------------------------------------------")

input("Presione enter para salir...")