# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///pokemon.db', echo=True)
Base = declarative_base()

########################################################################
class Pokemon(Base):
    """"""
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    pokemonType = Column(String)
    level = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, name, gender, pokemonType, level):
        """"""
        self.name = name
        self.gender = gender
        self.pokemonType = pokemonType
        self.level = level


# create tables
Base.metadata.create_all(engine)