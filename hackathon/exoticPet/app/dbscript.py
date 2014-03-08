import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pokemon.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create an artist
pikachu = Pokemon("Pikachu", "male", "electric", "9")
charmander = Pokemon("Charmander", "male", "fire", "17")
chancey = Pokemon("Chancey", "female", "egg", "18")
steelix = Pokemon("Steelix", "male", "metal", "20")
squirtle = Pokemon("Squirtle", "female", "water", "10")
bulbasaur = Pokemon("Bulbasaur", "male", "grass", "20")
butterfree = Pokemon("Butterfree", "female", "insect", "30")
jigglypuff = Pokemon("jigglypuff", "female", "moon", "25")
oddish = Pokemon("Oddish", "male", "grass", "40")
dewgong = Pokemon("Dewgong", "female", "moon", "17")


# add more albums
# Add the record to the session object
session.add(pikachu)
session.add(charmander)
session.add(steelix)
session.add(chancey)
session.add(squirtle)
session.add(bulbasaur)
session.add(butterfree)
session.add(jigglypuff)
session.add(dewgong)

# commit the record the database
session.commit()

