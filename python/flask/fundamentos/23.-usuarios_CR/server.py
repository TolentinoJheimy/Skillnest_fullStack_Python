from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)

# RUTA 1: Mostrar todos los usuarios
@app.route('/usuarios')
def mostrar_usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template('usuarios.html', usuarios=todos_los_usuarios)

# RUTA 2: Mostrar el formulario (Esta es la que causaba el error)
@app.route('/usuarios/nuevo')
def nuevo_usuario():
    return render_template('usuario_nuevo.html')

# RUTA 3: Procesar el formulario e insertar en la BD
@app.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(datos)
    # Redirige usando url_for apuntando a la función del listado
    return redirect(url_for('mostrar_usuarios'))

if __name__ == "__main__":
    app.run(debug=True)
