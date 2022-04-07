from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

engine = create_engine('postgresql:///pet_agency')
if not database_exists(engine.url):
    create_database(engine.url)

def connect_db(app):
  db.app = app
  db.init_app(app)


class Pet(db.Model):
  '''pets table'''
  __tablename__ = 'pets'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String, nullable=False)
  species = db.Column(db.String, nullable=False)
  photo_url = db.Column(db.String, nullable=True)
  age = db.Column(db.Integer, nullable=True)
  notes = db.Column(db.Text, nullable=True)
  available = db.Column(db.Boolean, nullable=False, default=True)

  def __repr__(self):
    return f'<Pet {self.name}>'


