import os
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
        
    with app.app_context():
        create_initial_data()

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
        
    return app

def register_blueprint(app):
    for module in find_modules('src.services'):
        app.register_blueprint(import_string(module).app) 

def create_initial_data():
    from src.models.pet_type import PetType
    from src.models.role import Role
    from src.models.unit import Unit

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
        
    #Verifica si existen datos para la tabla Unit y sino los agrega
    existing_data = Unit.query.all()
    if not existing_data:
        units = [
            Unit(name='Kilogramo', abbreviation='kg'),
            Unit(name='Gramo', abbreviation= 'g'),
            Unit(name='Litro', abbreviation= 'L'),
            Unit(name='Mililitro', abbreviation= 'mL'),
            Unit(name='Unidad', abbreviation= 'u')
        ]

        db.session.add_all(units)
        db.session.commit()

