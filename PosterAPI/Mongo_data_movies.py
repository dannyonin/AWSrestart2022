from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import *
from My_TMDB_App import Movie
import json
from titlecase import titlecase
import pymongo
from gridfs import GridFS

app = Flask(__name__)


class Image_Database():
	def __init__(self):
		self.mongo_host = "localhost"
		self.mongo_port = 27017
		self.mongo_db = 'MyPostersDB'
		self.mongo_collection = 'movies'
		self.mongo_safe = False
		self.conn=connect(self.mongo_host, self.mongo_port)
		self.db=self.conn[self.mongo_db]
		self.collection = self.db[self.mongo_collection]
		self.grid = GridFS(self.db, self.mongo_collection+".fs")

	def drop(self):
		self.db.drop_collection(self.mongo_collection)
		self.db.drop_collection(self.mongo_collection+".fs.chunks")
		self.db.drop_collection(self.mongo_collection+".fs.files")

	def set_raw(self, key, value):
		try:
			self.collection.update({'_id': key}, {"$set": { 'd': value } }, upsert=True, safe=self.mongo_safe)
		except InvalidStringData:
			self.rm(key)
			self.grid.put(value, _id=key)


class Movie_info(DynamicDocument):
	title = StringField()
	original_title = StringField()
	original_language = StringField()
	id = IntField()
	overview = StringField()
	poster = FileField()
#
class Poster(Document):
	title = ReferenceField(Movie_info)




@app.route('/movies')
def get_movies():

    get_movies = Movie()
    user_choice = get_movies.movie_title
    print("Your search <----->", user_choice)
    all_movies = get_movies.search()

    return json.dumps(all_movies, indent=3), 200


@app.route('/genres')
def list_genres():

	genres = Movie()
	my_genre_list = genres.genre_list()

	return json.dumps(my_genre_list) ,200

@app.route('/movies/<id>')
def get_one_movie(id: str):

    my_movies = Movie()
    user_choice = my_movies.movie_title
    print("Your search <----->", user_choice)
    movies = json.loads(my_movies.search())
    result = my_movies.menu()
    print("data page from movie title",id)

    return  movies[titlecase(id)], 200


my_mongo = Image_Database()
drop = my_mongo.drop()

app.run(debug=True)