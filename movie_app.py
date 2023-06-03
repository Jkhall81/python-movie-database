import statistics
import random
import requests


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        number_of_movies = int(len(movies))
        print(f'There are {number_of_movies} total!')
        for title, movie_info in movies.items():
            rating = movie_info['rating']
            year_of_release = movie_info['year of release']
            print(f'{title} - Rating: {rating}, Year of Release: {year_of_release}')

    def _command_movie_avg_and_median(self):
        """
        Calculates the average and median ratings of all movies.

        Returns:
            None
        """
        ratings = self._storage.return_ratings()
        average_rating = statistics.mean(ratings)
        median_rating = statistics.median(ratings)
        str1 = f'The average rating of the movies in the database is {average_rating}.'
        str2 = f'The median rating of movies in the database is {median_rating}.'
        print(str1)
        print(str2)

    def _command_best_and_worst_movies(self):
        movies = self._storage.list_movies()

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

        movies = self._storage.list_movies()

        key, value = random.choice(list(movies.items()))
        print(f'{key}, Rating: {value["rating"]}, Year of Release: {value["year of release"]}')

    def _command_search_movie(self):
        """
        Prompts the user to enter a movie title for searching.

        Returns:
            None
        """
        movies = self._storage.list_movies()

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
        movies = self._storage.list_movies()

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
        movies = self._storage.list_movies()

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

    def _command_show_movie_notes(self):
        """
        This function prompts the user to input a movie name, and then pulls up and prints
        the movie notes for that movie.

        Returns:
            None
        """
        movie_title = input('Please enter a movie name! ')
        movies = self._storage.list_movies()
        print(movies[movie_title]['notes'])

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
            10. Movie Notes
            """

        print(menu)
        user_input = input('Enter choice (1-10): ')
        return int(user_input)

    def add_movie_api_call(self):
        """
        This function will get a movie name from the user.  Next it will
        make an api call to get relevant data about the movie.  Finally, it
        will pass that data into the add_movie function.

        Returns:
            None
        """
        movie_title = input('Please enter a movie name: ')

        movie_data = self.api_call(movie_title)

        new_rating = movie_data['imdbRating']
        new_year = int(movie_data['Year'])
        new_poster_url = movie_data['Poster']
        notes = movie_data['Plot']

        self._storage.add_movie(movie_title, new_year, new_rating, new_poster_url, notes)
        print(f'{movie_title} successfully added to database!')
        return

    def movie_update_api_call(self):
        """
        This function prompts the user to input a movie name, that is already in the database,
        and then runs an api call to pull the movie's plot data.  That data is then passed to
        the update_movie method.

        Returns:
             None
        """
        movie_title = input('Enter the name of a movie to update! ')
        movie_data = self.api_call(movie_title)
        notes = movie_data['Plot']
        poster = movie_data['Poster']
        rating = movie_data['imdbRating']

        self._storage.update_movie(movie_title, rating, notes, poster)
        print(f'{movie_title} successfully updated!')

    def api_call(self, title):
        """
        This function makes an API call to retrieve data for a movie with the given title.

        Args:
            title (str): The title of the movie to retrieve data for.

        Returns:
            dict: A dictionary containing the movie data from the API.
        """
        api_key = '3c3d7378'
        api_url = f'http://www.omdbapi.com/?i=tt3896198&apikey={api_key}&t={title}'

        try:
            response = requests.get(api_url)

            if response.status_code != 200:
                print(f'Error: {response.text}')
                return
            movie_data = response.json()

        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return

        if movie_data['Response'] == 'False':
            print(f'Movie "{title}" not found!')
            return

        return movie_data

    def user_interaction(self):
        """
        This function contains a dictionary of functions related to each menu choice.  It will
        take in the user's menu choice and execute the related function.

        Returns:
            None
        """
        function_dict = {
            1: self._command_list_movies,
            2: self.add_movie_api_call,
            3: self._storage.delete_movie,
            4: self.movie_update_api_call,
            5: self.run_stats_functions,
            6: self._command_random_movie,
            7: self._command_search_movie,
            8: self._command_movies_sorted_by_rating,
            9: self._generate_website,
            10: self._command_show_movie_notes
        }

        while True:
            user_input = self.run()
            if user_input == 0:
                print('Bye!')
                break
            function_dict[user_input]()
