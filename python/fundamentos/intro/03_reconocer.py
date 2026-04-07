"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random #importa libreria para procesos aleatorios


nombre = "Frida Kahlo"#creacion de variable  tipo texto con  un valor incluido
print(type(nombre))#imprime el tipo de dato de la variable "nombre"
print(len(nombre))#imprime el largo de la variable


edad = 25#creacion de la variable edad con un valor numerico incluido


if edad < 18: #creacion de una condicional con condiciones incluidas
   print("Eres menor de edad.")#imprime un mensaje en tipo string
elif edad == 18:#condicion else if
   print("Tienes 18 años.")#imprime string
else:#condicion si no se cumple ninguna anterior
   print("Eres mayor de edad.")#imprime string


frutas = ["manzana", "pera", "fresa"]#creacion de la variable con un array incluido
print(frutas[0])#imprime el primer objeto de el arreglo
frutas[0] = "banana"#A la posicion 0 del arreglo se le remplaza con otro valor
frutas.append("uva")#se agrega un valor al final del arreglo
frutas.remove("pera")#se elimina un valor del arreglo


dimensiones = (200, 50) #Variable tipo tupla(variable inmutable)
print(dimensiones[0])# Muestra el primer valor de la variable


persona = { #Variable tipo objetos
   "nombre": "Carlos",#Se establece iten y su valor
   "edad": 30
}
print(persona["nombre"])#Imprime el valor del item de la variable persona
persona["edad"] = 31#Remplaza datos de un item de la variable persona
persona["ciudad"] = "Santiago"#Agrega un item y su valor a la variable
del persona["ciudad"]# Se elimina el item y su valor


for i in range(5):#Se crea un bucle, se declara la variable y se establece un rango
   if i == 2:#Condicional if 
       continue #Ignora el proceso y continua
   if i == 4: #Condicional if
       break#Detiene el bucle cuando "i" sea = 4
   print(i)#Imprime el valor de la variable "i"


contador = 0 #variable tipo numero
while contador < 3: #Bucle while con condicion
   print(f"while contador es: {contador}")#Imprime el numero recorrido (0,1,2) concatenado
   contador += 1 #Incrementa de 1 en 1 a la variable


def saludar_usuario(nombre):#Define una funcion
   return f"Hola, {nombre}" #devuelve una concatenacion


print(saludar_usuario("Francisca"))#Imprime lo que regrese la funcionnnnnnn.....