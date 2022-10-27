from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import *
from My_TMDB_App import Movie
import json
from titlecase import titlecase
import pymongo
from gridfs import GridFS

app = Flask(__name__)


class Database(object):
	def __init__(self):
		self.dataframe = {}
		self.mongo_host = "localhost"
		self.mongo_port = 27017
		self.mongo_db = 'MY_Movies_Database'
		self.mongo_collection = 'Movies'
		self.mongo_safe = False
		self.conn=connect(self.mongo_host, self.mongo_port)
		self.db=self.conn[self.mongo_db]
		self.collection = self.db[self.mongo_collection]
		self.grid = GridFS(self.db, self.mongo_collection+".fs")

	def craete_collection(self):
		pass

	@staticmethod
	def drops():
		db.collection.drop(self.mongo_collection)
		db.collection.drop(self.mongo_collection+".fs.chunks")
		db.collection.drop(self.mongo_collection+".fs.files")

	def set_raw(self, key, value):
		try:
			self.collection.update({'_id': key}, {"$set": { 'd': value } }, upsert=True, safe=self.mongo_safe)
		except InvalidStringData:
			self.rm(key)
			self.grid.put(value, _id=key)

	def mongodb_connect(self):

		try:
			return pymongo.MongoClient(self.mongo_host, self.mongo_port)

		except pymongo.errors.ConnectionFailure:
			print("Failed to connect to server {}").format(self.mongo_host, self.mongo_port)


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

#try to grt only the movie attributes - for database template
@app.route('/test')
def show_attributes():

	mv = Movie()
	atr = mv.search()
	json_data= json.loads(atr)
	h

	return json_data.keys()

@app.route('/movies')
def get_movies():

    get_movies = Movie()
    user_choice = get_movies.movie_title
    print("Your search <----->", user_choice)
    all_movies = get_movies.search()

    return json.loads(all_movies), 200


@app.route('/genres')
def list_genres():

	genres = Movie()
	my_genre_list = genres.genre_list()

	return json.loads(my_genre_list) ,200

@app.route('/movies/<movie_name>')
def get_one_movie(movie_name: str):

    my_movies = Movie()
    user_choice = my_movies.movie_title
    print("Your search <----->", user_choice)
    movies = json.loads(my_movies.search())
    result = my_movies.menu()
    print("data page from movie title",movie_name)

    return  movies[titlecase(movie_name)], 200

print()

# my_data_base = Database()
# print(my_data_base.collection)
# data = json.dumps(get_one_movie('cars 2')[0])
# print(data)
# print(type(data))
# jsonData = json.loads(data)
# print(type(jsonData))
# for x in jsonData:
# 	print(x)



# movie_1 =my_data_base.collection.insert_one(dict(get_one_movie("cars 3")[0]))






app.run(debug=True)