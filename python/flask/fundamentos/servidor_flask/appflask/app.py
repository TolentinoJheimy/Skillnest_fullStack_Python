from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "🌎 ¡Bienvenido a nuestro servidor Flask!"

@app.route("/explorar")
def explora():
    return "🔍 ¿Qué ruta estás buscando? ¡Prueba con diferentes direcciones!"

@app.route("/perfil/<nombre>")
def saludo_nombre(nombre):
    return f"👤 Bienvenid@ {nombre} a tu perfil personalizado en nuestra app."

@app.route("/repite/<int:veces>/<palabra>")
def repetir(veces, palabra):
    return f"🔄 Repite después de mí: {' '.join([palabra] * veces)}"

@app.route("/loquesea")
def loquesea():
    return "⚠️ ¡Sobrecarga de rutas! No encontramos a dónde quieres ir, inténtalo de nuevo"

if __name__ == "__main__":
    app.run(debug=True)