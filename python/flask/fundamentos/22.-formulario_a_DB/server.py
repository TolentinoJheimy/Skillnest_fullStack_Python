from flask import Flask, render_template, request, redirect
from mascota import Mascota

app = Flask(__name__)

@app.route('/')
def index():
    # Obtiene todas las mascotas de la base de datos
    todas_las_mascotas = Mascota.get_all()
    return render_template('index.html', mascotas=todas_las_mascotas)

@app.route('/crear_mascota', methods=['POST'])
def crear_mascota():
    # Estructura el diccionario con los datos del formulario
    datos = {
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "color": request.form["color"]
    }
    # Guarda el registro en MySQL
    Mascota.save(datos)
    # Redirige de vuelta a la raíz (Patrón POST -> Redirect -> GET)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
