class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        pass

    def _command_movie_stats(self):
        pass

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
        # Print menu
        # Get use command
        # Execute command
