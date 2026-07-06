import mysql.connector


class Conexion:

    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="usuarios_db"
            )

            return self.conexion

        except mysql.connector.Error as e:
            print("Error de conexión:", e)
            return None

    def cerrar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()