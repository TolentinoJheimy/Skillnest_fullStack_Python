class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self):
        """Agrega un contenido a la lista de reproducción del usuario."""
        titulo = input(f"{self.nombre}, introduce el título que deseas agregar a tu lista de reproducción: ")
        self.lista_reproduccion.append(titulo)
        print(f"{titulo} agregado a la lista de {self.nombre}.")

    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        if titulo in self.lista_reproduccion:
            print(f"Reproduciendo: {titulo}")
        else:
            print(f"{titulo} no está en tu lista de reproducción.")

    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        self.suscripcion = nueva_suscripcion
        print(f"{self.nombre} ahora tiene suscripción {self.suscripcion}.")

    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        print(f"\nUsuario: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        print(f"Lista de Reproducción: {self.lista_reproduccion}")


def crear_usuario():
    """Crea un nuevo usuario a partir de los datos ingresados por el usuario."""
    nombre = input("Introduce el nombre del usuario: ")
    email = input("Introduce el email del usuario: ")
    suscripcion = input("Introduce el tipo de suscripción (Gratis, Estándar, Premium): ")
    return UsuarioStreaming(nombre, email, suscripcion)

usuarios = []

# Crear los 3 usuarios
print("\nCrear primer usuario")
usuario1 = crear_usuario()
usuarios.append(usuario1)

print("\nCrear segundo usuario")
usuario2 = crear_usuario()
usuarios.append(usuario2)

print("\nCrear tercer usuario")
usuario3 = crear_usuario()
usuarios.append(usuario3)

# Acciones de los usuarios 
# USER 1
print(f"\nAcciones de {usuario1.nombre}")
usuario1.agregar_a_lista()
usuario1.agregar_a_lista()
for titulo in usuario1.lista_reproduccion:
    usuario1.ver_contenido(titulo)
# USER 2
print(f"\nAcciones de {usuario2.nombre}")
usuario2.agregar_a_lista()
usuario2.ver_contenido(usuario2.lista_reproduccion[0])
nueva_suscripcion2 = input(f"{usuario2.nombre}, ingresa la nueva suscripción (Gratis, Estándar, Premium): ")
usuario2.cambiar_suscripcion(nueva_suscripcion2)
# USER 3
print(f"\nAcciones de {usuario3.nombre}")
usuario3.agregar_a_lista()
usuario3.agregar_a_lista()
usuario3.agregar_a_lista()
for titulo in usuario3.lista_reproduccion:
    usuario3.ver_contenido(titulo)
nueva_suscripcion3_1 = input(f"{usuario3.nombre}, ingresa la primera nueva suscripción (Gratis, Estándar, Premium): ")
usuario3.cambiar_suscripcion(nueva_suscripcion3_1)
nueva_suscripcion3_2 = input(f"{usuario3.nombre}, ingresa la segunda nueva suscripción (Gratis, Estándar, Premium): ")
usuario3.cambiar_suscripcion(nueva_suscripcion3_2)
print()
for u in usuarios:
    u.mostrar_info_usuario()
