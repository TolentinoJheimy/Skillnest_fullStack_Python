datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el pun[taje de Pedro a 75
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores


datos[2]["puntaje"] = 75

def imprimir_resultados(name : int, lista):
    print(f"{lista[name]["nombre"]} obtuvo {lista[name]["puntaje"]} puntos!!")

def imprimir_campo(datos, campo):
    for estudiante in datos:
        print(estudiante[campo])

imprimir_resultados(0, datos)
print()
imprimir_campo(datos, "nombre")
print()
imprimir_campo(datos, "puntaje")