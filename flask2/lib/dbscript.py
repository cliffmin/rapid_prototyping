import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create an artist
new_artist1 = Artist("The Strokes")
new_artist1.albums = [Album("Room on fire",
                           "Alternative",
                           "Paramount", "CD")]

new_artist2 = Artist("Newsboys")
new_artist2.albums = [Album("Read All About It",
                           "Country",
                           "Refuge", "CD")]
new_artist3 = Artist("Pinback")
new_artist3.albums = [Album("Summer in Abaddon",
                           "Alternative",
                           "Parrapa", "CD")]

# add more albums
more_albums = [Album("Hell Is for Wimps",
                     "Country",
                     "Star Song", "CD"),
               Album("Love Liberty Disco",
                     "Country",
                     "Sparrow", "CD"),
               Album("Thrive",
                     "Country",
                     "Sparrow", "CD")]
new_artist2.albums.extend(more_albums)

# Add the record to the session object
session.add(new_artist1)
session.add(new_artist2)
session.add(new_artist3)
# commit the record the database
session.commit()

# Add several artists
session.add_all([
    Artist("MXPX"),
    Artist("Kutless"),
    Artist("Thousand Foot Krutch")
    ])
session.commit()