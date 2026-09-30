from flask_app.config.mysqlconnection import MySQLConnection


class Estudiante:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.curso_id = data["curso_id"]

    @classmethod
    def crear(cls, data):
        query = """
            INSERT INTO estudiantes
                (nombre, apellido, edad, curso_id)
            VALUES
                (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);
        """

        return MySQLConnection(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

    @classmethod
    def obtener_por_curso(cls, curso_id):
        query = """
            SELECT *
            FROM estudiantes
            WHERE curso_id = %(curso_id)s
            ORDER BY nombre ASC;
        """

        data = {
            "curso_id": curso_id
        }

        resultados = MySQLConnection(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

        estudiantes = []

        for estudiante in resultados:
            estudiantes.append(cls(estudiante))

        return estudiantes