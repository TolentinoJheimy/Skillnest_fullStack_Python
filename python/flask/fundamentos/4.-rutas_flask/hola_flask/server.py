from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola Mundo!"

@app.route("/exito")
def exito():
    return "¡Éxito!"

@app.route("/exito/<nombre>")
def saludar(nombre):
    return f"<h1>Hola {nombre}, Como te encuentras?"

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):

    return f"Hola {nombre}, tu color favorito es {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):

    return f"¡Hola {nombre}!" * veces

@app.route("/despedir/<nombre>")
def despedir(nombre):
    return f"<h1>Hola {nombre}, que te vaya muy bien, adios!"

@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):
    return f"<h1>Hola {nombre}, tienes {edad} años."


if __name__ == "__main__":
    app.run(debug=True)