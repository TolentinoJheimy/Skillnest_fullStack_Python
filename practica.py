#Crear una función que reciba una lista de números y muestre:
#La suma total
#La cantidad de números ingresados
def desarrollo1(num):
    cantidadNum = len(num)
    suma_total = 0
    for suma in num :
        suma_total = suma_total + (suma)
    return cantidadNum, suma_total

def funcion1():
    listaNum = []
    numRango = int(input("Cuantos números deseas ingresar? "))

    for i in range(numRango):
        num = int(input(f"Ingrese el número {i+1}: "))
        listaNum.append(num)
    cantidad, sumaT = desarrollo1(listaNum)
    print(f"La cantidad de números ingresados es:  {cantidad}")
    print(f"La Suma de la cantidad de números ingresados es:  {sumaT}")


#2 Crear una función que reciba un texto y cuente cuántas consonantes tiene.
def desarrollo2(txt):
    vocales = "aeiouAEIOU"
    contador = 0
    for i in txt:
        if i.isalpha() and i not in vocales:
            contador +=1
    return contador            



def funcion2():
    text = input("Ingrese un texto... : ")
    resultado = desarrollo2(text)
    print(f"El texto {text} tiene {resultado} consonantes")


#3 Crear una función que reciba una lista de palabras y muestre solo las que comienzan con una vocal.
def desarrollo3(palabras):
    palabrasM = 0
    palabras_vocal = []
    vocales = "aeiouAEIOU"
    for i in palabras:
        if len(i) > 0 and i[0] in vocales:
            palabrasM +=1
            palabras_vocal.append(i)
    return palabrasM, palabras_vocal

def funcion3():
    palabras = []
    palabra = input("Cuantas palabras desea ingresar: ")
    if palabra.isdigit():
        palabra = int(palabra)
        for i in range(palabra):
            txt = input(f"ingresa la palabra Número {i+1}: ")
            palabras.append(txt)
        resultNum, resultVocal = desarrollo3(palabras)
        print(f"{resultNum} Palabras empiezan por vocal: \n- { "\n- ".join(resultVocal)}")
    else: print("Ingrese un valor valido.")

#4 Crear una función que reciba una lista de números decimales y muestre:
#El número mayor
#El número menor
#El promedio
def desarrollo4(num):
    numMayor = max(num)
    numMenor = min(num)
    promedio = sum(num) / len(num)
    return numMayor, numMenor, promedio

def ejercicio4():
    numeros = []
    numrange = input("Cuantos Números desea ingresar: ")
    if numrange.isdigit():
        numrange = int(numrange)
        for i in range(numrange):
            num = float(input(f"Ingrese el Número {i+1}: "))
            
            numeros.append(num)
        numMayor, numMenor, numPromedio = desarrollo4(numeros)
        print(f"El número mayor de la lista es {numMayor}, el menor es {numMenor} y el promedio es {numPromedio}")
    else:
        print("Error: debes ingresar un número válido")
ejercicio4()

#5 Crear una función que reciba una lista de precios y aplique un aumento del 15%, mostrando el precio nuevo.

#6 Crear una función que reciba un número entero y determine si es positivo, negativo o cero.

#7 Crear una función que reciba una lista de edades y muestre:
#Cuántos son menores de edad
#Cuántos son adultos mayores (60 o más)

#8 Crear una función que reciba una lista de palabras y muestre cuántas tienen exactamente 4 letras.

#9 Crear una función que reciba una lista de números y genere otra lista con los números que sean múltiplos de 3.

#10 Crear una función que reciba una lista de productos (diccionarios con nombre y precio) y muestre cuáles cuestan más de 1000.