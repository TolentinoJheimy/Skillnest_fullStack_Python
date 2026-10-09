import os
import secrets
from pathlib import Path

import pymysql
from dotenv import load_dotenv
from flask import Flask, render_template, request, session

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.getenv("SECRET_KEY") or secrets.token_hex(32),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)


@app.before_request
def csrf_protection():
    session.setdefault("csrf_token", secrets.token_hex(32))

    if request.method == "POST" and not secrets.compare_digest(
        session["csrf_token"], request.form.get("csrf_token", "")
    ):
        return "Formulario vencido o inválido. Recarga la página.", 400


@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-store"
    return response


@app.errorhandler(pymysql.MySQLError)
def database_error(error):
    app.logger.error("Error MySQL: %s", type(error).__name__)
    return render_template("database_error.html"), 503


from flask_app.controllers import controlador_usuarios
