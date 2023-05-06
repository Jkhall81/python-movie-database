import statistics
import random
import movie_storage
import json
import website_generator
import poster_url_checker
from movie_storage import MovieAPI

movie_api = MovieAPI('3c3d7378')


# user interface menu
def display_menu():
    """This prints a string that acts as a menu and allows the user to interact with
    the program, and returns the user's menu selection.  This function has no parameters."""
    menu = """********** My Movies Database **********

        Menu:
        0. Exit
        1. List movies
        2. Add movie
        3. Delete movie
        4. Update movie
        5. Stats
        6. Random movie
        7. Search movie
        8. Movies sorted by rating
        9. Check for Movie Poster
        10. Generate website
        """

    print(menu)
    user_input = int(input('Enter choice (1-10): '))
    return user_input


# returns the average, median (of rankings), best, and worst movie
def stats():
    """ This function holds and executes the avg_and_median and best_and_worst_movies
    functions."""

    def avg_and_median():
        """ This function will calculate the average and median ratings of the movies in
        the database and returns two strings containing those values."""
        with open('data.json', 'r') as f:
            movies = json.load(f)

        ratings = [movies[movie]['rating'] for movie in movies]
        average_rating = statistics.mean(ratings)
        median_rating = statistics.median(ratings)
        str1 = f'The average rating of movies in the database is {average_rating}.\n'
        str2 = f'The median rating of movies in the database is {median_rating}.'
        return str1, str2

    def best_and_worst_movies():
        """ This function will find and print out the movies with the highest and lowest rating.
        If more than one movie has the same rating, high or low, it will put those movies in a list
        and print them."""
        with open('data.json', 'r') as f:
            movies = json.load(f)

        best_movie = max(movies, key=lambda x: movies[x]['rating'])
        worst_movie = min(movies, key=lambda x: movies[x]['rating'])
        best_rating = movies[best_movie]['rating']
        worst_rating = movies[worst_movie]['rating']
        list_of_best = [title for title, movie in movies.items() if movie['rating'] == best_rating]
        if len(list_of_best) > 1:
            print('The movies with the highest rating are:')
            for movie in list_of_best:
                print(movie)
        else:
            print(f'The movie with the best rating is: {best_movie}')
        list_of_worst = (
        [title for title, movie in movies.items() if movie['rating'] == worst_rating]
        )
        if len(list_of_worst) > 1:
            print('The movies with the lowest rating are: ')
            for item in list_of_worst:
                print(item)
        else:
            print(f'The movie with the lowest rating is: {worst_movie}')

    avg_rating, median_rating = avg_and_median()
    print(avg_rating, end='')
    print(median_rating)
    best_and_worst_movies()


# displays a random movie and it's rating
def random_movie():
    """ This function randomly prints a movie and it's rating from the database."""
    with open('data.json', 'r') as f:
        movies = json.load(f)

    key, value = random.choice(list(movies.items()))
    print(f'{key}, Rating: {value["rating"]}')


# search for a movie name and displays matching movies and ratings
def search_movie():
    """ This function asks the user to input a movie name or part of a name, and then searches
    the database for a match.  Will match a single word or phrase."""
    with open('data.json', 'r') as f:
            movies = json.load(f)

    movie_name = input('Enter part of the movie name: ')
    result_str = ''
    for key, value in movies.items():
        if movie_name.lower() in key.lower():
            result_str += (
            f'{key}, Rating: {movies[key]["rating"]}, Year of Release: {movies[key]["year of release"]}\n'
            )
    print(result_str)


# movies sorted by rating, descending
def movies_sorted_by_rating():
    """ This function will return a list of all movies sorted, in descending order, by rating.
    It will give The movie name, rating, and release year."""
    with open('data.json', 'r') as f:
        movies = json.load(f)

    sorted_list = sorted(movies, key=lambda x: movies[x]["rating"], reverse=True)
    for movie in sorted_list:
        print(
        f'{movie}, Rating: {movies[movie]["rating"]}, '\
        f'Year of Release: {movies[movie]["year of release"]}'
          )


# create a histogram of ratings
#def create_rating_histogram():
#    rating_list = movies.values()
#    plt.hist(rating_list)
#    plt.title('Ratings')
#    plt.xlabel('Rating')
#    plt.ylabel('Number of Movies')
#    plt.show()
#    save_file = input('Choose a filename to save your histogram to: ')
#    file_name = f'{save_file}.png'
#    plt.savefig(file_name)


# This will tie everything together and make it interactive
def user_interaction():
    """ This function contains a dictionary of functions related to each menu choice.  It will take
     in the user's menu choice and execute the related function."""
    function_dict = {
        1: movie_storage.list_movies,
        2: movie_storage.add_movie,
        3: movie_storage.delete_movie,
        4: movie_storage.update_movie,
        5: stats,
        6: random_movie,
        7: search_movie,
        8: movies_sorted_by_rating,
        9: poster_url_checker.update_movie_posters,
        10: website_generator.generate_website
    }
    while True:
        user_input = display_menu()
        if user_input == 0:
            print('Bye!')
            break
    function_dict[user_input]()


def main():
    """ This is the main function."""
    user_interaction()


if __name__ == "__main__":
    main()
