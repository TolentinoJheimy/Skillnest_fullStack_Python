from datetime import date

import pymysql
from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

from flask_app import app
from flask_app.models.modelo_usuario import Usuario


@app.get("/")
def index():
    today = date.today()

    try:
        max_birthdate = today.replace(year=today.year - 18)
    except ValueError:
        max_birthdate = today.replace(year=today.year - 18, day=28)

    return render_template(
        "index.html",
        form=session.pop("registro_form", {}),
        max_birthdate=max_birthdate.isoformat(),
    )


@app.post("/registro")
def register():
    data = request.form
    session["registro_form"] = {
        key: data.get(key, "")[:254]
        for key in ("nombre", "apellido", "email", "fecha_nacimiento", "interes")
    }

    errors = Usuario.validar_registro(data)
    if errors:
        for error in errors:
            flash(error, "registro_error")
        return redirect(url_for("index"))

    try:
        if Usuario.obtener_por_email(data["email"]):
            flash("Este correo ya está registrado.", "registro_error")
            return redirect(url_for("index"))

        user_id = Usuario.crear(data)
    except pymysql.err.IntegrityError as error:
        if error.args[0] != 1062:
            raise

        flash("Este correo ya está registrado.", "registro_error")
        return redirect(url_for("index"))

    session.clear()
    session["user_id"] = user_id
    flash("Registro exitoso. Tu cuenta ha sido creada.", "success")
    return redirect(url_for("success"))


@app.post("/login")
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    user = Usuario.obtener_por_email(email) if email and password else None

    if not user or not check_password_hash(user["password_hash"], password):
        flash("Correo o contraseña incorrectos.", "login_error")
        return redirect(url_for("index"))

    session.clear()
    session["user_id"] = user["id"]
    return redirect(url_for("success"))


@app.get("/exito")
def success():
    if "user_id" not in session:
        return redirect(url_for("index"))

    user = Usuario.obtener_por_id(session["user_id"])
    if not user:
        session.clear()
        return redirect(url_for("index"))

    return render_template("success.html", user=user)


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
