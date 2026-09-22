from mysqlconnection import connectToMySQL

class Mascota:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Método para LEER (Read) todas las mascotas."""
        query = "SELECT * FROM mascotas;"
        results = connectToMySQL('primera_flask').query_db(query)
        mascotas = []
        for mascota in results:
            mascotas.append(cls(mascota))
        return mascotas

    @classmethod
    def save(cls, data):
        """Método para CREAR (Create) una nueva mascota."""
        query = """
            INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at)
            VALUES (%(nombre)s, %(tipo)s, %(color)s, NOW(), NOW());
        """
        return connectToMySQL('primera_flask').query_db(query, data)
