from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Retrieve a list of movies from the JSON file and display their names, ratings, and release years.

        Returns:
            None
        """
        with open(self.file_path, 'r') as f:
            movies = json.load(f)

        number_of_movies = len(movies.keys())
        print(f'There are {number_of_movies} movies in total!')
        for item in movies:
            output = (
                f'{item}, Rating: {movies[item]["rating"]} '\
                f'Year of Release: {movies[item]["year of release"]}'
            )
            print(output)

    def add_movie(self, title, year, rating, poster):
        pass

    def delete_movie(self, title):
        pass

    def update_movie(self, title, notes):
        pass
