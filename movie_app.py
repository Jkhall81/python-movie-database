import statistics
import random


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        return movies

    def _command_movie_avg_and_median(self):
        """
        Calculates the average and median ratings of all movies.

        Returns:
            str: A string containing the average rating of all movies.
            str: A string containing the median rating of all movies.
        """
        ratings = self._storage.return_ratings()
        average_rating = statistics.mean(ratings)
        median_rating = statistics.median(ratings)
        str1 = f'The average rating of the movies in the database is {average_rating}.'
        str2 = f'The median rating of movies in the database is {median_rating}.'
        return str1, str2

    def _command_best_and_worst_movies(self):
        movies = self._storage.return_python_data_dict()

        best_movie = max(movies, key=lambda x: movies[x]['rating'])
        worst_movie = min(movies, key=lambda x: movies[x]['rating'])
        best_rating = movies[best_movie]['rating']
        worst_rating = movies[worst_movie]['rating']

        # if several movies have ratings equal to the best_rating then
        # they get put in this list
        list_of_best = (
            [title for title, movie in movies.items() if movie['rating'] == best_rating]
        )
        if len(list_of_best) > 1:
            print('The movies with the highest rating are: ')
            for movie in list_of_best:
                print(movie)
                print(f'Rating: {best_rating}')
        else:
            print(f'The movie with the best rating is: {best_movie}, Rating: {best_rating}')

        list_of_worst = (
            [title for title, movie in movies.items() if movie['rating'] == worst_rating]
        )
        if len(list_of_worst) > 1:
            print('The movies with the lowest rating are: ')
            for item in list_of_worst:
                print(item)
                print(f'Rating: {worst_rating}')
        else:
            print(f'The movie with the lowest rating is: {worst_movie}, Rating: {worst_rating}')

    def _command_random_movie(self):
        """
        Selects a random movie from the list and returns its details.

        Returns:
            str: A string containing the details of the randomly selected movie,
            including its title, rating, and year of release.
        """

        movies = self._storage.return_python_data_dict()

        key, value = random.choice(list(movies.items()))
        print(f'{key}, Rating: {value["rating"]}, Year of Release: {value["year of release"]}')

    def _command_search_movie(self):
        """
        Prompts the user to enter a movie title for searching.

        Returns:
            str: The title of the movie entered by the user.
        """
        movies = self._storage.return_python_data_dict()

        movie_name = input('Enter part of the movie name: ')
        result_str = ''
        for key, value in movies.items():
            if movie_name.lower() in key.lower():
                result_str += (
                    f'{key}, Rating: {movies[key]["rating"]}, Year of Release: {movies[key]["year of release"]}\n'
                    )
        print(result_str)

    def movies_sorted_by_rating(self):
        pass

    def _generate_website(self):
        pass

    def run(self):
        if self._storage is None:
            print('Error: Storage not initialized!')
            return
        # Print menu
        # Get use command
        # Execute command
        pass
