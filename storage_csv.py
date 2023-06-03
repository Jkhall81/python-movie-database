import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Loads and returns the data from the CSV file specified by
        'self.file_path' as a dictionary of dictionaries.

        Returns:
            dict: A dictionary of dictionaries containing the data from
            the CSV file. The keys are movie names, and the values are
            dictionaries containing movie information.
        """
        movies = {}
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                title = row[0]
                rating = float(row[2])
                year = int(row[1])
                poster = row[3]
                notes = row[4]

                movie_info = {
                    'rating': rating,
                    'year of release': year,
                    'poster url': poster,
                    'notes': notes
                }

                movies[title] = movie_info

        return movies

    def add_movie(self, title, rating, year, poster, notes):
        """
        Adds a new movie to the CSV file.

        Args:
            title (str): The title of the movie.
            rating (float): The rating of the movie.
            year (int): The release year of the movie.
            poster (str): The URL or path to the movie poster image.
            notes (str): Plot of the movie.

        Returns:
            None
        """
        movie = {
            'title': title,
            'rating': rating,
            'year of release': year,
            'poster url': poster,
            'notes': notes
        }

        with open(self.file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=movie.keys())
            writer.writerow(movie)

    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            None
        """
        movies = self.list_movies()

        if title in movies:
            del movies[title]

            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=movies[list(movies.keys())[0]].keys())
                writer.writeheader()
                writer.writerows(movies.values())

            print(f'{title} successfully deleted!')
        else:
            print('This movie is not present in the database!')

    def update_movie(self, title, rating=None, year=None, poster=None, notes=None):
        """
        Updates the information for a movie in the CSV file.

        Args:
            title (str): The title of the movie to update.
            rating (float, optional): The updated rating of the movie.
            year (int, optional): The updated release year of the movie.
            poster (str, optional): The updated URL or path to the movie poster image.
            notes (str, optional): The updated notes for the movie.

        Returns:
            None
        """
        movies = self.list_movies()

        if title in movies:
            movie = movies[title]

            if rating is not None:
                movie['rating'] = rating
            if year is not None:
                movie['year'] = year
            if poster is not None:
                movie['poster'] = poster

    def return_ratings(self):
        """
        Retrieves the ratings of all movies from the CSV file and
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
