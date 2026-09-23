from mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT id_estudiante, nombre, email, created_at FROM estudiantes ORDER BY id_estudiante;"
        resultados = connectToMySQL().query_db(query)
        estudiantes = []
        for estudiante in resultados:
            estudiantes.append(cls(estudiante))
        return estudiantes

    @classmethod
    def get_one(cls, data):
        query = "SELECT id_estudiante, nombre, email, created_at FROM estudiantes WHERE id_estudiante = %(id_estudiante)s;"
        resultados = connectToMySQL().query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def update(cls, data):
        query = "UPDATE estudiantes SET nombre = %(nombre)s, email = %(email)s WHERE id_estudiante = %(id_estudiante)s;"
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM estudiantes WHERE id_estudiante = %(id_estudiante)s;"
        return connectToMySQL().query_db(query, data)
