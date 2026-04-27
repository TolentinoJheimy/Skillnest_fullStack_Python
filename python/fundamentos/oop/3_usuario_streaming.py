class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


   def agregar_a_lista(self, titulo):
       """Agrega un contenido a la lista de reproducción del usuario."""
       self.lista_reproduccion.append(titulo)


   def ver_contenido(self):
        """Simula que el usuario reproduce un contenido."""
        print(f"Lista de reproducción : \n {self.lista_reproduccion}")
        eleccion = input("Elige el contenido que deseas reproducir: ")
        if eleccion in self.lista_reproduccion:
            print(f"Reproduciendo: {eleccion} 🎬")
        else:
            print("Ese contenido no está en tu lista.")


   def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        self.suscripcion = nueva_suscripcion


   def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       print(f"User: {self.nombre} \n email: {self.email} \n Tipo de suscripcion: {self.suscripcion} \n Lista de Reproducción: {self.lista_reproduccion}")


user = UsuarioStreaming("Akon", "akonbustamante@liceovvh.cl", "Premium")
user.agregar_a_lista("pepino")
user.ver_contenido()