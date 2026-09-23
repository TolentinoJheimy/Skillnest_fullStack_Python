from flask import render_template, request, redirect, url_for

from flask_app import app
from flask_app.models.usuario import Usuario


@app.route("/")
def inicio():
    return redirect(url_for("mostrar_usuarios"))


@app.route("/usuarios")
def mostrar_usuarios():

    usuarios = Usuario.obtener_todos()

    return render_template(
        "index.html",
        usuarios=usuarios
    )


@app.route("/usuarios/nuevo")
def formulario_nuevo():

    return render_template("nuevo.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():

    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip()
    }

    if not all(datos.values()):
        return render_template(
            "nuevo.html",
            error="Debes completar todos los campos.",
            datos=datos
        )

    resultado = Usuario.crear(datos)

    if resultado is False:
        return render_template(
            "nuevo.html",
            error="Ocurrió un problema al guardar el usuario.",
            datos=datos
        )

    return redirect(url_for("mostrar_usuarios"))


@app.route("/usuarios/<int:id>")
def mostrar_usuario(id):

    usuario = Usuario.buscar_por_id(id)

    if usuario is None:
        return "El usuario solicitado no existe.", 404

    return render_template(
        "detalle.html",
        usuario=usuario
    )


@app.route("/usuarios/editar/<int:id>")
def formulario_edicion(id):

    usuario = Usuario.buscar_por_id(id)

    if usuario is None:
        return "El usuario solicitado no existe.", 404

    return render_template(
        "editar.html",
        usuario=usuario
    )


@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar_usuario(id):

    datos = {
        "id": id,
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip()
    }

    if not all([
        datos["nombre"],
        datos["apellido"],
        datos["email"]
    ]):
        usuario = Usuario.buscar_por_id(id)

        return render_template(
            "editar.html",
            usuario=usuario,
            error="Todos los campos son obligatorios."
        )

    resultado = Usuario.modificar(datos)

    if resultado is False:
        usuario = Usuario.buscar_por_id(id)

        return render_template(
            "editar.html",
            usuario=usuario,
            error="No se pudo actualizar el usuario."
        )

    return redirect(url_for("mostrar_usuarios"))


@app.route("/usuarios/borrar/<int:id>")
def eliminar_usuario(id):

    resultado = Usuario.eliminar(id)

    if resultado is False:
        return "No se pudo eliminar el usuario.", 500

    return redirect(url_for("mostrar_usuarios"))