import os

import pymysql


class MySQLConnection:
    def __init__(self, database=None):
        self.connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            database=(
                database or os.getenv("MYSQL_DATABASE", "inicio_sesion_registro")
            ),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data if data is not None else ())
                if cursor.description is not None:
                    return list(cursor.fetchall())

                self.connection.commit()
                if query.lstrip().split(None, 1)[0].upper() == "INSERT":
                    return cursor.lastrowid

                return cursor.rowcount
        except Exception:
            self.connection.rollback()
            raise
        finally:
            self.connection.close()


def connectToMySQL(database=None):
    return MySQLConnection(database)
