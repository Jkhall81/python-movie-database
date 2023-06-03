from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        The function loads the information from the JSON or CSV
        file and returns the data.

        Returns:
            a dictionary
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster, notes):
        """
        Add a new movie to the storage.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): The URL or path to the movie poster.
            notes (str): The plot of the movie.

        Returns:
            None
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Delete a movie from the storage.

        Returns:
            None
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating, notes, poster):
        """
        Update the notes for a movie in the storage.

        Args:
            title (str): The title of the movie to update.
            rating (float): The rating of the movie to update.
            notes (str): The updated notes for the movie.
            poster (str): The url for the movie poster.

        Returns:
            None
        """
        pass
