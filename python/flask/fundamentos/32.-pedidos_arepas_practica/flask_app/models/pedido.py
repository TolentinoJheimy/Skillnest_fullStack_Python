# Importa la función flash para almacenar errores temporales en la sesión del usuario
from flask import flash

# Importa la función del archivo de configuración para interactuar con MySQL
from flask_app.config.mysqlconnection import connectToMySQL

class Pedido:
    """
    Modela la estructura de la tabla 'pedidos' y encapsula sus operaciones de datos.
    """
    def __init__(self, data):
        # Mapea cada columna de la base de datos a un atributo de la instancia
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo_arepa = data["tipo_arepa"]
        self.cantidad = data["cantidad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_pedido(pedido):
        """
        Analiza un diccionario de datos simulando el formulario y gatilla alertas si rompe reglas.
        """
        es_valido = True

        # Valida que el campo nombre no llegue vacío
        if not pedido["nombre"]:
            flash("El nombre es obligatorio.", "danger")
            es_valido = False
        # Valida la longitud mínima exigida por los requerimientos del negocio
        elif len(pedido["nombre"]) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "danger")
            es_valido = False

        # Valida que el campo tipo_arepa contenga texto
        if not pedido["tipo_arepa"]:
            flash("El tipo de arepa es obligatorio.", "danger")
            es_valido = False

        # Valida la existencia y el tipo numérico del campo cantidad
        if not pedido["cantidad"]:
            flash("La cantidad es obligatoria.", "danger")
            es_valido = False
        else:
            try:
                # Intenta transformar el texto del formulario a un entero puro
                cantidad = int(pedido["cantidad"])
                # Bloquea números negativos o compras en cero
                if cantidad <= 0:
                    flash("La cantidad debe ser mayor que 0.", "danger")
                    es_valido = False
            except ValueError:
                # Captura el error si el usuario ingresó letras en el campo numérico
                flash("La cantidad debe ser un número válido mayor que 0.", "danger")
                es_valido = False

        return es_valido

    @classmethod
    def get_all(cls):
        """
        Consulta la base de datos y exporta una lista de objetos tipo Pedido para la Vista.
        """
        query = """
            SELECT id, nombre, tipo_arepa, cantidad, created_at, updated_at
            FROM pedidos ORDER BY id DESC;
        """
        # Solicita la lista de diccionarios a la capa de configuración
        resultados = connectToMySQL("esquema_arepas").query_db(query)
        pedidos = []

        # Recorre cada diccionario y lo transforma en un objeto con la estructura de la clase
        for pedido in resultados:
            pedidos.append(cls(pedido))

        return pedidos

    @classmethod
    def save(cls, data):
        """
        Recibe un diccionario validado e inserta de forma segura el registro en la base de datos.
        """
        query = """
            INSERT INTO pedidos (nombre, tipo_arepa, cantidad)
            VALUES (%(nombre)s, %(tipo_arepa)s, %(cantidad)s);
        """
        # Ejecuta la sentencia armada y retorna el ID asignado al nuevo pedido
        return connectToMySQL("esquema_arepas").query_db(query, data)
