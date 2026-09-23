from flask import Flask, render_template, request, redirect, url_for
from estudiante import Estudiante

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('estudiantes'))

@app.route('/estudiantes')
def estudiantes():
    return render_template('estudiantes.html', todos_estudiantes=Estudiante.get_all())

@app.route('/estudiantes/<int:id_estudiante>')
def mostrar_estudiante(id_estudiante):
    data = {"id_estudiante": id_estudiante}
    return render_template('estudiante_ver.html', estudiante=Estudiante.get_one(data))

@app.route('/estudiantes/<int:id_estudiante>/editar')
def editar_estudiante(id_estudiante):
    data = {"id_estudiante": id_estudiante}
    return render_template('estudiante_editar.html', estudiante=Estudiante.get_one(data))

@app.route('/estudiantes/actualizar', methods=['POST'])
def actualizar_estudiante():
    Estudiante.update(request.form)
    return redirect(url_for('estudiantes'))

@app.route('/estudiantes/<int:id_estudiante>/eliminar')
def eliminar_estudiante(id_estudiante):
    data = {"id_estudiante": id_estudiante}
    Estudiante.delete(data)
    return redirect(url_for('estudiantes'))

if __name__ == "__main__":
    app.run(debug=True)
