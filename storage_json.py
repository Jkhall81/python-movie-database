from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        The function loads the information from the JSON or CSV
        file and returns the data.

        Returns:
            a dictionary
        """
        with open(self.file_path, 'r') as f:
            movies = json.load(f)
        return movies

    def add_movie(self, title, year, rating, poster, notes):
        """
        Adds a new movie to the JSON file.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): the URL or path to the movie poster image.
            notes (str): the plot of the movie.

        Returns:
            None
        """
        new_obj = {
            'rating': rating,
            'year of release': year,
            'poster url': poster,
            'notes': notes
            }

        movies = self.list_movies()
        movies[title] = new_obj
        with open(self.file_path, 'w') as f:
            json.dump(movies, f, indent=4)

    def delete_movie(self, title):
        """
        Deletes a movie from the JSON file.

        Returns:
            None
        """
        movies = self.list_movies()

        movie_to_delete = input('Which movie would you like to delete? Movie name: ')
        if movies.get(movie_to_delete) is None:
            print('This movie is not present in the database!')
        else:
            del movies[movie_to_delete]
            print(f'{movie_to_delete} successfully deleted!')

        with open(self.file_path, 'w') as f:
            json.dump(movies, f, indent=4)

    def update_movie(self, title, rating, notes, poster):
        """
        Updates the notes for a movie in the JSON file.

        Args:
            title (str): The title of the movie to update.
            rating (float): The rating of the movie to update.
            notes (str): The updated notes for the movie.
            poster (str): The url of the movie poster.
        """
        movies = self.list_movies()

        if movies.get(title) is None:
            print('This movie is not present in the database!')
        else:
            movies[title]['notes'] = notes
            movies[title]['rating'] = rating
            movies[title]['poster'] = poster

        with open(self.file_path, 'w') as f:
            json.dump(movies, f, indent=4)

    def return_ratings(self):
        """
        Retrieves the ratings of all movies from the JSON file and
        returns them as a list of integers.

        Returns:
            list: A list containing the ratings of all movies as
            integers.
        """
        movies = self.list_movies()

        ratings_list = []

        for item in movies.values():
            rating = item.get('rating')
            if rating is not None:
                ratings_list.append(float(rating))

        return ratings_list
