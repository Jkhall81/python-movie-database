import statistics


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
        str1 = f'The average rating of the movies in the database is {average_rating}.\n'
        str2 = f'The median rating of movies in the database is {median_rating}'
        return str1, str2

    def _command_best_and_worst_movies(self):
        pass

    def _command_random_movie(self):
        pass

    def search_movie(self):
        pass

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
