import statistics
import random
import storage_json


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
            None
        """

        movies = self._storage.return_python_data_dict()

        key, value = random.choice(list(movies.items()))
        print(f'{key}, Rating: {value["rating"]}, Year of Release: {value["year of release"]}')

    def _command_search_movie(self):
        """
        Prompts the user to enter a movie title for searching.

        Returns:
            None
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

    def _command_movies_sorted_by_rating(self):
        """
        Sorts and displays the movies, name and year of release, in the database based
        on their ratings.

        Returns:
            None
        """
        movies = self._storage.return_python_data_dict()

        sorted_list = sorted(movies, key=lambda x: movies[x]['rating'], reverse=True)
        for movie in sorted_list:
            print(
                f'{movie}, Rating: {movies[movie]["rating"]}, '\
                f'Year of Release: {movies[movie]["year of release"]}'
            )

    def _generate_website(self):
        """
        Generates a website based on the movies in the database.

        Returns:
            None
        """
        movies = self._storage.return_python_data_dict()

        with open('_static/index_template.html', 'r') as file:
            template = file.read()

        movie_grid = ''
        for movie_title, movie_data in movies.items():
            rating = movie_data['rating']
            poster_url = movie_data['poster url']
            release_year = movie_data['year of release']

            movie_html = f"""
                <li class='movie'>
                    <h2 class='movie-title'>{movie_title}</h2>
                    <img class='movie-poster' src='{poster_url}' alt='{movie_title} Poster'>
                    <p class='movie-text'>Release Year: {release_year}</p>
                    <p class='movie-text'>Rating: {rating}</p>
                </li>
            """

            movie_grid += movie_html

        html = template.replace('__TEMPLATE_MOVIE_GRID__', movie_grid)

        title = 'My Movie App'
        html = html.replace('__TEMPLATE_TITLE__', title)

        with open('_static/index.html', 'w') as file:
            file.write(html)

        print('Website was generated successfully')

    def run_stats_functions(self):
        """
        This function calls the _command_movie_avg_and_median and _command_best_and_worst_movies
        functions.

        Returns:
            See docstrings of the two above functions for return output.  This function returns
            nothing.
        """
        self._command_movie_avg_and_median()
        self._command_best_and_worst_movies()
        return

    def run(self):
        """
        Runs the movie application.

        Prints the menu, gets the user's command and returns it.

        Returns:
            The user's command.
        """
        if self._storage is None:
            print('Error: Storage not initialized!')
            return

        menu = """********** My Movies Database **********
            
            Menu:
            0. Exit
            1. List Movies
            2. Add Movie
            3. Delete Movie
            4. Update Movie
            5. Stats
            6. Random Movie
            7. Search Movie
            8. Movies Sorted by Rating
            9. Generate Website
            """

        print(menu)
        user_input = int(input('Enter choice (1-9): '))
        return user_input

    def user_interaction(self):
        """
        This function contains a dictionary of functions related to each menu choice.  It will
        take in the user's menu choice and execute the related function.

        Returns:
            None
        """
        function_dict = {
            1: self._command_list_movies,
            2: storage_json.StorageJson.add_movie,
            3: storage_json.StorageJson.delete_movie,
            4: storage_json.StorageJson.update_movie,
            5: self.run_stats_functions,
            6: self._command_random_movie,
            7: self._command_search_movie,
            8: self._command_movies_sorted_by_rating,
            9: self._generate_website
        }

        while True:
            user_input = self.run()
            if user_input == 0:
                print('Bye!')
                break
            function_dict[user_input]()
