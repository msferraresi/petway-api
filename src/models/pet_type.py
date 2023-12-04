from src import db, ma
from sqlalchemy.orm import relationship

class PetType(db.Model):
    __tablename__ = 'pet_type'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
        
    questions = relationship('Question', back_populates='pet_type')

    def __init__(self, name):
        self.name = name
        
class PetTypeSchema(ma.Schema):
    class Meta:
        model = PetType
        load_instance = True
        sqla_sesson = db.session
        fields = ('id', 'name', 'created_at', 'updated_at', 'deleted_at')