from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


@app.route("/estudiante")
def nuevo_estudiante():

    cursos = Curso.obtener_todos()

    return render_template(
        "nuevo_estudiante.html",
        cursos=cursos
    )


@app.route("/estudiante/crear", methods=["POST"])
def crear_estudiante():

    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "edad": request.form["edad"],
        "curso_id": request.form["curso_id"]
    }

    Estudiante.crear(datos)

    return redirect("/cursos")