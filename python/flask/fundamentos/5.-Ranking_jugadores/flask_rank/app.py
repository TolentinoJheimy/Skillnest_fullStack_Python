from flask import Flask, render_template

app = Flask(__name__)

# Datos de jugadores con puntajes
jugadores = [
    {"nombre": "AlexGamer", "puntaje": 5000},
    {"nombre": "PixelMaster", "puntaje": 7500},
    {"nombre": "ShadowNinja", "puntaje": 8200},
    {"nombre": "CyberWarrior", "puntaje": 9100},
    {"nombre": "UltraNoob", "puntaje": 3000}
]

# Ordenar de mayor a menor puntaje
jugadores = sorted(jugadores, key=lambda x: x["puntaje"], reverse=True)


# Ruta para mostrar el ranking completo
@app.route("/ranking")
def ranking():
    return render_template("ranking.html", jugadores=jugadores, color=None)


# Ruta para mostrar un número limitado de jugadores
@app.route("/ranking/<int:cantidad>")
def ranking_cantidad(cantidad):
    return render_template(
        "ranking.html",
        jugadores=jugadores[:cantidad],
        color=None
    )


# Ruta para personalizar el color del ranking
@app.route("/ranking/<int:cantidad>/<color>")
def ranking_color(cantidad, color):
    return render_template(
        "ranking.html",
        jugadores=jugadores[:cantidad],
        color=color
    )


# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)