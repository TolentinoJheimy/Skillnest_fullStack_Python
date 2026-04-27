#Creación de clase usuario - entidad
class Usuario:
    def __init__(self, nombre, apellido, email, limite, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite
       self.saldo_pagar = saldo_pagar
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
#
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 30000, 0)

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

miyagi.hacer_compra(150)
miyagi.hacer_compra(300)
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45





class Estudiante:
    def __init__(self,rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.nacimiento = fecha_nac
        

daniel = Estudiante("1111111", "Daniel", "jimenez", "Programación" , 2008 )
juan = Estudiante("222222", "Juan", "Prevals", "Programación", 2008 )
akon = Estudiante("333333", "Akon", "Bustamante", "Programación", 2008 )


print(f"Hola soy {daniel.nombre} { daniel.apellido},  soy de la especialidad  de {daniel.especialidad}. ")
print(f"Hola soy {juan.nombre} {juan.apellido}, soy de la especialidad  de {juan.especialidad}. ")
print(f"Hola soy {akon.nombre} {akon.apellido}, soy de la especialidad  de {akon.especialidad}. ")
