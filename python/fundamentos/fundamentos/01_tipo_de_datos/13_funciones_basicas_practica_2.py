import os

# Ejercicio 1
# Calcula experiencia
def multiplica_por_2(n):
    resultado = []
    for i in range(n + 1):
        resultado.append(i * 2)
    return resultado

def ejercicio1():
    result1 = multiplica_por_2(5)
    print("Retorno de la función:", result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]


# Ejercicio 2
# Analiza publicaciones
def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    return suma, resta

def ejercicio2():
    suma, resta = suma_y_resta([120, 115])
    print("Resultado (suma):", suma)
    print("Retorno de la función (resta):", resta)
# Imprime: 235 y retorna: 5

# Ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma - len(lista)

def ejercicio3():
    lista = [10, 5, 3, 7]
    
    suma_total = 0
    for num in lista:
        suma_total += num

    longitud = len(lista)
    result3 = sumatoria_menos_longitud(lista)

    print("Suma total =", suma_total)
    print("Longitud =", longitud)
    print("Retorno de la función:", result3)
# Suma total = 25, longitud = 4, debe retornar: 21


# Ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        return []
    
    segundo = lista[1]
    resultado = []
    
    for num in lista:
        resultado.append(num * segundo)
    
    return resultado

def ejercicio4():
    lista1 = [100, 3, 50, 20]
    lista2 = [100]

    print("Longitud de la primera lista:", len(lista1))
    result4_1 = valores_multiplicados_segundo(lista1)
    print("Retorno de la función:", result4_1)
# Imprime: 4 y retorna: [300, 9, 150, 60]
    print("Longitud de la segunda lista:", len(lista2))
    result4_2 = valores_multiplicados_segundo(lista2)
    print("Retorno de la función:", result4_2)
# Imprime: 1 y retorna: []

# Ejercicio 5
# Genera precio fijo
def valor_multiplicado_longitud(valor, longitud):
    resultado = []
    for i in range(longitud):
        resultado.append(valor * longitud)
    return resultado

def ejercicio5():
    result5_1 = valor_multiplicado_longitud(5, 2)
    print("Retorno de la función:", result5_1)
# Debe retornar: [10, 10]
    result5_2 = valor_multiplicado_longitud(7, 5)
    print("Retorno de la función:", result5_2)
# Debe retornar: [35, 35, 35, 35, 35]
# MENÚ

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar:
    print("\n=== EJERCICIOS PYTHON ===")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("0. Salir")

    opcion = input("\nElige una opción (0-5): ")

    if opcion == "1":
        limpiar_consola()
        print("\nEjecutando el ejercicio 1:\n")
        ejercicio1()

    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutando el ejercicio 2:\n")
        ejercicio2()

    elif opcion == "3":
        limpiar_consola()
        print("\nEjecutando el ejercicio 3:\n")
        ejercicio3()

    elif opcion == "4":
        limpiar_consola()
        print("\nEjecutando el ejercicio 4:\n")
        ejercicio4()

    elif opcion == "5":
        limpiar_consola()
        print("\nEjecutando el ejercicio 5:\n")
        ejercicio5()

    elif opcion == "0":
        print("\nSaliendo del programa...")
        continuar = False

    else:
        print("\nOpción inválida. Intenta otra vez.")