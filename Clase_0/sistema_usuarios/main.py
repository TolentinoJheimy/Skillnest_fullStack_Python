from usuario import Usuario


def menu_admin(nombre):

    while True:

        print("\n==============================")
        print(f"Bienvenido Administrador: {nombre}")
        print("==============================")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            usuario = input("Usuario: ")
            password = input("Contraseña: ")

            print("\nTipos")
            print("1. ADMIN")
            print("2. USER")

            tipo = int(input("Seleccione tipo: "))

            nuevo = Usuario(
                usuario=usuario,
                password=password,
                tipo=tipo
            )

            nuevo.crear_usuario()

        elif opcion == "2":

            Usuario().listar_usuarios()

        elif opcion == "3":

            id_buscar = int(input("ID: "))

            datos = Usuario().buscar_usuario(id_buscar)

            if datos:

                print("\nUsuario encontrado")
                print("ID:", datos["id"])
                print("Usuario:", datos["usuario"])
                print("Password:", datos["password"])
                print("Tipo:", datos["tipo"])

            else:

                print("No existe.")

        elif opcion == "4":

            id_modificar = int(input("ID: "))

            datos = Usuario().buscar_usuario(id_modificar)

            if datos is None:

                print("Usuario no encontrado.")
                continue

            usuario = input("Nuevo usuario: ")
            password = input("Nueva contraseña: ")

            print("1.ADMIN")
            print("2.USER")

            tipo = int(input("Nuevo tipo: "))

            Usuario(
                id=id_modificar,
                usuario=usuario,
                password=password,
                tipo=tipo
            ).modificar_usuario()

        elif opcion == "5":

            id_eliminar = int(input("ID a eliminar: "))

            confirmar = input("¿Seguro? (S/N): ")

            if confirmar.upper() == "S":

                Usuario().eliminar_usuario(id_eliminar)

        elif opcion == "6":

            print("Sesión cerrada.")
            break

        else:

            print("Opción inválida.")


def menu_user(nombre):

    while True:

        print("\n========================")
        print("Bienvenido", nombre)
        print("Tipo de usuario: USER")
        print("========================")
        print("1. Cerrar sesión")

        opcion = input("Seleccione: ")

        if opcion == "1":

            break


def login():

    while True:

        print("\n==========================")
        print("SISTEMA DE USUARIOS")
        print("==========================")
        print("1. Iniciar sesión")
        print("2. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":

            usuario = input("Usuario: ")
            password = input("Contraseña: ")

            datos = Usuario(
                usuario=usuario,
                password=password
            ).login()

            if datos:

                if datos["tipo"] == "ADMIN":

                    menu_admin(datos["usuario"])

                else:

                    menu_user(datos["usuario"])

            else:

                print("Usuario o contraseña incorrectos.")

        elif opcion == "2":

            print("Hasta luego.")
            break

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    login()