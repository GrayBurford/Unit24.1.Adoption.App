"""Add sample pets to Pet Adoption Agency App Database"""

from models import db, Pet
from app import app

# Drop all tables and recreate all tables
db.drop_all()
db.create_all()

gray = Pet(name='Gray', species='human', age=35, notes='I love bouldering', available=True)
tina = Pet(name='Tina', species='human', age=33, notes='I love top roping', available=True)
bensley = Pet(name='Bensley', species='cat', age=1, notes='Food all day', available=False)
ming = Pet(name='Ming', species='cat', age=1, notes='Let me outside!!!', available=True)

db.session.add_all([gray, tina, bensley, ming])
db.session.commit()