import os
import re
from datetime import date

from werkzeug.security import generate_password_hash

from flask_app.config.mysql_connection import connectToMySQL

INTERESES = ("Python", "Desarrollo web", "Bases de datos")


class Usuario:
    @classmethod
    def obtener_por_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %s"
        results = connectToMySQL(
            os.getenv("MYSQL_DATABASE", "inicio_sesion_registro")
        ).query_db(query, (email.strip().lower(),))

        return results[0] if results else None

    @classmethod
    def obtener_por_id(cls, user_id):
        query = "SELECT id, nombre FROM usuarios WHERE id = %s"
        results = connectToMySQL(
            os.getenv("MYSQL_DATABASE", "inicio_sesion_registro")
        ).query_db(query, (user_id,))

        return results[0] if results else None

    @classmethod
    def crear(cls, data):
        query = (
            "INSERT INTO usuarios "
            "(nombre, apellido, email, password_hash, fecha_nacimiento, interes) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        values = (
            data["nombre"].strip(),
            data["apellido"].strip(),
            data["email"].strip().lower(),
            generate_password_hash(data["password"]),
            date.fromisoformat(data["fecha_nacimiento"].strip()),
            data["interes"].strip(),
        )

        return connectToMySQL(
            os.getenv("MYSQL_DATABASE", "inicio_sesion_registro")
        ).query_db(query, values)

    @staticmethod
    def validar_registro(data):
        errors = []

        for field, label in (("nombre", "Nombre"), ("apellido", "Apellido")):
            value = data.get(field, "").strip()
            if not 2 <= len(value) <= 80 or not value.isalpha():
                errors.append(f"{label}: usa solo letras, entre 2 y 80 caracteres.")

        email = data.get("email", "").strip()
        if len(email) > 254 or not re.fullmatch(
            r"[^\s@]+@[^\s@]+\.[^\s@]+", email
        ):
            errors.append("Ingresa un correo válido.")

        password = data.get("password", "")
        if not 8 <= len(password) <= 128:
            errors.append("La contraseña debe tener entre 8 y 128 caracteres.")
        if not any(character.isupper() for character in password):
            errors.append("La contraseña debe incluir al menos una mayúscula.")
        if not any(character.isdigit() for character in password):
            errors.append("La contraseña debe incluir al menos un número.")

        if password != data.get("confirm_password", ""):
            errors.append("La confirmacion de contraseña no coincide.")

        birth_date = data.get("fecha_nacimiento", "").strip()
        if not birth_date:
            errors.append("Ingresa tu fecha de nacimiento.")
        else:
            try:
                if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", birth_date):
                    raise ValueError

                birth_date = date.fromisoformat(birth_date)
            except ValueError:
                errors.append("Ingresa una fecha de nacimiento válida.")
            else:
                today = date.today()
                age = today.year - birth_date.year - (
                    (today.month, today.day) < (birth_date.month, birth_date.day)
                )

                if birth_date > today:
                    errors.append("La fecha de nacimiento no puede estar en el futuro.")
                elif age < 18:
                    errors.append("Debes tener al menos 18 años para registrarte.")

        if data.get("interes", "").strip() not in INTERESES:
            errors.append("Selecciona un interés válido.")

        return errors
