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



def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def mostrar():
    nombres = []
    
    cantidad = int(input("¿Cuántos nombres quieres ingresar? "))
    
    for i in range(cantidad):
        nombre = input("Ingresa un nombre: ")
        print(f"{nombre} agregado con exito a la lista.")
        nombres.append(nombre)
        
    
    for nombre in filtrar(nombres):
        print("Los nombres con más de 5 Letras son: ")
        print(nombre)

mostrar()