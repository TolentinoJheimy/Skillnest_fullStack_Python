# Importa el módulo para que los resultados de la base de datos se manejen como diccionarios de Python
import pymysql.cursors

class MySQLConnection:
    """
    Administra la conexión física y el envío de consultas entre Flask y MySQL.
    """
    def __init__(self, db):
        # Establece la conexión con el motor de base de datos local usando PyMySQL
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234", 
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """
        Ejecuta una consulta SQL genérica y maneja la respuesta según el tipo de comando.
        """
        with self.connection.cursor() as cursor:
            try:
                # Ejecuta la sentencia previniendo inyecciones SQL mediante sentencias preparadas
                cursor.execute(query, data)
                tipo_consulta = query.strip().lower()

                # Si es un SELECT, extrae y retorna todas las filas encontradas
                if tipo_consulta.startswith("select"):
                    return cursor.fetchall()

                # Si es un INSERT, retorna el ID numérico generado automáticamente
                if tipo_consulta.startswith("insert"):
                    return cursor.lastrowid

                # Si es UPDATE o DELETE, retorna la cantidad de filas que fueron modificadas
                return cursor.rowcount

            except Exception as e:
                # Imprime el error en la terminal en caso de falla sintáctica o de conexión
                print("Something went wrong:", e)
                return False

            finally:
                # Cierra la conexión de manera segura para liberar recursos del sistema
                self.connection.close()

def connectToMySQL(db):
    """
    Función constructora que exporta una nueva instancia de la clase de conexión.
    """
    return MySQLConnection(db)
