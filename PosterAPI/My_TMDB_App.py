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
import json


# Class Movie built with TMDB API
class Movie:
    import tmdbsimple as tmdb
    import os

    def __init__(self):

        self.tmdb.API_KEY = self.os.environ["API_KEY"]
        self.movie_title = "avengers"  # input("Please Enter name of a Movie:")
        self.movie_title_found = str
        self.movie_atr = {}
        self.movie_result = {}
        self.POSTER_PATH = "https://image.tmdb.org/t/p/original/"

    # Search Function for movie
    def search(self):

        search = tmdb.Search()
        search = search.movie(query=f'{self.movie_title}')

        for info in search['results']:
            self.movie_atr = {key: value for (key, value) in info.items()}
            self.movie_title_found = info['original_title']
            self.movie_result[self.movie_title_found] = self.movie_atr

        return json.dumps(self.movie_result, indent=3)

    # Menu Option for user to choose which movie poster to download
    def menu(self):

        menu_choices = []

        for number, results in enumerate(self.movie_result):
            menu_choices.append(f'{number + 1}:{results}')

        for choice in menu_choices:
            print(choice)
        return menu_choices

    # User input for choice menu
    def user_input_for_poster(self, search_result):

        choice = input("choose poster to download: ")
        choice = int(choice)
        try:
            name = search_result[choice - 1].split(":", 1)
            print(f'your choice is {name[1]}')
            return name[1], self.movie_result.get(name[1])
        except:
            print("error input")
            return 1

    def get_data(self, data, selected):
        pass

    # Download Poster Function (save file locally in Downloads directory)
    def download(self, name, num, poster_path, path='.\Downloads'):
        img_url = "https://image.tmdb.org/t/p/original/"
        new_url = (img_url + poster_path[num])
        r = requests.get(new_url)
        name = name.replace(":", "").replace(" ", "")
        filetype = r.headers['content-type'].split('/')[-1]
        filename = f'{name}_poster.{filetype}'
        print(filename)
        filepath = os.path.join(path, filename)
        with open(filepath, 'wb') as w:
            w.write(r.content)


if __name__ == '__main__':
    movie = Movie()
    user_choice = movie.movie_title
    print("Your search <----->", user_choice)
    search_results = movie.search()
    poster_menu = movie.menu()
    pickup = movie.user_input_for_poster(poster_menu)
    print(list(pickup))
