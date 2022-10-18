from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import *
from My_TMDB_App import Movie
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'My_Posters_DB',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)
class Movie_DB(db.Document):
    title = db.StringField(required=True)
    year = db.IntField()
    rated = db.StringField()
    cast = db.EmbeddedDocumentListField(Cast)
    poster = db.FileField()
    imdb = db.EmbeddedDocumentField(Imdb)
@app.route('/movies')
def get_movies():
    my_movie = Movie()
    user_choice = my_movie.movie_title
    print("Your search <----->", user_choice)
    movies = my_movie.search()
    return json.dumps(movies, indent=3), 200

@app.route('/movies/<id>')
def get_one_movie(id: str):
    movie = Movie.objects(id=id).first()
    return jsonify(movie), 200



db.init_app(app.run())
