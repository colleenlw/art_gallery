from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name= db.Column(db.String(15), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    artworks = db.relationship('Artwork', backref='artists', lazy=True)

    def __init__(self, #artist_id: int, 
    first_name:str, last_name:str, location:str):
        #self.artist_id = artist_id
        self.first_name = first_name
        self.last_name = last_name
        self.location = location

    def serialize(self):
        return {
            'id': self.id,
            #'artist_id': self.artist_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'location': self.location

        }
    
class Artwork(db.Model):
    __tablename__ = 'artworks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    date = db.Column(db.Integer, nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

    def __init__(self, artist_id: int, 
    title:str, date:int):
        self.artist_id = artist_id
        self.title = title
        self.date = date
    
    def serialize(self):
        return {
            'id': self.id,
            'artist_id': self.artist_id,
            'title': self.title,
            'date': self.date
        }

categories_table = db.Table(
    'art_category',
    db.Column(
        'artworks_id', db.Integer,
        db.ForeignKey('artworks.id'),
        primary_key=True
    ),
    db.Column(
    'category_id', db.Integer,
        db.ForeignKey('categories.id'),
        primary_key=True
        )
    )

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), nullable=True)
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))

    def __init__(self, artwork_id: int, category:str):
        self.artwork_id = artwork_id
        self.category = category
    
    def serialize(self):
        return {
            'id': self.id,
            'artworks_id': self.artwork_id,
        }
    
class Artist_Account(db.Model):
    __tablename__ = 'artist_accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __init__(self, artist_id: int, 
    email:str, password:str):
        self.artist_id = artist_id
        self.email = email
        self.password = password
    
    def serialize(self):
        return {
            'id': self.id,
            'artist_id': self.artist_id,
            'email': self.email,
            'password': self.password
        }

class Collector(db.Model):
    __tablename__ = 'collectors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    artworks_id = db.Column(db.Integer, db.ForeignKey('artworks.id'), nullable=False)

    def __init__(self, collector_id:int, first_name:str, last_name:str, artworks_id:int):
        self.collector_id = collector_id
        self.first_name = first_name
        self.last_name = last_name
        self.artworks_id = artworks_id
    
    def serialize(self):
        return {
            'id': self.id,
            'collector_id': self.collector_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'artworks_id': self.artworks_id
        }

class Collector_Account(db.Model):
    __tablename__ = 'collector_accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collector_id = db.Column(db.Integer, db.ForeignKey('collectors.id'), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __init__(self, collector_id: int, email:str, password:str):
        self.collector_id = collector_id
        self.email = email
        self.password = password
    
    def serialize(self):
        return {
            'id': self.id,
            'collector_id': self.collector_id,
            'email': self.email,
            'password': self.password
        }

# need to set up foreign key references for one-to-many relationships (artists to artworks, customer to artworks)
# need to create the bridge table for many-to-many relationships (artoworks to categories) DONE
# set up one-to-one relationships (customer-account, artists-account)
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

