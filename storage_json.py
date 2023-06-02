from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Retrieve a list of movies from the JSON file and display their
        names, ratings, and release years.

        Returns:
            None
        """
        movies = self.return_python_data_dict()

        number_of_movies = len(movies.keys())
        print(f'There are {number_of_movies} movies in total!')
        for item in movies:
            output = (
                f'{item}, Rating: {movies[item]["rating"]} '\
                f'Year of Release: {movies[item]["year of release"]}'
            )
            print(output)

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the JSON file.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): the URL or path to the movie poster image.

        Returns:
            None
        """
        new_obj = {
            'rating': rating,
            'year of release': year,
            'poster url': poster
            }

        movies = self.return_python_data_dict()
        movies[title] = new_obj
        with open(self.file_path, 'w') as f:
            json.dump(movies, f, indent=4)

    def delete_movie(self, title):
        """
        Deletes a movie from the JSON file.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            None
        """
        movies = self.return_python_data_dict()

        movie_to_delete = input('Which movie would you like to delete? Movie name: ')
        if movies.get(movie_to_delete) is None:
            print('This movie is not present in the database!')
        else:
            del movies[movie_to_delete]
            print(f'{movie_to_delete} successfully deleted!')

        with open(self.file_path, 'w') as f:
            json.dump(movies, f, indent=4)

    def update_movie(self, title, notes):
        """
        Updates the notes for a movie in the JSON file.

        Args:
            title (str): The title of the movie to update.
            notes (str): The updated notes for the movie
        """
        movies = self.return_python_data_dict()

        movie_to_check = input('Enter a movie name: ')
        if movies.get(movie_to_check) is None:
            print('This movie is not present in the database!')
        else:
            movies[movie_to_check]['notes'] = notes

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
        movies = self.return_python_data_dict()

        ratings_list = []

        for item in movies.values():
            rating = item.get('rating')
            if rating is not None:
                ratings_list.append(int(rating))

        return ratings_list

    def return_python_data_dict(self):
        """
        Loads and returns the Python dictionary representation of
        the JSON data stored in the filed specified by 'self.file_
        path'.

        Returns:
            dict: A Python dictionary containing the JSON data
            from the specified file.
        """
        with open(self.file_path, 'r') as f:
            movies = json.load(f)
        return movies
