from werkzeug.utils import find_modules, import_string
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()

def create_app(environment=None):
    app = Flask(__name__)
    
    if environment == 'production':
        app.config.from_object('config.configProd.ProductionConfig')
    elif environment == 'development':
        app.config.from_object('config.configDev.DevelopmentConfig')
    else:
        raise(Exception)
    
    db.init_app(app)
    ma.init_app(app)
    CORS(app)
    
    with app.app_context():
        register_blueprint(app)
        db.create_all()
        
        create_initial_data()

    return app

def register_blueprint(app):
    for module in find_modules('src.services'):
        app.register_blueprint(import_string(module).app) 
        
def create_initial_data():
    # Comprueba si ya hay datos en la tabla PetType
    from src.models.pet_type import PetType  # Importa el modelo dentro de la función
    existing_data = PetType.query.all()
    if not existing_data:
        # Si no hay datos, inserta algunos ejemplos
        pet_types = [
            PetType(name='Perro'),
            PetType(name='Gato'),
            PetType(name='Otro')
            # Agrega más según sea necesario
        ]

        # Agrega y commitea los datos a la base de datos
        db.session.add_all(pet_types)
        db.session.commit()
