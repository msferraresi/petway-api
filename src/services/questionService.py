import datetime
from flask import Blueprint, jsonify, request
from src.models.question import Question, QuestionSchema
from src import db

app = Blueprint('question',__name__,url_prefix='/question')


schema = QuestionSchema()
schemas = QuestionSchema(many=True)

@app.route('/create', methods=['POST'])
def create():
    values = request.get_json()
    if not values:
        return jsonify({'message': 'No input data provided'}), 400 # Bad request
    elif values.get('name') is None:
        return jsonify({'message': 'No input data NAME provided'}), 400 # Bad request
    elif values.get('last_name') is None:
        return jsonify({'message': 'No input data LAST NAME provided'}), 400 # Bad request
    elif values.get('email') is None:
        return jsonify({'message': 'No input data EMAIL provided'}), 400 # Bad request
    elif values.get('age') is None:
        return jsonify({'message': 'No input data AGE provided'}), 400 # Bad request
    elif values.get('pet_type_id') is None:
        return jsonify({'message': 'No input data PET TYPE provided'}), 400 # Bad request
    elif values.get('pet_name') is None:
        return jsonify({'message': 'No input data PET NAME provided'}), 400 # Bad request
    elif values.get('question') is None:
        return jsonify({'message': 'No input data LAST QUESTION provided'}), 400 # Bad request
    else:
        try:
            element = Question(values.get('name'), values.get('last_name'), values.get('email'), values.get('age'), values.get('pet_type_id'), values.get('pet_name'), values.get('question'))
            db.session.add(element)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Question created'}), 201
        except:
            # Internal server error
            return jsonify({'message': 'An error occurred creating the Question'}), 500

