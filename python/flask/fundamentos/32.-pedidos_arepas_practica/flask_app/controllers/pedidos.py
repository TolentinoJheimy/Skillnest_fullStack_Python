# Importa la instancia de Flask para poder adosarle las rutas del sistema
from flask_app import app

# Importa las herramientas nativas de Flask para manejar respuestas, datos POST y navegación
from flask import render_template, request, redirect, url_for, flash

# Importa el Modelo Pedido para delegarle la validación y el almacenamiento de datos
from flask_app.models.pedido import Pedido

@app.route("/")
def inicio():
    """
    Ruta raíz que redirige automáticamente al flujo principal de listado.
    """
    return redirect(url_for("pedidos"))

@app.route("/pedidos")
def pedidos():
    """
    Solicita los datos al Modelo y se los inyecta a la plantilla HTML correspondiente.
    """
    # Invoca al método de clase del modelo para traer la lista de objetos de la BD
    todos_los_pedidos = Pedido.get_all()
    
    # Envía los objetos directamente a la vista usando Jinja2
    return render_template("pedidos.html", pedidos=todos_los_pedidos)

@app.route("/pedidos/nuevo")
def nuevo_pedido():
    """
    Muestra la vista del formulario limpio para un nuevo registro.
    """
    return render_template("nuevo_pedido.html")

@app.route("/pedidos/crear", methods=["POST"])
def crear_pedido():
    """
    Procesa el envío del formulario, orquesta la validación y define el destino del usuario.
    """
    # Extrae y limpia los espacios en blanco de los datos enviados mediante la petición POST
    nombre = request.form.get("nombre", "").strip()
    tipo_arepa = request.form.get("tipo_arepa", "").strip()
    cantidad = request.form.get("cantidad", "").strip()

    # Estructura el diccionario con los datos limpios para enviarlo al modelo
    data = {
        "nombre": nombre,
        "tipo_arepa": tipo_arepa,
        "cantidad": cantidad
    }

    # Intercepta el flujo invocando la validación del Modelo antes de tocar la base de datos
    if not Pedido.validar_pedido(data):
        # Si el modelo retorna False, aborta el guardado y recarga el formulario mostrando los flash()
        return redirect(url_for("nuevo_pedido"))

    # Transforma el dato a entero una vez asegurado que pasó la validación del backend
    data["cantidad"] = int(data["cantidad"])

    # Ordena al Modelo guardar el registro verificado en MySQL
    resultado = Pedido.save(data)

    # Verifica si hubo un fallo interno de guardado en el motor de base de datos
    if resultado is False:
        flash("No fue posible guardar el pedido.", "danger")
        return redirect(url_for("nuevo_pedido"))

    # Si todo sale bien, genera un mensaje de éxito para el usuario
    flash("Pedido creado correctamente.", "success")
    
    # Redirige al listado general para visualizar el nuevo cambio reflejado
    return redirect(url_for("pedidos"))
