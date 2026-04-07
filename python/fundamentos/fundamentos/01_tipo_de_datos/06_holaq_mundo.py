#Primera prueba
print("Hola, mundo")

#Saluda con tu nombre
nombre = "Valeria"

print("Hola,", nombre)

print("Hola, " + nombre)


#Presenta tu número de la suerte
numero = 7
print("Mi numero de la suerte es el", str(numero) + "!")
print("Mi numero de la suerte es el " + str(numero) + "!")


#Comparte tus gustos
comida1 = "pizza"
comida2 = "sushi"

print("Me encanta comer {} y {}!".format(comida1, comida2))

print(f"Me encanta comer {comida1} y {comida2}!")


#Desafío bonus: métodos de cadenas
frase = "  Python es genial  "

print(frase.upper())# Mayúsculas
print(frase.lower())# Minúsculas
print(frase.strip())# Elimina espacios al inicio y al final
print(len(frase.strip()))# Longitud de la cadena sin espacios
print(frase.strip().count("e"))# Cuenta ocurrencias de la letra "e"