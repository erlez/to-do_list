from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix = '/todo')

@bp.route('/list')
def index():
    return "lista de tareas"

@bp.route('/create')
def crear_tarea():
    return "crear tarea"