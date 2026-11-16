# Ejercicio 1 
# ---------------------------------------------------------------------------
# a = 10
# b = input("Introduce un número: ")
# result = a / b # Error: TypeError. Ya que "b" no esta validado, "input()" devuelve un string y no se puede dividir un int por un str.
# print(f"Resultado: {result}")
# numbers = [1, 2, 3]
# print(numbers[5]) # Error: IndexError. Ya que el indice 5 no existe en la lista "numbers".
# ---------------------------------------------------------------------------
# Ejercicio 2
print("Ejercicio 2")
print("-------------------------------------")
a = 10
b = input("Introduce un número entero positivo distinto de 0: ")
# Con la validación correcta, el programa no arroja TypeError.
while not b.isdigit() or b == "0":
    print("Por favor, introduce un número entero positivo distinto de 0.")
    b = input("Introduce un número positivo distinto de 0: ")
b = int(b)
result = a / b
print(f"Resultado: {result}")
# Usando un indice correcto, el programa no arroja IndexError.
numbers = [1, 2, 3]
print(numbers[2])
print("-------------------------------------")
print("Ejercicio 2 terminado")
print("-------------------------------------")
# Ejercicio 3
print("Ejercicio 3")
print("-------------------------------------")
a = 10
try:
    b = input("Introduce un número: ")
    result = a / b
except:
    result = "Error. Valor no válido. No se ha podido realizar la operación."
print(f"Resultado: {result}")
numbers = [1, 2, 3]
try:
    print(numbers[5])
except:
    print("Error. Indice fuera de rango.")
print("-------------------------------------")
print("Ejercicio 3 terminado")
print("-------------------------------------")
# Ejercicio 4
print("Ejercicio 4")
print("-------------------------------------")
a = 10
try:
    b = input("Introduce un número: ")
    result = a / b
except TypeError:
    result = "Error. Valor no válido. No se ha podido realizar la operación."
print(f"Resultado: {result}")
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error. Indice fuera de rango.")
print("-------------------------------------")
print("Ejercicio 4 terminado")
print("-------------------------------------")
# Ejercicio 5
print("Ejercicio 5")
print("-------------------------------------")
a = 10
try:
    b = input("Introduce un número: ")
    result = a / b
except TypeError:
    print("Error. No se puede dividir un número por un texto.")
else:
    print(f"Resultado: {result}")
finally:
    print("Finalizó la operación.")
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error. Índice fuera de rango.")
else:
    print("El índice es válido.")
finally:
    print("Finalizó el acceso a la lista.")
print("-------------------------------------")
print("Ejercicio 5 terminado")
print("-------------------------------------")
# Ejercicio 6
print("Ejercicio 6")
print("-------------------------------------")
try:
    numero = int(input("Ingrese un número: "))
    print(numero)

except ValueError:
    print("Debe ingresar un número válido")

except Exception as error:
    print("Se produjo un error inesperado:", error)
print("-------------------------------------")
print("Ejercicio 6 terminado")
print("-------------------------------------")
# Ejercicio 7
print("Ejercicio 7")
print("-------------------------------------")
while True:
    try:
        numero = int(input("Ingrese un número: "))
        print(numero)

    except ValueError:
        print("Debe ingresar un número válido")

    except Exception as error:
        print("Se produjo un error inesperado:", error)

    else:
        break
print("-------------------------------------")
print("Ejercicio 7 terminado")
print("-------------------------------------")
input("Presiona enter para salir...")