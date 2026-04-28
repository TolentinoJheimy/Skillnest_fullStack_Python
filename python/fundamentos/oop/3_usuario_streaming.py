class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
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
usuario = crear_usuario()
usuarios.append(usuario)
print(f"Usuario:{usuario.nombre}")


