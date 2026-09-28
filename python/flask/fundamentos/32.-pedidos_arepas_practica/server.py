# Importa la instancia de la aplicación Flask desde el paquete flask_app
from flask_app import app

# Importa el controlador para registrar las rutas y funciones que responderán al usuario
from flask_app.controllers import pedidos

# Verifica si el archivo se ejecuta directamente para encender el servidor en modo desarrollo
if __name__ == "__main__":
    app.run(debug=True)
