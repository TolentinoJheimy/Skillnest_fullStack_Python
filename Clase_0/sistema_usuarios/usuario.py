from conexion import Conexion


class Usuario:

    def __init__(self, id=None, usuario=None, password=None, tipo=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo = tipo

    # ---------------- CREAR ---------------- #

    def crear_usuario(self):

        conexion = Conexion()
        db = conexion.conectar()

        try:

            cursor = db.cursor(dictionary=True)

            sql = """
            INSERT INTO usuarios(usuario,password,tipo_usuario)
            VALUES(%s,%s,%s)
            """

            cursor.execute(sql, (
                self.usuario,
                self.password,
                self.tipo
            ))

            db.commit()

            print("Usuario registrado correctamente.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conexion.cerrar()

    # ---------------- LISTAR ---------------- #

    def listar_usuarios(self):

        conexion = Conexion()
        db = conexion.conectar()

        try:

            cursor = db.cursor(dictionary=True)

            sql = """
            SELECT u.id,
                   u.usuario,
                   t.nombre AS tipo
            FROM usuarios u
            INNER JOIN tipo_usuario t
            ON u.tipo_usuario=t.id
            ORDER BY u.id
            """

            cursor.execute(sql)

            datos = cursor.fetchall()

            print("\n------ LISTADO ------")

            for fila in datos:
                print(f"{fila['id']} | {fila['usuario']} | {fila['tipo']}")

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conexion.cerrar()

    # ---------------- BUSCAR ---------------- #

    def buscar_usuario(self, id):

        conexion = Conexion()
        db = conexion.conectar()

        try:

            cursor = db.cursor(dictionary=True)

            sql = """
            SELECT u.id,
                   u.usuario,
                   u.password,
                   t.nombre AS tipo
            FROM usuarios u
            INNER JOIN tipo_usuario t
            ON u.tipo_usuario=t.id
            WHERE u.id=%s
            """

            cursor.execute(sql, (id,))

            return cursor.fetchone()

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conexion.cerrar()

    # ---------------- MODIFICAR ---------------- #

    def modificar_usuario(self):

        conexion = Conexion()
        db = conexion.conectar()

        try:

            cursor = db.cursor(dictionary=True)

            sql = """
            UPDATE usuarios
            SET usuario=%s,
                password=%s,
                tipo_usuario=%s
            WHERE id=%s
            """

            cursor.execute(sql, (
                self.usuario,
                self.password,
                self.tipo,
                self.id
            ))

            db.commit()

            print("Usuario actualizado correctamente.")

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conexion.cerrar()

    # ---------------- ELIMINAR ---------------- #

    def eliminar_usuario(self, id):

        conexion = Conexion()
        db = conexion.conectar()

        try:

            cursor = db.cursor(dictionary=True)

            sql = "DELETE FROM usuarios WHERE id=%s"

            cursor.execute(sql, (id,))

            db.commit()

            print("Usuario eliminado correctamente.")

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conexion.cerrar()

    # ---------------- LOGIN ---------------- #

    def login(self):

        conexion = Conexion()
        db = conexion.conectar()

        try:

            cursor = db.cursor(dictionary=True)

            sql = """
            SELECT u.id,
                   u.usuario,
                   t.nombre AS tipo
            FROM usuarios u
            INNER JOIN tipo_usuario t
            ON u.tipo_usuario=t.id
            WHERE u.usuario=%s
            AND u.password=%s
            """

            cursor.execute(sql, (
                self.usuario,
                self.password
            ))

            return cursor.fetchone()

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conexion.cerrar()