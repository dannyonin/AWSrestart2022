from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import *
from My_TMDB_App import Movie
import json
from titlecase import titlecase

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'My_Posters_DB',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class Imdb(db.EmbeddedDocument):
    imdb_id = db.StringField()
    rating = db.DecimalField()
    votes = db.IntField()

class Movie_DB(db.Document):
    title = db.StringField(required=True)
    year = db.IntField()
    rated = db.StringField()
    poster = db.FileField()
    imdb = db.EmbeddedDocumentField(Imdb)


@app.route('/movies')
def get_movies():

    get_movies = Movie()
    user_choice = get_movies.movie_title
    print("Your search <----->", user_choice)
    all_movies = get_movies.search()

    return json.dumps(all_movies, indent=3), 200



@app.route('/movies/<id>')
def get_one_movie(id: str):

    my_movies = Movie()
    user_choice = my_movies.movie_title
    print("Your search <----->", user_choice)
    movies = json.loads(my_movies.search())
    result = my_movies.menu()
    print("data page from movie title",id)

    return  movies[titlecase(id)], 200



app.run(debug=True)