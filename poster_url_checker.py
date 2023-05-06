import json
import requests
from movie_storage import MovieAPI

movie_api = MovieAPI('3c3d7378')


def update_movie_posters():
    """ This function will check all the movies in the data.json
    file to see if they have movie poster urls present.  If they
    are not present, an api call will be made, and the data Will
    be added to the data.json file."""

    with open('data.json', 'r') as file:
        data = json.load(file)

    for movie_title, movie_data in data.items():
        if "poster url" not in movie_data:
            response = requests.get(f'{movie_api.api_url}&t={movie_title}')
            movie_json = response.json()

            poster_url = movie_json.get('Poster', '')
            if poster_url:
                movie_data['poster url'] = poster_url
                print(f'Added poster URL for {movie_title}!')

    with open('data.json', 'w') as file:
        json.dump(data, file)
