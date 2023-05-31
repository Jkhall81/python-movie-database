from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Retrieve a list of movies from storage.

        Returns:
            list: A list of movies.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Add a new movie to the storage.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): The URL or path to the movie poster.

        Returns:
            None
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Delete a movie from the storage.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            None
        """
        pass

    @abstractmethod
    def update_movie(self, title, notes):
        """
        Update the notes for a movie in the storage.

        Args:
            title (str): The title of the movie to update.
            notes (str): The updated notes for the movie.

        Returns:
            None
        """
        pass
