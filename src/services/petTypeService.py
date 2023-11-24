import datetime
from flask import Blueprint, jsonify, request
from src.models.pet_type import PetType, PetTypeSchema
from src import db

app = Blueprint('pet_type',__name__,url_prefix='/pet_type')

schema = PetTypeSchema()
schemas = PetTypeSchema(many=True)
