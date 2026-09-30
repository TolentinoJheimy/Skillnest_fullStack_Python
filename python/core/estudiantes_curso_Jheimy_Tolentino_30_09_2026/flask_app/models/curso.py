from flask_app.config.mysqlconnection import MySQLConnection


class Curso:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def obtener_todos(cls):
        query = """
            SELECT *
            FROM cursos
            ORDER BY nombre ASC;
        """

        resultados = MySQLConnection(
            "esquema_estudiantes_cursos"
        ).query_db(query)

        cursos = []

        for curso in resultados:
            cursos.append(cls(curso))

        return cursos

    @classmethod
    def crear(cls, data):
        query = """
            INSERT INTO cursos (nombre)
            VALUES (%(nombre)s);
        """

        return MySQLConnection(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

    @classmethod
    def obtener_uno(cls, curso_id):
        query = """
            SELECT *
            FROM cursos
            WHERE id = %(id)s;
        """

        data = {
            "id": curso_id
        }

        resultado = MySQLConnection(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None