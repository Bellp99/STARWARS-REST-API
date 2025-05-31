from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

#user_person = db.Table('user_person_favorites',
#                        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#                        db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
#)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User "{self.username}">'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.email,
            # do not serialize the password, its a security breach
        }


class Person(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=True)

    def __repr__(self):
        return f'<Person "{self.name}">'

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'hair_color': self.hair_color
        }
    
class User_Person_Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)  
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey('person.id'), nullable=False)
    user = relationship(User) 
    person = relationship(Person)

    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "person_id": self.person_id,
        }

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)


