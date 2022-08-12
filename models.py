"""Model classes for Pet Adoption Agency App"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

default_pet_icon = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs2ZrJnge74YWK4yP3fD1-u2Iwp-cUHcy9Aw&usqp=CAU'

class Pet(db.Model):
    """Create a new pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.Text, nullable=False, default='Harry')
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def identify_myself(self):
        """Returns intro statement about pet"""

        return f"Hi, I am {self.name} and I'm a {self.species}. I am {self.age} years old and I am currently {'available!' if self.available else 'not available.'}"

    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or default_pet_icon
