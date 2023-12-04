import datetime
from flask import Blueprint, jsonify, request
from src.models.unit import Unit, UnitSchema
from src import db

app = Blueprint('unit',__name__,url_prefix='/unit')

schema = UnitSchema()
schemas = UnitSchema(many=True)

@app.route('', methods=['GET'])
def get_units():
    lst_units = Unit.query.order_by(Unit.name.asc()).filter_by(deleted_at=None).all()
    if not lst_units:
        return jsonify({'message': 'No units found'}), 404
    else:
        return jsonify({'units':schema.dump(lst_units, many=True)}), 200

@app.route('/<int:unit_id>', methods=['GET'])
def get_unit(unit_id):
    unit = Unit.query.filter_by(id=unit_id, deleted_at=None).first()
    if not unit:
        return jsonify({'message': 'No unit found'}), 404
    else:
        return jsonify({'unit': schema.dump(unit)}), 200