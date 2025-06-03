from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()



User_Person_Favorites = Table('user_person_favorites',
                       db.metadata,
                        Column('user_id', db.ForeignKey('user.id'), primary_key=True, nullable=False),
                        Column('person_id', db.ForeignKey('person.id'), primary_key=True, nullable=False),
)

User_Planet_Favorites = Table(
    'user_planet_favorites',
    db.metadata,
    Column('user_id', db.ForeignKey('user.id'), primary_key=True, nullable=False),
    Column('planet_id', ForeignKey('planet.id'), primary_key=True, nullable=False),
    
)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)


#relationship
    favorite_people: Mapped[list['Person']] = relationship(secondary=User_Person_Favorites, back_populates='favorited_by_user')
    favorite_planet: Mapped[list['Planet']] = relationship(secondary=User_Planet_Favorites, back_populates='favorited_by_user')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }


class Person(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=True)

    favorited_by_user: Mapped[list['User']] = relationship(secondary=User_Person_Favorites, back_populates='favorite_people')

    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'hair_color': self.hair_color
        }
    
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    terrain: Mapped[str] = mapped_column(String(120), nullable=False)

    favorited_by_user: Mapped[list['User']] = relationship(secondary=User_Planet_Favorites, back_populates='favorite_planet')

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'terrain': self.terrain
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


