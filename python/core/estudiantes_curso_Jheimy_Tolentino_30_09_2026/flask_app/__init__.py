from flask import Flask

app = Flask(__name__)

from flask_app.controllers import cursos
from flask_app.controllers import estudiantes