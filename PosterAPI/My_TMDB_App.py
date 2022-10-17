import tmdbsimple as tmdb
from flask import Flask
from flask_mongoengine import MongoEngine
from bs4 import BeautifulSoup
import requests
import os


# class Movie()
def search():
    tmdb.API_KEY = os.environ["API_KEY"]
    # tmdb.REQUESTS_SESSION = requests.Session()

    search = tmdb.Search()
    response = search.movie(query='avengers')
    for info in search.results:
        print(info['title'], info['id'], info['release_date'], info['original_language'],info['popularity'],info['poster_path'])
