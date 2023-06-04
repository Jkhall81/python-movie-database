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
                year = int(row[1])
                rating = float(row[2])
                poster = row[3]
                notes = row[4]

                movies[title] = {
                    'rating': rating,
                    'year of release': year,
                    'poster url': poster,
                    'notes': notes
                }

        return movies

    def add_movie(self, title, year, rating, poster, notes):
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
        if isinstance(year, str):
            year = int(year)

        movie = {
            'title': title,
            'year of release': year,
            'rating': rating,
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

        data = []

        if title in movies:
            del movies[title]

            for title, movie_info in movies.items():
                movie_obj = {
                    'title': title,
                    'year of release': movie_info['year of release'],
                    'rating': movie_info['rating'],
                    'poster url': movie_info['poster url'],
                    'notes': movie_info['notes']
                }
                data.append(movie_obj)
            fieldnames = ['title', 'year of release', 'rating', 'poster url', 'notes']
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for movie in data:
                    writer.writerow(movie)

        else:
            print('This movie is not present in the database!')

    def update_movie(self, title, rating):
        """
        Updates the information for a movie in the CSV file.

        Args:
            title (str): The title of the movie to update.
            rating (float): The updated rating of the movie.

        Returns:
            None
        """
        movies = self.list_movies()

        if title in movies:
            movies[title]['rating'] = rating
        else:
            print(f'{title} not in the database!')

        data = []
        for title, movie_info in movies.items():
            movie_obj = {
                'title': title,
                'year of release': movie_info['year of release'],
                'rating': movie_info['rating'],
                'poster url': movie_info['poster url'],
                'notes': movie_info['notes']
            }
            data.append(movie_obj)
        fieldnames = ['title', 'year of release', 'rating', 'poster url', 'notes']
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for movie in data:
                writer.writerow(movie)

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
