from flask import Flask, render_template, request

app = Flask(__name__)

# ==========================
# Base de datos ficticia
# ==========================

frutas = [
    {
        "nombre": "Manzana",
        "precio": 2.5,
        "imagen": "manzana.png",
        "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C."
    },
    {
        "nombre": "Plátano",
        "precio": 1.8,
        "imagen": "platano.png",
        "descripcion": "Fruta energética rica en potasio, perfecta para deportistas."
    },
    {
        "nombre": "Naranja",
        "precio": 3.0,
        "imagen": "naranja.png",
        "descripcion": "Cítrico jugoso con alto contenido de vitamina C."
    },
    {
        "nombre": "Fresa",
        "precio": 4.5,
        "imagen": "fresa.png",
        "descripcion": "Baya dulce y aromática rica en antioxidantes."
    },
    {
        "nombre": "Uva",
        "precio": 3.8,
        "imagen": "uva.png",
        "descripcion": "Pequeña, dulce y perfecta para snacks."
    },
    {
        "nombre": "Piña",
        "precio": 5.0,
        "imagen": "pina.png",
        "descripcion": "Fruta tropical dulce con propiedades digestivas."
    },
    {
        "nombre": "Sandía",
        "precio": 4.2,
        "imagen": "sandia.png",
        "descripcion": "Muy refrescante y rica en agua."
    },
    {
        "nombre": "Mango",
        "precio": 3.5,
        "imagen": "mango.png",
        "descripcion": "Fruta tropical rica en vitaminas A y C."
    }
]

# ==========================
# Página principal
# ==========================

@app.route("/")
def index():
    return render_template(
        "index.html",
        frutas=frutas
    )


# ==========================
# Catálogo
# ==========================

@app.route("/frutas")
def catalogo():
    return render_template(
        "frutas.html",
        frutas=frutas
    )


# ==========================
# Checkout
# ==========================

@app.route("/checkout", methods=["POST"])
def checkout():

    nombre = request.form["nombre"]
    email = request.form["email"]
    direccion = request.form["direccion"]

    pedido = []
    total = 0
    total_frutas = 0

    for fruta in frutas:

        cantidad = int(request.form.get(fruta["nombre"], 0))

        if cantidad > 0:

            subtotal = cantidad * fruta["precio"]

            pedido.append({
                "nombre": fruta["nombre"],
                "precio": fruta["precio"],
                "cantidad": cantidad,
                "subtotal": subtotal,
                "imagen": fruta["imagen"]
            })

            total += subtotal
            total_frutas += cantidad

    return render_template(
        "checkout.html",
        nombre=nombre,
        email=email,
        direccion=direccion,
        pedido=pedido,
        total=total,
        total_frutas=total_frutas
    )


if __name__ == "__main__":
    app.run(debug=True)