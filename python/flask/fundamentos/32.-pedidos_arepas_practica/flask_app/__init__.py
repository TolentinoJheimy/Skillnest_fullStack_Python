# Importa la clase Flask para poder instanciar la aplicación web
from flask import Flask

# Crea la instancia global de la aplicación que usarán los controladores
app = Flask(__name__)

# Configura la clave secreta obligatoria para encriptar la sesión y usar mensajes flash()
app.secret_key = "clave-secreta-desarrollo"
