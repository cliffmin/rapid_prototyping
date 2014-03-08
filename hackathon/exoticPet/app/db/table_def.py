# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


engine = create_engine('sqlite:///pokemon.db', echo=True)

########################################################################
class Pokemon(db.Model):
    """"""
    __tablename__ = "pokemon"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    pokemonType = db.Column(db.String)
    level = db.Column(db.String)

    #----------------------------------------------------------------------
    def __init__(self, name, gender, pokemonType, level):
        """"""
        self.name = name
        self.gender = gender
        self.pokemonType = pokemonType
        self.level = level


# create tables
Base.metadata.create_all(engine)