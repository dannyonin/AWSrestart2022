'''

     MY API PROGRAM WITH FOR MOVIE POSTERS
     *SEARCH FOR POSTER IN TMDB DATA BASE
     *UPLOAD THE DATA TO MONGODB  WITH FLASK
     *ABILITY TO SEARCH IN THE DATA BASE


    <the code is not in final version>
    <work in progress>

    Author: Daniel Yonin
    AWSRestart 2022

'''


import tmdbsimple as tmdb
from flask import Flask
from flask_mongoengine import MongoEngine
from bs4 import BeautifulSoup
import requests
# import os
import json


# Class Movie built with TMDB API
class Movie():
    import tmdbsimple as tmdb
    import os

    def __init__(self):

        self.tmdb.API_KEY = self.os.environ["API_KEY"]
        self.movie_title = input("Please Enter name of a Movie:")
        self.movie_title_found = str
        self.movie_atr = {}
        self.movie_result = {}

    # Search Function for movie
    def search(self):
        search = tmdb.Search()
        search = search.movie(query=f'{self.movie_title}')

        for info in search['results']:
            self.movie_atr = {key:value for (key,value) in info.items()}
            self.movie_title_found = info['original_title']
            self.movie_result[self.movie_title_found] = self.movie_atr

        return json.dumps(self.movie_result, indent=3)


movie= Movie()
a=movie.movie_title
print(a)
print(movie.search())
