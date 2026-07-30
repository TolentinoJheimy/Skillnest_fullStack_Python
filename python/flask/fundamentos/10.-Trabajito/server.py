from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Bienvenido</h1>
    <a href="/videojuegos">Ir al listado de videojuegos</a>
    """

@app.route("/videojuegos")
def videojuegos():

    lista_videojuegos = [
        {
            "nombre": "Minecraft",
            "plataforma": "PC",
            "anio": 2011
        },
        {
            "nombre": "Valorant",
            "plataforma": "PC",
            "anio": 2020
        },
        {
            "nombre": "EA Sports FC 25",
            "plataforma": "PC / PS5 / Xbox",
            "anio": 2024
        },
        {
            "nombre": "God of War Ragnarök",
            "plataforma": "PlayStation 5",
            "anio": 2022
        },
        {
            "nombre": "The Legend of Zelda: Breath of the Wild",
            "plataforma": "Nintendo Switch",
            "anio": 2017
        },
        {
            "nombre": "Grand Theft Auto V",
            "plataforma": "PC / PlayStation / Xbox",
            "anio": 2013
        }
    ]

    return render_template(
        "videojuegos.html",
        videojuegos=lista_videojuegos
    )

if __name__ == "__main__":
    app.run(debug=True)