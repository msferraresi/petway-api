from src import db, ma
from sqlalchemy.orm import relationship

from src.models.unit import UnitSchema

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), default='No description data')
    photo_name = db.Column(db.String(200), default='not_available.png')
    quantity = db.Column(db.Float, default=0.0)
    price = db.Column(db.Float, default=0.0)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    unit = relationship("Unit", back_populates='products')

    def __init__(self, name, description, quantity, price, unit_id, photo_name):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.unit_id = unit_id
        self.photo_name = photo_name
        
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity,
            'price': self.price,
            'unit_id': self.unit_id,
            'photo_name': photo_name,
            'unit': {
                'id': self.unit.id,
                'name': self.unit.name,
                'abbreviation': self.unit.abbreviation
            }
        }
    
class ProductSchema(ma.Schema):
    unit = ma.Nested(UnitSchema, only=('id', 'name', 'abbreviation'))
    class Meta:
        model = Product
        load_instance = True
        sqla_sesson = db.session
        fields = ('id', 'name', 'description', 'quantity', 'price', 'unit_id', 'photo_name', 'unit',
                  'created_at', 'updated_at', 'deleted_at')