from src import db, ma
from sqlalchemy.orm import relationship

class Unit(db.Model):
    __tablename__ = 'unit'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    abbreviation = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    products = relationship('Product', back_populates='unit')
    
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        
class UnitSchema(ma.Schema):
    class Meta:
        model = Unit
        load_instance = True
        sqla_sesson = db.session
        fields = ('id', 'name', 'abbreviation', 'created_at', 'updated_at', 'deleted_at')