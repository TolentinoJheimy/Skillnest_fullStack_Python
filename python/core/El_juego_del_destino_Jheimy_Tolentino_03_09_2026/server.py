from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

# Mensajes de predicción principal (positivos y de mala suerte)
MENSAJES_POSITIVOS = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Grandes oportunidades vienen en camino. El universo conspira a tu favor.",
    "Tu esfuerzo dará frutos muy pronto. ¡Prepárate para el éxito!",
    "Las estrellas se alinean para ti. Un nuevo comienzo lleno de fortuna te espera.",
    "Alguien especial entrará en tu vida y te traerá mucha felicidad.",
    "Tu suerte está cambiando. ¡Este es tu momento para brillar!",
]

MENSAJES_NEGATIVOS = [
    "Ten cuidado con las decisiones apresuradas en los próximos días.",
    "El camino se ve algo nublado. Es momento de tener paciencia.",
    "Podrías enfrentar un pequeño obstáculo, pero lo superarás con esfuerzo.",
    "Las energías no están muy favorables hoy. Mejor evita riesgos innecesarios.",
    "Algo no saldrá como lo planeaste, pero será una gran lección.",
]

# Significados asociados a colores favoritos
SIGNIFICADO_COLORES = {
    "rojo": ("pasión", "energía"),
    "azul": ("calma", "sabiduría"),
    "verde": ("misterio", "descubrimiento"),
    "morado": ("espiritualidad", "intuición"),
    "violeta": ("espiritualidad", "intuición"),
    "amarillo": ("alegría", "optimismo"),
    "naranja": ("creatividad", "entusiasmo"),
    "negro": ("poder", "elegancia"),
    "blanco": ("pureza", "claridad"),
    "rosa": ("amor", "ternura"),
    "gris": ("equilibrio", "neutralidad"),
    "celeste": ("serenidad", "libertad"),
    "dorado": ("abundancia", "prestigio"),
    "plateado": ("intuición", "refinamiento"),
    "café": ("estabilidad", "cercanía"),
    "marrón": ("estabilidad", "cercanía"),
    "turquesa": ("equilibrio", "renovación"),
}

# Pares de significado por defecto cuando el color/animal no está en el diccionario
SIGNIFICADOS_GENERICOS = [
    ("originalidad", "misterio"),
    ("sensibilidad", "creatividad"),
    ("fuerza", "determinación"),
    ("curiosidad", "aventura"),
]

# Hex aproximado para pintar la muestra de color
HEX_COLORES = {
    "rojo": "#e11d48",
    "azul": "#2563eb",
    "verde": "#16a34a",
    "morado": "#7c3aed",
    "violeta": "#7c3aed",
    "amarillo": "#eab308",
    "naranja": "#ea580c",
    "negro": "#111827",
    "blanco": "#e5e7eb",
    "rosa": "#ec4899",
    "gris": "#6b7280",
    "celeste": "#38bdf8",
    "dorado": "#d4af37",
    "plateado": "#c0c0c0",
    "café": "#78350f",
    "marrón": "#78350f",
    "turquesa": "#14b8a6",
}

# Significados asociados a animales favoritos
SIGNIFICADO_ANIMALES = {
    "perro": ("lealtad", "compañerismo"),
    "gato": ("independencia", "misterio"),
    "águila": ("visión", "libertad"),
    "aguila": ("visión", "libertad"),
    "león": ("valentía", "liderazgo"),
    "leon": ("valentía", "liderazgo"),
    "delfín": ("inteligencia", "alegría"),
    "delfin": ("inteligencia", "alegría"),
    "lobo": ("instinto", "lealtad"),
    "búho": ("sabiduría", "percepción"),
    "buho": ("sabiduría", "percepción"),
    "tortuga": ("paciencia", "longevidad"),
    "mariposa": ("transformación", "delicadeza"),
    "tigre": ("poder", "coraje"),
    "conejo": ("suerte", "sensibilidad"),
    "caballo": ("libertad", "nobleza"),
    "zorro": ("astucia", "adaptabilidad"),
    "oso": ("fuerza", "protección"),
}


def obtener_significado(valor, diccionario):
    """Devuelve un par (rasgo1, rasgo2) para el color o animal ingresado."""
    clave = valor.strip().lower()
    if clave in diccionario:
        return diccionario[clave]
    return random.choice(SIGNIFICADOS_GENERICOS)


def obtener_mensaje_edad(edad_str):
    """Genera un mensaje de predicción según el rango de edad."""
    try:
        edad = int(edad_str)
    except (ValueError, TypeError):
        return "Tu momento ideal está por llegar, sin importar el tiempo que tome."

    if edad < 18:
        return f"A tus {edad} años, tienes por delante un camino lleno de aprendizajes y descubrimientos."
    elif edad <= 25:
        return f"A tus {edad} años, estás en un momento favorable para aprovechar nuevas oportunidades."
    elif edad <= 40:
        return f"A tus {edad} años, tu experiencia y energía se combinan para abrirte grandes puertas."
    elif edad <= 60:
        return f"A tus {edad} años, la sabiduría acumulada te guiará hacia decisiones acertadas."
    else:
        return f"A tus {edad} años, la calma y la experiencia son tu mayor tesoro para lo que viene."


# Ruta principal que muestra el formulario para ingresar datos
@app.route("/")
def index():
    return render_template("index.html")


# Ruta para procesar los datos del formulario y almacenarlos en sesión
@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre", "").strip()
    edad = request.form.get("edad", "").strip()
    color = request.form.get("color", "").strip()
    animal = request.form.get("animal", "").strip()

    # Guardamos los datos del usuario en la sesión
    session["nombre"] = nombre if nombre else "Viajero"
    session["edad"] = edad
    session["color"] = color if color else "morado"
    session["animal"] = animal if animal else "gato"

    return redirect("/futuro")


# Ruta para mostrar la predicción del futuro basada en los datos ingresados
@app.route("/futuro")
def futuro():
    nombre = session.get("nombre", "Viajero")
    edad = session.get("edad", "")
    color = session.get("color", "morado")
    animal = session.get("animal", "gato")

    # Selección aleatoria entre mensaje positivo o de mala suerte
    if random.choice([True, False]):
        mensaje = random.choice(MENSAJES_POSITIVOS)
        tipo = "positivo"
    else:
        mensaje = random.choice(MENSAJES_NEGATIVOS)
        tipo = "negativo"

    rasgo_color_1, rasgo_color_2 = obtener_significado(color, SIGNIFICADO_COLORES)
    rasgo_animal_1, rasgo_animal_2 = obtener_significado(animal, SIGNIFICADO_ANIMALES)
    color_hex = HEX_COLORES.get(color.strip().lower(), "#7c3aed")
    numero_suerte = random.randint(1, 99)
    mensaje_edad = obtener_mensaje_edad(edad)

    return render_template(
        "futuro.html",
        nombre=nombre,
        edad=edad,
        color=color,
        animal=animal,
        color_hex=color_hex,
        rasgo_color_1=rasgo_color_1,
        rasgo_color_2=rasgo_color_2,
        rasgo_animal_1=rasgo_animal_1,
        rasgo_animal_2=rasgo_animal_2,
        numero_suerte=numero_suerte,
        mensaje_edad=mensaje_edad,
        mensaje=mensaje,
        tipo=tipo,
    )


if __name__ == "__main__":
    app.run(debug=True)
