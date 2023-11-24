from src import db, ma
from sqlalchemy.orm import relationship

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pet_type_id = db.Column(db.Integer, db.ForeignKey('pet_type.id'), nullable=False)
    pet_name = db.Column(db.String(120), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    pet_type = relationship("PetType", back_populates='questions')
    
    def __init__(self, name, last_name, email, age, pet_type_id, pet_name, question):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.pet_type_id = pet_type_id
        self.pet_name = pet_name
        self.question = question
        
class QuestionSchema(ma.Schema):
    class Meta:
        model = Question
        load_instance = True
        sqla_sesson = db.session
        fields = ('id','name','last_name','email','age','pet_type_id','pet_name',
                  'question','created_at','updated_at','deleted_at')