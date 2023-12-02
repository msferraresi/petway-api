import datetime
from flask import Blueprint, jsonify, request
from src.models.pet_type import PetType, PetTypeSchema
from src import db

app = Blueprint('pet_type',__name__,url_prefix='/pet_type')

schema = PetTypeSchema()
schemas = PetTypeSchema(many=True)

@app.route('', methods=['GET'])
def get_pet_types():
    lst_units = PetType.query.order_by(PetType.id.asc()).filter_by(deleted_at=None).all()
    if not lst_units:
        return jsonify({'message': 'No pet types found'}), 404
    else:
        return jsonify({'pet_types':schema.dump(lst_units, many=True)}), 200