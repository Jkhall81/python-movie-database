import json
import requests

class MovieAPI:
  def __init__(self, api_key):
    self.api_key = api_key
    self.api_url = f'http://www.omdbapi.com/?i=tt3896198&apikey={self.api_key}'

movie_api = MovieAPI('3c3d7378')

def list_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data. 
    """
    with open('data.json', 'r') as f:
      movies = json.load(f)

    number_of_movies = len(movies.keys())
    print(f'There are {number_of_movies} movies in total.')
    for item in movies:
        str1 = (
        f'{item}, Rating: {movies[item]["rating"]}, '\
        f'Year of Release: {movies[item]["year of release"]}'
        )
        print(str1)


def add_movie():
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # gets movie title from user
    movie_title = input('Please enter a movie name: ')
    
    # api request
    #api_key = '3c3d7378'
    api_url = f'{movie_api.api_url}&t={movie_title}'
      
    try:
      response = requests.get(api_url)
      # extract what we want from the api response
      if response.status_code != 200:
        print(f'Error: {response.text}')
        return
      movie_data = response.json()

    except requests.exceptions.RequestException as e:
      print(f'Error: {e}')
      return

    if movie_data['Response'] == 'False':
      print(f'Movie "{movie_title}" not found!')
      return
    
    
    new_rating = float(movie_data['imdbRating'])
    new_year = int(movie_data['Year'])
    new_poster_url = movie_data['Poster']
    new_obj = {
      'rating': new_rating,
      'year of release': new_year,
      'poster url': new_poster_url
      }

    # update our data.json
    with open('data.json', 'r') as f:
      movies = json.load(f)
    movies[movie_title] = new_obj
    with open('data.json', 'w') as f:
      json.dump(movies, f, indent=4)

    
def delete_movie():
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open('data.json', 'r') as f:
      movies = json.load(f)

    movie_to_delete = input('Which movie would you like to delete?  Movie name: ')
    if movies.get(movie_to_delete) is None:
        print('This movie is not present in the database!')
    else:
        print(f'{movie_to_delete} successfully deleted!')
        del movies[movie_to_delete]

    with open('data.json', 'w') as f:
      json.dump(movies, f, indent=4)


def update_movie():
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open('data.json', 'r') as f:
      movies = json.load(f)

    movie_to_check = input('Enter a movie name: ')
    if movies.get(movie_to_check) is None:
        print('This movie is not present in the database!')
    else:
        new_rating = float(input('Please enter a new rating: '))
        movies[movie_to_check]['rating'] = new_rating
  
    with open('data.json', 'w') as f:
      json.dump(movies, f, indent=4)