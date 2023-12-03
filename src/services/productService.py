import base64
import datetime as dt
from distutils import config
import os
from flask import Blueprint, Config, Flask, jsonify, request
import flask
from src.models.product import Product, ProductSchema
from src import db
from sqlalchemy.orm import joinedload
from werkzeug.utils import secure_filename

confi = Flask(__name__)
confi.config.from_object('config.configProd.ProductionConfig')

app = Blueprint('product',__name__,url_prefix='/product')

schema = ProductSchema()
schemas = ProductSchema(many=True)

@app.route('', methods=['GET'])
def get_products():
    search_term = request.args.get('search', None)
    query = Product.query.options(joinedload(Product.unit)).order_by(Product.name.asc()).filter_by(deleted_at=None)
    if search_term:
        query = query.filter(Product.name.ilike(f"%{search_term}%"))

    lst_products = query.all()
    if not lst_products:
        return jsonify({'message': 'No products found'}), 404
    else:
        return jsonify({'products':schema.dump(lst_products, many=True)}), 200

@app.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    valid = Flask(__name__)
    valid.config.from_object('config.configProd.ProductionConfig')
    print(valid.config['UPLOAD_FOLDER'])
    product = Product.query.options(joinedload(Product.unit)).filter_by(id=product_id, deleted_at=None).first()
    if not product:
        return jsonify({'message': 'No product found'}), 404
    else:
        image_path = f"{confi.config['UPLOAD_FOLDER']}/{product.photo_name}"
        product_data = schema.dump(product)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as image_file:
                image_content = image_file.read()
            
            image_base64 = base64.b64encode(image_content).decode('utf-8')
            product_data['image'] = image_base64

        return jsonify({'product': product_data}), 200

'''@app.route('', methods=['POST'])
def create_product():
    values = request.get_json()
    print(f"valores:{request}")
    if not values:
        return jsonify({'message': 'No input data provided'}), 400 
    elif values.get('name') is None:
        return jsonify({'message': 'No input data NAME provided'}), 400
    elif values.get('unit_id') is None:
        return jsonify({'message': 'No input data UNIT provided'}), 400
    else:
        name = values.get('name')
        description = values.get('description') if values.get('description') is not None else 'No description data'
        quantity = values.get('quantity') if values.get('quantity') is not None else 0.0
        price = values.get('price') if values.get('price') is not None else 0.0
        unit_id = values.get('unit_id')
        photo_name = values.get('photo_name') if values.get('photo_name') is not None else 'not_available.png'

        product = Product(name, description, quantity, price, unit_id, photo_name)
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product created', 'product': schema.dump(product)}), 200'''
        
@app.route('', methods=['POST'])
def create_product():
    name = request.form.get('name')
    description = request.form.get('description', 'No description data')
    quantity = float(request.form.get('quantity', 0.0))
    price = float(request.form.get('price', 0.0))
    unit_id = int(request.form.get('unit_id'))
    photo_name = 'not_available.png'

    if 'photo' in request.files:
        photo_file = request.files['photo']
        if photo_file.filename != '':
            photo_name = photo_file.filename
            timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
            _, extension = os.path.splitext(photo_file.filename)
            filename = f"{timestamp}{extension}"

            filepath = os.path.join(confi.config['UPLOAD_FOLDER'], filename)
            photo_file.save(filepath)
            photo_name = filename

    product = Product(name, description, quantity, price, unit_id, photo_name)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'product': schema.dump(product)}), 200



'''@app.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    values = request.get_json()
    if not values:
        return jsonify({'message': 'No input data provided'}), 400 
    elif values.get('name') is None:
        return jsonify({'message': 'No input data NAME provided'}), 400
    elif values.get('unit_id') is None:
        return jsonify({'message': 'No input data UNIT provided'}), 400
    elif not product:
        return jsonify({'message': 'No product found'}), 404
    else:
        name = values.get('name')
        description = values.get('description')
        quantity = values.get('quantity')
        price = values.get('price')
        unit_id = values.get('unit_id')
        photo_name = values.get('photo_name')
        
        product.name = name if name is not None else product.name
        product.description = description if description is not None else product.description
        product.quantity = quantity if quantity is not None else product.quantity
        product.price = price if price is not None else product.price
        product.unit_id = unit_id if unit_id is not None else product.unit_id
        product.photo_name = photo_name if photo_name is not None else product.photo_name

        db.session.commit()
        return jsonify({'message': 'Product updated', 'product': schema.dump(product)}), 200'''
        
@app.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)

    name = request.form.get('name')
    description = request.form.get('description', 'No description data')
    quantity = float(request.form.get('quantity', 0.0))
    price = float(request.form.get('price', 0.0))
    unit_id = int(request.form.get('unit_id'))
    photo_name = request.form.get('photo_name')

    product.name = name if name is not None else product.name
    product.description = description if description is not None else product.description
    product.quantity = quantity if quantity is not None else product.quantity
    product.price = price if price is not None else product.price
    product.unit_id = unit_id if unit_id is not None else product.unit_id

    if photo_name != product.photo_name:
        if photo_name != 'not_available.png':
            old_photo_name = product.photo_name
            path_old_photo = os.path.join(confi.config['UPLOAD_FOLDER'], old_photo_name)
            if os.path.exists(path_old_photo):
                os.remove(path_old_photo)
        if 'photo' in request.files:
            photo_file = request.files['photo']
            if photo_file.filename != '':
                photo_name = photo_file.filename
                timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
                _, extension = os.path.splitext(photo_file.filename)
                filename = f"{timestamp}{extension}"

                filepath = os.path.join(confi.config['UPLOAD_FOLDER'], filename)
                photo_file.save(filepath)
                photo_name = filename

    product.photo_name = photo_name if photo_name is not None else product.photo_name

    db.session.commit()
    return jsonify({'message': 'Product updated', 'product': schema.dump(product)}), 200

@app.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.filter_by(id=product_id, deleted_at=None).first()
    if not product:
        return jsonify({'message': 'No product found'}), 404
    else:
        if product.photo_name != 'not_available.png':
            old_photo_name = product.photo_name
            product.photo_name = 'not_available.png'
            path_old_photo = os.path.join(confi.config['UPLOAD_FOLDER'], old_photo_name)
            if os.path.exists(path_old_photo):
                os.remove(path_old_photo)
        product.deleted_at = dt.datetime.now()
        db.session.commit()
        return jsonify({'message': 'Product deleted'}), 200
