"""
1.Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
2.Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
3.Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
4.Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
5.Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
6.Crear una función que reciba un número entero y determine si es par o impar.
7.Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
8.Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
9.Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
10.Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.

"""


#1
# Función que calcula el mayor y menor 
def obtener_mayor_menor(arreglo):
    mayor = max(arreglo)
    menor = min(arreglo)
    return mayor, menor


# Función principal
def ejercicio1():
    arreglo = []
    
    cantidad = int(input("¿Cuántos números quieres ingresar?: "))

    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i+1}: "))
        arreglo.append(num)

    mayor, menor = obtener_mayor_menor(arreglo)

    print("Número mayor:", mayor)
    print("Número menor:", menor)

#2

# Función que cuenta las vocales
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vocales:
            contador += 1

    return contador


# Función principal
def ejercicio2():
    texto = input("Ingresa una cadena de texto: ")

    cantidad = contar_vocales(texto)

    print("Cantidad de vocales:", cantidad)


#3

def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def ejercicio3():
    nombres = []
    
    cantidad = int(input("¿Cuántos nombres quieres ingresar? "))
    
    for i in range(cantidad):
        nombre = input("Ingresa un nombre: ")
        print(f"{nombre} agregado con exito a la lista.")
        nombres.append(nombre)
    
    filtrados = filtrar(nombres)
    
    if filtrados:
        print("Los nombres con más de 5 letras son:")
        for nombre in filtrados:
            print(f"- {nombre}")
    else:
        print("No hay nombres con más de 5 letras.")

#4

# Función que calcula el promedio y determina si aprueba
def evaluar_estudiante(notas):
    promedio = sum(notas) / len(notas)
    
    if promedio >= 4.0:
        estado = "Aprueba"
    else:
        estado = "Reprueba"
    
    return promedio, estado


# Función principal
def ejercicio4():
    notas = []
    
    cantidad = int(input("¿Cuántas notas ingresarás?: "))

    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    promedio, estado = evaluar_estudiante(notas)

    print("Promedio:", round(promedio, 2))
    print("Resultado:", estado)


#5

# Función que aplica el descuento
def aplicar_descuento(precios):
    precios_con_descuento = []

    for precio in precios:
        nuevo_precio = precio * 0.9  # 10% de descuento
        precios_con_descuento.append(nuevo_precio)

    return precios_con_descuento


# Función principal
def ejercicio5():
    precios = []
    
    cantidad = int(input("¿Cuántos productos ingresarás?: "))

    for i in range(cantidad):
        precio = float(input(f"Ingrese el precio del producto {i+1}: "))
        precios.append(precio)

    precios_desc = aplicar_descuento(precios)

    print("\nPrecios originales y con descuento:")
    for i in range(len(precios)):
        print(f"Producto {i+1}: Original = {precios[i]} | Con descuento = {round(precios_desc[i], 2)}")

#6

# Función que determina si es par o impar
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"


# Función principal
def ejercicio6():
    numero = int(input("Ingresa un número entero: "))

    resultado = es_par_o_impar(numero)

    print("El número es:", resultado)


#7

# Función que cuenta mayores de edad
def contar_mayores(edades):
    contador = 0

    for edad in edades:
        if edad >= 18:
            contador += 1

    return contador


# Función principal
def ejercicio7():
    edades = []
    
    cantidad = int(input("¿Cuántas edades ingresarás?: "))

    for i in range(cantidad):
        edad = int(input(f"Ingrese la edad {i+1}: "))
        edades.append(edad)

    total_mayores = contar_mayores(edades)

    print("Cantidad de personas mayores de edad:", total_mayores)

#8

# Función que cuenta cuántas veces aparece una palabra
def contar_palabra(lista, palabra_buscar):
    contador = 0

    for palabra in lista:
        if palabra.lower() == palabra_buscar.lower():
            contador += 1

    return contador


# Función principal
def ejercicio8():
    palabras = []
    
    cantidad = int(input("¿Cuántas palabras ingresarás?: "))

    for i in range(cantidad):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        palabras.append(palabra)

    buscar = input("¿Qué palabra deseas buscar?: ")

    resultado = contar_palabra(palabras, buscar)

    print("La palabra aparece", resultado, "veces.")



#9

# Función que filtra números positivos
def obtener_positivos(numeros):
    positivos = []

    for num in numeros:
        if num > 0:
            positivos.append(num)

    return positivos


# Función principal
def ejercicio9():
    numeros = []
    
    cantidad = int(input("¿Cuántos números ingresarás?: "))

    for i in range(cantidad):
        num = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)

    lista_positivos = obtener_positivos(numeros)

    print("Números positivos:", lista_positivos)


#10

# Función que filtra productos con bajo stock
def productos_bajo_stock(productos):
    bajos = []

    for producto in productos:
        if producto["stock"] < 5:
            bajos.append(producto)

    return bajos


# Función principal
def ejercicio10():
    productos = []
    
    cantidad = int(input("¿Cuántos productos ingresarás?: "))

    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
        stock = int(input(f"Ingrese el stock de {nombre}: "))

        producto = {
            "nombre": nombre,
            "stock": stock
        }

        productos.append(producto)

    resultado = productos_bajo_stock(productos)

    print("\nProductos con stock menor a 5:")
    for p in resultado:
        print(f"Producto: {p['nombre']} | Stock: {p['stock']}")


def menu():
    while True:
        print("\n¿QUE EJERCICIO DESEAS EJECUTAR?")
        print("1. Mayor y menor")
        print("2. Contar vocales")
        print("3. Nombres con mas de 5 letras")
        print("4. Promedio y aprobación")
        print("5. Aplicar descuento")
        print("6. Par o impar")
        print("7. Mayores de edad")
        print("8. Buscar palabra")
        print("9. Números positivos")
        print("10. Productos bajo stock")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
menu()