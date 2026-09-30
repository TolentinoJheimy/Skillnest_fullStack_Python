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
                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid

                return True

            except Exception as error:
                print("Something went wrong", error)
                return False