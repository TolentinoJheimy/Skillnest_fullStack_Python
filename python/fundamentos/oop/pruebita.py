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
        antiguaSus = self.suscripcion
        self.suscripcion = nueva_suscripcion
        print(f"{self.nombre} tenia suscripción {antiguaSus} ahora tiene suscripción {self.suscripcion}.")

    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        print(f"\nUsuario: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        if len(self.lista_reproduccion) == 0:
            print("La lista de reproducción esta vacia.")
        else:
            print(f"Lista de reproducción: \n- {"\n- ".join(self.lista_reproduccion)}")
        

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
titulo1_1 = input(f"{usuario1.nombre}, introduce el primer título que deseas agregar a tu lista de reproducción: ")
titulo1_2 = input(f"{usuario1.nombre}, introduce el segundo título que deseas agregar a tu lista de reproducción: ")
usuario1.agregar_a_lista(titulo1_1)
usuario1.agregar_a_lista(titulo1_2)
for titulo in usuario1.lista_reproduccion:
    usuario1.ver_contenido(titulo)
# USER 2
print(f"\nAcciones de {usuario2.nombre}")
titulo2_1 = input(f"{usuario2.nombre}, introduce el título que deseas agregar a tu lista de reproducción: ")
usuario2.agregar_a_lista(titulo2_1)
usuario2.ver_contenido(usuario2.lista_reproduccion[0])
nueva_suscripcion2 = input(f"{usuario2.nombre}, ingresa la nueva suscripción (Gratis, Estándar, Premium): ")
usuario2.cambiar_suscripcion(nueva_suscripcion2)
# USER 3
print(f"\nAcciones de {usuario3.nombre}")
titulo3_1 = input(f"{usuario3.nombre}, introduce el primer título que deseas agregar a tu lista de reproducción: ")
titulo3_2 = input(f"{usuario3.nombre}, introduce el segundo título que deseas agregar a tu lista de reproducción: ")
titulo3_3 = input(f"{usuario3.nombre}, introduce el primer título que deseas agregar a tu lista de reproducción: ")
usuario3.agregar_a_lista(titulo3_1)
usuario3.agregar_a_lista(titulo3_2)
usuario3.agregar_a_lista(titulo3_3)
for titulo in usuario3.lista_reproduccion:
    usuario3.ver_contenido(titulo)
nueva_suscripcion3_1 = input(f"{usuario3.nombre}, ingresa la primera nueva suscripción (Gratis, Estándar, Premium): ")
usuario3.cambiar_suscripcion(nueva_suscripcion3_1)
nueva_suscripcion3_2 = input(f"{usuario3.nombre}, ingresa la segunda nueva suscripción (Gratis, Estándar, Premium): ")
usuario3.cambiar_suscripcion(nueva_suscripcion3_2)
print()
for u in usuarios:
    u.mostrar_info_usuario()
