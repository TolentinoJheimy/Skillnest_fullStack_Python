from flask import render_template, redirect, request, url_for
from flask_app import app
from flask_app.models.taco import Taco

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tacos/crear', methods=['POST'])
def crear_taco():
    Taco.save(request.form)
    return redirect(url_for('resultados'))

@app.route('/tacos')
def resultados():
    return render_template('resultados.html', todos_tacos=Taco.get_all())

@app.route('/tacos/<int:id>')
def detalle(id):
    data = {"id": id}
    return render_template('detalle.html', taco=Taco.get_one(data))

@app.route('/tacos/<int:id>/editar')
def editar(id):
    data = {"id": id}
    return render_template('editar.html', taco=Taco.get_one(data))

@app.route('/tacos/actualizar', methods=['POST'])
def actualizar():
    Taco.update(request.form)
    return redirect(url_for('resultados'))

@app.route('/tacos/<int:id>/eliminar')
def eliminar(id):
    data = {"id": id}
    Taco.delete(data)
    return redirect(url_for('resultados'))
