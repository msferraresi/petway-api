from flask_jwt_extended import JWTManager
from werkzeug.utils import find_modules, import_string
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
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
    jwt.init_app(app)
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
    from src.models.pet_type import PetType
    from src.models.role import Role
    #Verifica si existen datos para la tabla PetType y sino los agrega
    existing_data = PetType.query.all()
    if not existing_data:
        pet_types = [
            PetType(name='Perro'),
            PetType(name='Gato'),
            PetType(name='Otro')
        ]

        db.session.add_all(pet_types)
        db.session.commit()

    #Verifica si existen datos para la tabla Roles y sino los agrega
    existing_data = Role.query.all()
    if not existing_data:
        roles = [
            Role(name='Empleado'),
            Role(name='Cliente')
        ]

        db.session.add_all(roles)
        db.session.commit()

