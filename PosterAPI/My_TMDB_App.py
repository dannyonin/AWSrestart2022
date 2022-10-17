import tmdbsimple as tmdb
from flask import Flask
from flask_mongoengine import MongoEngine
from bs4 import BeautifulSoup
import requests
# import os
import json



class Movie():
    import tmdbsimple as tmdb
    import os

    def __init__(self):

        self.tmdb.API_KEY = self.os.environ["API_KEY"]
        self.movie_title = str
        self.movie_title_found = str
        self.movie_atr = {}
        self.movie_result = {self.movie_title_found: [self.movie_atr]}
        self.movie_title_list = []




    def search(self):
        # tmdb.REQUESTS_SESSION = requests.Session()

        search = tmdb.Search()
        search = search.movie(query=f'{self.movie_title}')
        for info in search['results']:
            self.movie_title_list.append(info['original_title'])
            self.movie_atr = {key:value for (key,value) in info.items()}
            self.movie_result = {title:atr for (title,atr) in zip(self.movie_title_list,self.movie_atr.items())}
            print((self.movie_atr))
        print((self.movie_result))


                # print(self.movie_result)

            # print(info['title'], info['id'], info['release_date'], info['original_language'],info['popularity'],info['poster_path'])






movie= Movie()
movie.movie_title = 'Avengers'
print(movie.movie_title)
movie.search()