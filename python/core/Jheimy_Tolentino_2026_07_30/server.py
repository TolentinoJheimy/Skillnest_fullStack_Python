from flask import Flask, render_template

app = Flask(__name__)

# ============================
# Base de datos ficticia
# ============================

datos = [
    {
        "id": 1,
        "nombre": "Discord",
        "usuarios": "250M",
        "fundado": 2015,
        "pais": "EE.UU.",
        "icono": "bi-discord",
        "color": "#5865F2",
        "descripcion": "Plataforma de comunicación para comunidades y videojuegos."
    },
    {
        "id": 2,
        "nombre": "Instagram",
        "usuarios": "2.35B",
        "fundado": 2010,
        "pais": "EE.UU.",
        "icono": "bi-instagram",
        "color": "#E4405F",
        "descripcion": "Red social para compartir fotografías y videos."
    },
    {
        "id": 3,
        "nombre": "Netflix",
        "usuarios": "247M",
        "fundado": 1997,
        "pais": "EE.UU.",
        "icono": "bi-film",
        "color": "#E50914",
        "descripcion": "Servicio de streaming de películas y series."
    },
    {
        "id": 4,
        "nombre": "Spotify",
        "usuarios": "515M",
        "fundado": 2006,
        "pais": "Suecia",
        "icono": "bi-spotify",
        "color": "#1DB954",
        "descripcion": "Servicio de música y podcasts en streaming."
    },
    {
        "id": 5,
        "nombre": "TikTok",
        "usuarios": "1.7B",
        "fundado": 2016,
        "pais": "China",
        "icono": "bi-tiktok",
        "color": "#000000",
        "descripcion": "Plataforma de videos cortos."
    },
    {
        "id": 6,
        "nombre": "Twitch",
        "usuarios": "140M",
        "fundado": 2011,
        "pais": "EE.UU.",
        "icono": "bi-twitch",
        "color": "#9146FF",
        "descripcion": "Plataforma de transmisiones en vivo."
    },
    {
        "id": 7,
        "nombre": "YouTube",
        "usuarios": "2.5B",
        "fundado": 2005,
        "pais": "EE.UU.",
        "icono": "bi-youtube",
        "color": "#FF0000",
        "descripcion": "La plataforma de videos más utilizada del mundo."
    }
]

# ============================
# Ruta principal
# ============================

@app.route("/")
def inicio():
    return render_template(
        "tabla.html",
        datos=datos,
        total=len(datos)
    )

# ============================
# Ruta de la práctica
# ============================

@app.route("/tabla")
def tabla():
    return render_template(
        "tabla.html",
        datos=datos,
        total=len(datos)
    )

# ============================
# Página de detalle
# ============================

@app.route("/detalle/<int:id>")
def detalle(id):

    plataforma = next(
        (p for p in datos if p["id"] == id),
        None
    )

    return render_template(
        "detalle.html",
        plataforma=plataforma
    )

# ============================
# Ejecutar servidor
# ============================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )