from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


@app.route("/")
def inicio():
    return redirect("/cursos")


@app.route("/cursos")
def cursos():
    todos_los_cursos = Curso.obtener_todos()

    return render_template(
        "cursos.html",
        cursos=todos_los_cursos
    )


@app.route("/cursos/crear", methods=["POST"])
def crear_curso():

    datos = {
        "nombre": request.form["nombre"]
    }

    Curso.crear(datos)

    return redirect("/cursos")


@app.route("/cursos/<int:curso_id>")
def mostrar_curso(curso_id):

    curso = Curso.obtener_uno(curso_id)

    estudiantes = Estudiante.obtener_por_curso(curso_id)

    return render_template(
        "mostrar_curso.html",
        curso=curso,
        estudiantes=estudiantes
    )