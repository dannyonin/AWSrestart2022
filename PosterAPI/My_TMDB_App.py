import tmdbsimple as tmdb
from flask import Flask
from flask_mongoengine import MongoEngine
from bs4 import BeautifulSoup
import requests
import os
import json



class Movie():
    def __init__(self):
        self.movie_title = str
        self.movie_atr = {self.movie_title: []}

    def search(self):
        tmdb.API_KEY = os.environ["API_KEY"]
        # tmdb.REQUESTS_SESSION = requests.Session()

        search = tmdb.Search()
        response = search.movie(query=f'{self.movie_title}')
        for info in search.results:
            for keys in info:
                movie_result = {}
                atributes = keys
            print(info)

            print(info['title'], info['id'], info['release_date'], info['original_language'],info['popularity'],info['poster_path'])






movie= Movie()
movie.movie_title = 'Avengers'
print(movie.movie_title)
movie.search()