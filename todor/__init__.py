#indicador de paquete 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#extencion de sqlalchemy
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    
    #config del proyecto
    app.config.from_mapping(
        DEBUG = True,
        #clave provisional por desarollo
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )
    
    db.init_app(app)
    
    #registro blue print
    from . import todo , auth
    
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app