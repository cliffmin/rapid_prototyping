from flask import Flask, render_template
#AUSTIN
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/pokemon.db'
db = SQLAlchemy(app)

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


#AUSTIN
@app.route('/search')
def search():
    pokemonArray = Pokemon.query.all()

    identity = request.args.get('identity', '')
    name = request.args.get('name', '')
    for pokemon in pokemonArray:
     if (pokemon.name == name):
         return render_template('search.html', pokemon=pokemon)


