import pymysql
import pymysql.cursors


class MySQLConnection:

    def __init__(self, database):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database=database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):

        with self.connection.cursor() as cursor:

            try:
                cursor.execute(query, data or {})

                tipo_consulta = query.strip().lower()

                if tipo_consulta.startswith("select"):
                    return cursor.fetchall()

                if tipo_consulta.startswith("insert"):
                    return cursor.lastrowid

                return cursor.rowcount

            except Exception as error:
                print(f"Error en la consulta: {error}")
                return False

            finally:
                self.connection.close()


def connectToMySQL(database):
    return MySQLConnection(database)