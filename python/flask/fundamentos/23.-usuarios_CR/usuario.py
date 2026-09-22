from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Obtiene todos los usuarios de la base de datos."""
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        usuarios = []
        for u in results:
            usuarios.append(cls(u))
        return usuarios

    @classmethod
    def save(cls, data):
        """Guarda un nuevo usuario en la base de datos."""
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL('esquema_usuarios').query_db(query, data)
